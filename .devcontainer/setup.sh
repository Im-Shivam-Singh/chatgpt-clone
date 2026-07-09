#!/usr/bin/env bash

set -e

echo "======================================="
echo "ChatGPT Clone"
echo "======================================="

echo ""
echo "Python:"
python --version

echo ""
echo "UV:"
uv --version

echo ""
echo "Terraform:"
terraform version

echo ""
echo "Azure CLI:"
az version

echo ""
echo "Docker:"
docker --version

echo ""
echo "Installing Python dependencies..."

#!/usr/bin/env bash
set -e

for service in gateway chat-service ai-agent
do
    if [ -f "$service/pyproject.toml" ]; then
        echo "Setting up $service..."
        (
            cd "$service"
            uv sync
        )
    fi
done

echo ""
echo "Setup Complete!"