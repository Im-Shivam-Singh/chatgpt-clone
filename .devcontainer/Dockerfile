FROM mcr.microsoft.com/devcontainers/python:3.12

USER root

# -----------------------------------------------------
# Install system packages
# -----------------------------------------------------
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    gnupg \
    lsb-release \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------
# Install Node.js 22 LTS
# -----------------------------------------------------
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs

# -----------------------------------------------------
# Install uv
# -----------------------------------------------------
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY --from=ghcr.io/astral-sh/uv:latest /uvx /usr/local/bin/uvx

# -----------------------------------------------------
# Install Azure CLI
# -----------------------------------------------------
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# -----------------------------------------------------
# Install Terraform
# -----------------------------------------------------
RUN wget -qO- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    > /etc/apt/sources.list.d/hashicorp.list && \
    apt-get update && \
    apt-get install -y terraform

# -----------------------------------------------------
# Install Docker CLI
# -----------------------------------------------------
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | \
    gpg --dearmor -o /usr/share/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
    > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------
# Verify installations
# -----------------------------------------------------
RUN python --version && \
    node --version && \
    npm --version && \
    git --version && \
    uv --version && \
    terraform version && \
    docker --version && \
    az version

USER vscode

WORKDIR /workspaces