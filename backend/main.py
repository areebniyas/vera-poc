from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI(title="Verdentra HR Chatbot API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Azure OpenAI client
try:
    chat_client = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("OPEN_AI_ENDPOINT"),
        api_key=os.getenv("OPEN_AI_KEY")
    )
except Exception as e:
    print(f"Error initializing Azure OpenAI client: {e}")
    chat_client = None

# Pydantic models
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    response: str
    status: str

# Store chat sessions (in production, use a proper database)
chat_sessions: Dict[str, List[ChatMessage]] = {}

@app.get("/")
async def root():
    return {"message": "Verdentra HR Chatbot API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "openai_client": chat_client is not None}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        if not chat_client:
            raise HTTPException(status_code=500, detail="OpenAI client not initialized")
        
        # Initialize prompt with system message
        prompt = [
            {
                "role": "system", 
                "content": "You are an HR Assistant chatbot for Verdentra. Your role is to answer employee questions using only the data provided from the data source indexed in Azure Search AI. Your primary goal is to provide clear, accurate, and policy-compliant responses. Be professional, helpful, and concise."
            }
        ]
        
        # Add chat history
        for msg in request.history:
            prompt.append({"role": msg.role, "content": msg.content})
        
        # Add current user message
        prompt.append({"role": "user", "content": request.message})
        
        # RAG parameters for Azure Search
        rag_params = {
            "data_sources": [
                {
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": os.getenv("SEARCH_ENDPOINT"),
                        "index_name": os.getenv("INDEX_NAME"),
                        "authentication": {
                            "type": "api_key",
                            "key": os.getenv("SEARCH_KEY"),
                        },
                        "query_type": "vector",
                        "embedding_dependency": {
                            "type": "deployment_name",
                            "deployment_name": os.getenv("EMBEDDING_MODEL"),
                        },
                    }
                }
            ],
        }
        
        # Get response from Azure OpenAI
        response = chat_client.chat.completions.create(
            model=os.getenv("CHAT_MODEL"),
            messages=prompt,
            extra_body=rag_params,
            temperature=0.7,
            max_tokens=500
        )
        
        completion = response.choices[0].message.content
        
        return {"response": completion, "status": "success"}
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/clear-history")
async def clear_history():
    return {"message": "History cleared", "status": "success"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)