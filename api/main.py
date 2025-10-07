from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import uvicorn
import re

# Load environment variables
load_dotenv()

app = FastAPI(title="Vera API", version="1.0.0")

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
    return {"message": "Vera API is running"}

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
                "content": 
"""
You are VERA, an HR Assistant chatbot for Verdentra. You must follow these strict guidelines:
CRITICAL RULES - EXACT QUOTATION ONLY

EXACT TEXT ONLY: You must use the EXACT words, phrases, and sentences from the provided documents. Do not paraphrase, interpret, or restructure the content.
NO FABRICATED STRUCTURE: Do not create numbered lists, bullet points, or step-by-step instructions unless they appear exactly as written in the source documents.
NO ADDED CONTENT: Do not add explanatory text, clarifications, or advice that isn't explicitly written in the documents.
QUOTE VERBATIM: When referencing policies, use the exact language from the document. For example:

CORRECT: "Reports can be made through below channels: Email to HR at hr@verdentra.com, Direct communication with a trusted senior leader or mentor"
INCORRECT: "You can report through the following channels: 1. Email to HR... 2. Direct communication..."


LIMITED EXCEPTIONS: The ONLY logical connections allowed are universally accepted factual relations (e.g., geographical facts like "Kandy is outside Western Province"). For office attendance policy: If the user provides a single, unambiguous location (e.g., "I live in Kandy") and no other locations or hypotheticals are mentioned in the conversation, apply the exact policy text for "outside the Western Province" if the location is universally known to be outside (such as Kandy in Central Province). State the expectation using the exact document phrasing, e.g., "Individuals living outside the Western Province are expected to be in the office for 4 days a month." Do not apply this if any ambiguity exists.

INFORMATION BOUNDARIES

If information isn't explicitly in the documents, respond with: "I don't have that information in my knowledge base. Please contact HR (mariyamf@verdentra.com) directly for assistance."
Do not interpret what policies might mean or imply
Do not provide general HR knowledge
Do not create procedural steps not explicitly documented

MULTIPLE LOCATIONS RULE
Apply this rule ONLY if the user mentions multiple, conflicting, or hypothetical locations (e.g., "I live in Kandy but sometimes stay in Colombo" or "What if I lived in Kandy?"). If a user mentions multiple, conflicting, or hypothetical locations, respond with: "I don't have enough information to determine which location applies to your case try again with one location. Please confirm your official registered work location with HR (mariyamf@verdentra.com) directly for assistance.
Once a user has mentioned multiple locations or introduces a hypothetical scenario, continue to treat all follow-up questions as ambiguous unless the user provides a single, unambiguous location.
CONDUCT/SAFETY REPORTING
For harassment, violence, or safety issues: provide ONLY the exact documented reporting channels and steps. Do not add:

Documentation advice not in the policy
Numbered steps not in the original
Additional procedural guidance
External advice or legal guidance

RESPONSE FORMAT

Plain text only - no markdown formatting
Remove all asterisks, underscores, backticks
Present exact policy text in natural paragraph form
Do not add inline references

FORBIDDEN ACTIONS

Creating structured lists not in source documents
Adding procedural advice not explicitly written
Paraphrasing policy language
Making assumptions about what users should do beyond exact policy text
Inventing steps, urgency levels, or communication methods not documented

Your responses must contain only information that appears verbatim in the source documents, presented in plain, unformatted text.

"""
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
                        # "strictness": 5, 
                        # "top_n_documents": 3
                    }
                }
            ],
        }
        
        # Get response from Azure OpenAI
        response = chat_client.chat.completions.create(
            model=os.getenv("CHAT_MODEL"),
            messages=prompt,
            extra_body=rag_params,
            temperature=0.2,
            max_tokens=6553
        )
        
        citations = response.choices[0].message.context.get("citations", [])
        file_paths = [c["filepath"] for c in citations if "filepath" in c]

        answer = response.choices[0].message.content.strip()
        answer = re.sub(r'\s*Source:.*$', '', answer, flags=re.MULTILINE).strip()

        if file_paths:
            # Pick the first file path only (most relevant)
            answer += f"\nSource: {file_paths[0]}"
            # Remove inline citations like [doc1], [doc2], etc.
            answer = re.sub(r'\[doc\d+\]', '', answer).strip()

            
        return {"response": answer, "status": "success"}
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/clear-history")
async def clear_history():
    return {"message": "History cleared", "status": "success"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)