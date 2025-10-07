# VERA API - Backend Service

This is the backend API service for VERA, built with FastAPI and powered by Azure AI services.

## Overview

The API backend provides RESTful endpoints for chat interactions, integrating Azure OpenAI for natural language understanding and Azure Cognitive Search for knowledge retrieval. It implements RAG (Retrieval Augmented Generation) to provide accurate, context-aware responses to HR-related queries.

## Technology Stack

- **Framework**: FastAPI 0.100+
- **Language**: Python 3.11 or 3.12
- **ASGI Server**: Uvicorn
- **AI Services**: Azure OpenAI
- **Search**: Azure Cognitive Search
- **Configuration**: python-dotenv
- **HTTP Client**: OpenAI Python SDK

## Project Structure

```
api/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (not in version control)
├── .env.example           # Example environment configuration
└── README.md              # This file
```

## Getting Started

### Prerequisites

- Python 3.11 or 3.12 (Python 3.13 not recommended due to dependency compatibility)
- pip package manager
- Virtual environment tool (venv)
- Azure OpenAI service with deployed models
- Azure Cognitive Search service with indexed data

### Installation

1. **Navigate to the API directory**
   ```bash
   cd api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```powershell
   .\venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   
   Create a `.env` file in the `api` directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your Azure service credentials (see Configuration section below).

6. **Start the development server**
   ```bash
   python main.py
   ```
   
   The API will be available at `http://localhost:8000`

## Configuration

### Environment Variables

Create a `.env` file with the following configuration:

```env
# Azure OpenAI Configuration
OPEN_AI_ENDPOINT=https://[YOUR-RESOURCE-NAME].openai.azure.com/
OPEN_AI_KEY=[YOUR-AZURE-OPENAI-KEY]
CHAT_MODEL=[YOUR-CHAT-MODEL-DEPLOYMENT-NAME]
EMBEDDING_MODEL=[YOUR-EMBEDDING-MODEL-DEPLOYMENT-NAME]
# Azure Cognitive Search Configuration
SEARCH_ENDPOINT=https://[YOUR-SEARCH-SERVICE].search.windows.net
SEARCH_KEY=[YOUR-AZURE-SEARCH-KEY]
INDEX_NAME=[YOUR-SEARCH-INDEX-NAME]

# Optional: API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

### CORS Configuration

The API is configured to accept requests from specific origins. Update `main.py` for your environment:

### Code Style Guidelines

**Follow PEP 8 guidelines:**
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter default)
- Use type hints for function parameters and return values
- Write docstrings for all functions and classes

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and run `pip install -r requirements.txt` |
| Port 8000 already in use | Kill the process using port 8000: `lsof -ti:8000 \| xargs kill -9` (macOS/Linux) or change port in `main.py` |
| Azure OpenAI timeout | Check network connectivity, verify endpoint URL, ensure API key is valid |
| CORS errors | Update `allow_origins` in CORS middleware configuration |
| 401 Unauthorized from Azure | Verify API keys haven't expired, check Azure portal for key rotation |
| Import errors | Use Python 3.11 or 3.12, avoid Python 3.13 |

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure Cognitive Search Documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Python Best Practices](https://docs.python-guide.org/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
