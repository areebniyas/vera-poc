# VERA

An enterprise-grade HR assistant chatbot built with Next.js and FastAPI, powered by Azure OpenAI and Azure Cognitive Search. This application provides employees with instant access to HR policies, procedures, and information through an intelligent conversational interface.

## 🚀 Features

- **Modern Chat Interface**: Clean, responsive UI built with Next.js and shadcn/ui components
- **AI-Powered Responses**: Leverages Azure OpenAI with RAG (Retrieval Augmented Generation)
- **Enterprise Search**: Integrated with Azure Cognitive Search for accurate information retrieval
- **Real-time Communication**: WebSocket-like experience with instant message delivery
- **Professional Design**: Minimalistic and user-friendly interface suitable for corporate environments
- **Conversation History**: Maintains context throughout the conversation
- **Error Handling**: Robust error management and graceful fallbacks

## 🏗️ Architecture

- **Frontend**: Next.js 14 with TypeScript, Tailwind CSS, and shadcn/ui
- **Backend**: FastAPI with Azure OpenAI integration
- **AI Services**: Azure OpenAI (GPT models) + Azure Cognitive Search
- **Styling**: Modern design system with dark/light mode support

## 📁 Project Structure

```
verdentra-hr-chatbot/
├── README.md
├── .gitignore
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt        # Python dependencies
│   ├── .env                   # Environment variables (not committed)
│   └── venv/                  # Python virtual environment
└── verdentra-hr-chatbot/      # Next.js frontend
    ├── src/
    │   ├── app/
    │   │   ├── globals.css
    │   │   ├── layout.tsx
    │   │   └── page.tsx       # Main chat interface
    │   ├── components/
    │   │   └── ui/            # shadcn/ui components
    │   └── lib/
    │       └── utils.ts
    ├── package.json
    ├── tailwind.config.js
    ├── components.json
    └── next.config.js
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.11+ (Python 3.13 may have compatibility issues)
- Node.js 18+ and npm
- Azure OpenAI account with deployed models
- Azure Cognitive Search service with indexed HR data

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn python-dotenv openai "pydantic>=1.10.0,<2.0.0"
   ```

4. **Create .env file:**
   ```env
   OPEN_AI_ENDPOINT=your_azure_openai_endpoint
   OPEN_AI_KEY=your_azure_openai_key
   CHAT_MODEL=your_chat_model_deployment_name
   EMBEDDING_MODEL=your_embedding_model_deployment_name
   SEARCH_ENDPOINT=your_azure_search_endpoint
   SEARCH_KEY=your_azure_search_key
   INDEX_NAME=your_search_index_name
   ```

5. **Start the backend server:**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to project root and create Next.js app:**
   ```bash
   npx create-next-app@latest verdentra-hr-chatbot --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
   cd verdentra-hr-chatbot
   ```

2. **Initialize shadcn/ui:**
   ```bash
   npx shadcn@latest init
   ```
   Choose the following options:
   - TypeScript: Yes
   - Style: Default
   - Color: Slate (or your preference)
   - CSS file: src/app/globals.css
   - CSS variables: Yes
   - Tailwind config: tailwind.config.js
   - Components alias: src/components
   - Utils alias: src/lib/utils

3. **Install shadcn components:**
   ```bash
   npx shadcn@latest add button input scroll-area avatar badge
   ```

4. **Replace src/app/page.tsx** with the chat interface component from this repository.

5. **Start the development server:**
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:3000`

## 🚀 Usage

1. Start both backend (`python main.py`) and frontend (`npm run dev`) servers
2. Open `http://localhost:3000` in your browser
3. Start chatting with the HR assistant
4. Ask questions about HR policies, benefits, procedures, etc.

## 📡 API Endpoints

- `GET /` - API status check
- `GET /health` - Health check with Azure OpenAI connection status
- `POST /chat` - Main chat endpoint
  ```json
  {
    "message": "What is the vacation policy?",
    "history": [
      {"role": "user", "content": "Previous message"},
      {"role": "assistant", "content": "Previous response"}
    ]
  }
  ```
- `POST /clear-history` - Clear conversation history

## 🎨 Customization

### Styling
- Modify `src/app/globals.css` for global styles
- Update `tailwind.config.js` for theme customization
- Components are in `src/components/ui/` and fully customizable

### Branding
- Update company name references in the code
- Modify colors and styling in the chat interface
- Add your company logo to the header

## 🔧 Configuration

### Environment Variables (Backend)
All Azure service configurations are managed through environment variables in the backend `.env` file.

### CORS Configuration
The backend is configured to accept requests from `http://localhost:3000` by default. Update the CORS settings in `main.py` for production deployment.

## 🚀 Deployment

### Backend Deployment
- Deploy to Azure App Service, AWS Lambda, or any cloud provider
- Update CORS origins to include your production domain
- Set environment variables in your deployment platform

### Frontend Deployment
- Deploy to Vercel, Netlify, or any static hosting service
- Update the API endpoint URL in the frontend code
- Configure build settings for Next.js

## 🛡️ Security Considerations

- API keys are stored securely in environment variables
- CORS is configured for specific origins
- No sensitive data is logged or stored in the frontend
- All API communications should use HTTPS in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Rust compilation errors**: Use Python 3.11 or 3.12 instead of 3.13
2. **CORS errors**: Ensure backend is running on port 8000
3. **Azure connection issues**: Verify environment variables are correctly set
4. **Package installation failures**: Try installing dependencies one by one

### Support

For issues and questions, please open a GitHub issue or contact the development team.

---

**Built with ❤️ for Verdentra**