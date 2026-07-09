FROM mcr.microsoft.com/devcontainers/python:3.12

USER root

# ---------- Install basic packages ----------
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    gnupg \
    software-properties-common \
    lsb-release

# ---------- Install uv ----------
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

# ---------- Install Azure CLI ----------
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# ---------- Install Terraform ----------
RUN wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/hashicorp.list && \
    apt-get update && \
    apt-get install -y terraform

USER vscode