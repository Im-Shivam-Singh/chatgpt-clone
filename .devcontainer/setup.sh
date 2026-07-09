#!/usr/bin/env bash

set -e

echo ""
echo "========================================"
echo "🚀 Enterprise AI Platform Setup"
echo "========================================"
echo ""

#######################################################
# Verify tools
#######################################################

echo "Checking required tools..."

command -v python >/dev/null || { echo "❌ Python not found"; exit 1; }
command -v uv >/dev/null || { echo "❌ uv not found"; exit 1; }
command -v node >/dev/null || { echo "❌ Node.js not found"; exit 1; }
command -v npm >/dev/null || { echo "❌ npm not found"; exit 1; }

echo "✅ Required tools found."
echo ""

#######################################################
# Python Services
#######################################################

echo "📦 Installing Python dependencies..."

for service in gateway chat-service ai-service
do
    if [ -d "$service" ]; then

        echo ""
        echo "→ Setting up $service"

        (
            cd "$service"

            if [ -f ".env.example" ] && [ ! -f ".env" ]; then
                cp .env.example .env
                echo "   ✅ Created .env"
            fi

            if [ -f "pyproject.toml" ]; then
                uv sync
            fi
        )
    fi
done

#######################################################
# Frontend
#######################################################

if [ -d "frontend" ]; then

    echo ""
    echo "📦 Setting up Frontend"

    (
        cd frontend

        if [ -f ".env.example" ]; then
            cp .env.example .env
            echo "   ✅ Created .env"
        fi

        npm install

        # Initialize shadcn only if not already initialized
        if [ ! -f "components.json" ]; then

            echo ""
            echo "Initializing shadcn/ui..."

            npx shadcn@latest init --yes || true

        fi
    )
fi

#######################################################
# Finished
#######################################################

echo ""
echo "========================================"
echo "✅ Setup Complete!"
echo "========================================"
echo ""

echo "Installed Versions"
echo "------------------"

python --version
echo ""

uv --version
echo ""

node --version
echo ""

npm --version
echo ""

terraform version | head -1
echo ""

az version | head -5 || true

echo ""
echo "🎉 Repository is ready!"
echo ""
echo "Run the services using:"
echo ""
echo "Gateway      : uv run uvicorn app.main:app --reload --port 8000"
echo "Chat Service : uv run uvicorn app.main:app --reload --port 8001"
echo "AI Service   : uv run uvicorn app.main:app --reload --port 8002"
echo "Frontend     : npm run dev"
echo ""