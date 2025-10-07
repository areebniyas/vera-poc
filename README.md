# VERA

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)

## Overview

VERA leverages Azure AI services to provide employees with instant access to HR policies, procedures, and organizational information through an intelligent conversational interface.

### Key Capabilities

- **AI-Powered Conversational Interface**: Natural language processing using Azure OpenAI with Retrieval Augmented Generation (RAG)
- **Enterprise Knowledge Base**: Integration with Azure Cognitive Search for accurate, context-aware information retrieval
- **Modern Web Application**: Responsive frontend built with Next.js 15 and TypeScript
- **RESTful API Backend**: High-performance FastAPI service with async request handling
- **Conversation Context Management**: Maintains conversation history for coherent multi-turn interactions
- **Enterprise-Ready Security**: Environment-based configuration with secure credential management

## Architecture

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Frontend | Next.js 15, TypeScript, Tailwind CSS | User interface and client-side logic |
| UI Components | shadcn/ui, Radix UI | Accessible, customizable component library |
| API Backend | FastAPI, Python 3.11+ | RESTful API service layer |
| AI Services | Azure OpenAI | Natural language understanding and generation |
| Search | Azure Cognitive Search | Enterprise knowledge base indexing and retrieval |
| Styling | Tailwind CSS v4 | Utility-first CSS framework |

### System Architecture

```
┌─────────────────┐
│       Users     │
└────────┬────────┘
         │
    ┌────▼────┐
    │  Web UI │ (Next.js)
    └────┬────┘
         │ HTTP/REST
    ┌────▼────┐
    │   API   │ (FastAPI)
    └────┬────┘
         │
    ┌────┴─────────────────┐
    │                      │
┌───▼────────┐    ┌───────▼──────┐
│Azure OpenAI│    │Azure Cognitive│
│            │    │    Search     │
└────────────┘    └───────────────┘
```

## Repository Structure

```
vera/
├── README.md                   # This file
├── .gitignore                  # Git ignore patterns
├── api/                        # Backend API service
│   ├── README.md              # API-specific documentation
│   ├── main.py                # FastAPI application entry point
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables (not in version control)
└── web/                       # Frontend application
    ├── README.md              # Frontend-specific documentation
    ├── src/
    │   ├── app/               # Next.js app directory
    │   │   ├── globals.css    # Global styles
    │   │   ├── layout.tsx     # Root layout
    │   │   └── page.tsx       # Main chat interface
    │   ├── components/        # React components
    │   │   └── ui/            # shadcn/ui component library
    │   └── lib/               # Utility functions
    │       └── utils.ts       # Helper utilities
    ├── package.json           # Node.js dependencies
    ├── tsconfig.json          # TypeScript configuration
    ├── next.config.ts         # Next.js configuration
    ├── tailwind.config.js     # Tailwind CSS configuration
    └── components.json        # shadcn/ui configuration
```

## Prerequisites

### Development Environment

- **Python**: 3.11 or 3.12 (Note: Python 3.13 may have dependency compatibility issues)
- **Node.js**: 18.x or higher
- **Package Manager**: npm 9.x or higher
- **Git**: 2.x or higher

### Azure Services

The following Azure resources are required:

- **Azure OpenAI Service**: Deployed GPT model for chat completion
- **Azure OpenAI Embeddings**: Deployed embedding model for semantic search
- **Azure Cognitive Search**: Search service with indexed HR documentation
- **Azure Subscription**: Active subscription with appropriate permissions

### Required Access

- Azure portal access with permissions to:
  - Read Azure OpenAI endpoints and keys
  - Read Azure Cognitive Search endpoints and keys
- Repository access with appropriate permissions for your organization

## Getting Started

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vera
   ```

2. **Set up the API backend**
   ```bash
   cd api
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create `api/.env` file with the following configuration:
   ```env
   OPEN_AI_ENDPOINT=<your-azure-openai-endpoint>
   OPEN_AI_KEY=<your-azure-openai-key>
   CHAT_MODEL=<your-chat-model-deployment-name>
   EMBEDDING_MODEL=<your-embedding-model-deployment-name>
   SEARCH_ENDPOINT=<your-azure-search-endpoint>
   SEARCH_KEY=<your-azure-search-key>
   INDEX_NAME=<your-search-index-name>
   ```

4. **Start the API server**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

5. **Set up the frontend** (in a new terminal)
   ```bash
   cd web
   npm install
   npm run dev
   ```
   The application will be available at `http://localhost:3000`

## Development

### API Development

See the [API README](./api/README.md) for detailed backend development guidelines.

**Local Development:**
```bash
cd api
python main.py
```

The API server runs on `http://localhost:8000` with auto-reload enabled for development.

**Available Scripts:**
- `npm run dev` - Start development server with Turbopack
- `npm run build` - Build production bundle
- `npm run start` - Start production server
- `npm run lint` - Run ESLint code quality checks

### Code Quality

**Python (API):**
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Document functions and classes with docstrings

**TypeScript (Web):**
- Use TypeScript strict mode
- Follow ESLint configuration
- Use functional components with React hooks
- Maintain component modularity

## Testing

### API Testing

```bash
cd api
pytest
```

### Frontend Testing

```bash
cd web
npm test
```

## Configuration

### Environment Variables

All sensitive configuration is managed through environment variables. Never commit `.env` files to version control.

**Required API Environment Variables:**

| Variable | Description | Example |
|----------|-------------|---------|
| `OPEN_AI_ENDPOINT` | Azure OpenAI service endpoint | `https://<resource>.openai.azure.com/` |
| `OPEN_AI_KEY` | Azure OpenAI API key | `<32-character-key>` |
| `CHAT_MODEL` | Deployed chat model name | `gpt-4` |
| `EMBEDDING_MODEL` | Deployed embedding model name | `text-embedding-ada-002` |
| `SEARCH_ENDPOINT` | Azure Cognitive Search endpoint | `https://<service>.search.windows.net` |
| `SEARCH_KEY` | Azure Cognitive Search API key | `<32-character-key>` |
| `INDEX_NAME` | Search index name | `hr-policies` |

### CORS Configuration

The API is configured to accept requests from `http://localhost:3000` during development. For production deployments, update the CORS origins in `api/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-production-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## API Reference

### Endpoints

#### `GET /`
Health check endpoint for API status verification.

**Response:**
```json
{
  "status": "ok",
  "service": "VERA HR Assistant API"
}
```

#### `GET /health`
Comprehensive health check including Azure service connectivity.

**Response:**
```json
{
  "status": "healthy",
  "azure_openai": "connected",
  "timestamp": "2025-10-07T12:00:00Z"
}
```

#### `POST /chat`
Main chat endpoint for conversational interactions.

**Request Body:**
```json
{
  "message": "How many days should I come to office?",
  "history": [
    {"role": "user", "content": "Previous question"},
    {"role": "assistant", "content": "Previous response"}
  ]
}
```

**Response:**
```json
{
  "response": "According to the HR policy...",
  "sources": ["policy-doc-123"]
}
```

#### `POST /clear-history`
Clear conversation history for a fresh session.

## Contributing

### Branching Strategy

- `main` - Production-ready code
- `development` - Integration branch for features
- `feature/*` - Individual feature branches
- `hotfix/*` - Critical production fixes

### Contribution Workflow

1. Create a feature branch from `develop`
   ```bash
   git checkout -b feature/your-feature-name develop
   ```

2. Make your changes following code quality guidelines

3. Write or update tests as needed

4. Commit changes with descriptive messages
   ```bash
   git commit -m "feat: add user authentication feature"
   ```

5. Push to the remote repository
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request to `develop` branch

7. Ensure CI/CD pipeline passes

8. Request code review from team members

### Commit Message Convention

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## Support and Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Python dependency compilation errors | Use Python 3.11 or 3.12. Python 3.13 may have compatibility issues with some dependencies. |
| CORS errors in browser console | Verify API is running on port 8000 and CORS origins are configured correctly in `main.py` |
| Azure OpenAI connection failures | Confirm environment variables are set correctly and Azure OpenAI service is accessible from your network |
| 401 Unauthorized from Azure services | Verify API keys are valid and have not expired. Check Azure portal for key rotation. |
| Module not found errors (Python) | Ensure virtual environment is activated and all dependencies are installed via `pip install -r requirements.txt` |
| npm install failures (Node.js) | Clear npm cache (`npm cache clean --force`) and try again. Ensure Node.js version is 18 or higher. |


### Technologies

- [Next.js](https://nextjs.org/) - React framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) - AI services
- [Azure Cognitive Search](https://azure.microsoft.com/en-us/products/search) - Enterprise search
- [shadcn/ui](https://ui.shadcn.com/) - UI component library
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
