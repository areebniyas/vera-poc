````markdown
# VERA Web - Frontend Application

This is the frontend application for VERA (Virtual Employee Resource Assistant), built with Next.js 15, TypeScript, and Tailwind CSS.

## Overview

The web frontend provides an intuitive chat interface for employees to interact with the VERA HR assistant. It features a modern, responsive design built with shadcn/ui components and integrates seamlessly with the FastAPI backend.

## Technology Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS v4
- **UI Components**: shadcn/ui (Radix UI primitives)
- **State Management**: React hooks
- **HTTP Client**: Fetch API
- **Build Tool**: Turbopack (Next.js 15 default)

## Project Structure

```
web/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── layout.tsx         # Root layout component
│   │   ├── page.tsx           # Main chat interface
│   │   ├── globals.css        # Global styles and Tailwind directives
│   │   └── favicon.ico        # Application favicon
│   ├── components/            # React components
│   │   └── ui/                # shadcn/ui component library
│   │       ├── avatar.tsx     # Avatar component
│   │       ├── badge.tsx      # Badge component
│   │       ├── button.tsx     # Button component
│   │       ├── input.tsx      # Input component
│   │       └── scroll-area.tsx # Scroll area component
│   └── lib/                   # Utility functions
│       └── utils.ts           # Helper utilities (cn, etc.)
├── public/                    # Static assets
├── components.json            # shadcn/ui configuration
├── next.config.ts             # Next.js configuration
├── tsconfig.json              # TypeScript configuration
├── tailwind.config.mjs        # Tailwind CSS configuration
├── postcss.config.mjs         # PostCSS configuration
├── eslint.config.mjs          # ESLint configuration
└── package.json               # Node.js dependencies and scripts
```

## Getting Started

### Prerequisites

- Node.js 18.x or higher
- npm 9.x or higher
- Running API backend (see [../api/README.md](../api/README.md))

### Installation

1. **Navigate to the web directory**
   ```bash
   cd web
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure API endpoint** (if needed)
   
   Update the API base URL in the application code if not using the default `http://localhost:8000`.

4. **Start the development server**
   ```bash
   npm run dev
   ```

5. **Open the application**
   
   Navigate to [http://localhost:3000](http://localhost:3000) in your browser.

## Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server with Turbopack (hot reload enabled) |
| `npm run build` | Build production-optimized bundle |
| `npm run start` | Start production server (requires build first) |
| `npm run lint` | Run ESLint for code quality checks |

### Development Workflow

```bash
# Start development with hot reload
npm run dev

# Build and test production bundle locally
npm run build
npm run start

# Run linter
npm run lint
```

## Development Guidelines

### Component Development

**File naming conventions:**
- Components: PascalCase (e.g., `ChatInterface.tsx`)
- Utilities: camelCase (e.g., `formatMessage.ts`)
- Styles: kebab-case (e.g., `chat-styles.css`)

## API Integration

### API Configuration

The frontend communicates with the FastAPI backend. Update the API base URL as needed:

**For Development:**
```typescript
const API_BASE_URL = 'http://localhost:8000';
```

**For Production:**
```typescript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://[YOUR-API-DOMAIN]'; // TODO: Update with published backend URL
```

### API Endpoints Used

- `POST /chat` - Send chat messages and receive AI responses
- `POST /clear-history` - Clear conversation history
- `GET /health` - Check API health status

## Configuration

### Environment Variables

Create a `.env.local` file for local development (not committed to version control):

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=VERA
```

### TypeScript Configuration

The project uses strict TypeScript settings. Key configurations in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true
  }
}
```
## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Module not found` errors | Run `npm install` to ensure all dependencies are installed |
| Port 3000 already in use | Kill the process using port 3000 or use `npm run dev -- -p 3001` to use a different port |
| API connection errors | Verify the API backend is running on port 8000 and CORS is configured |
| Build failures | Clear `.next` directory and `node_modules`, then reinstall: `rm -rf .next node_modules && npm install` |
| TypeScript errors | Run `npx tsc --noEmit` to see all type errors |
| Styling not applied | Ensure Tailwind CSS is properly configured and PostCSS is processing correctly |

```

## Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com/)
- [Radix UI Documentation](https://www.radix-ui.com/)
