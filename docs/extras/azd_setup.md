# Azure Developer CLI (azd) Setup Guide

## What is azd?
**azd** stands for Azure Developer CLI and is pronounced "az-dee" (A-Z-D). It is a command-line tool from Microsoft that helps developers build, deploy, and manage cloud applications on Azure using best practices.

## Key Features
- Scaffold new projects with best-practice templates
- Provision Azure resources (infrastructure) using Infrastructure as Code (IaC)
- Deploy your application code to Azure
- Manage environments (dev, test, prod)
- Integrate with CI/CD tools like GitHub Actions

## How to Install azd (on Windows)
Open PowerShell and run:
```pwsh
winget install microsoft.azd
```
Or follow the official instructions:  
https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd

## Basic Workflow
1. **Initialize a project**
   ```pwsh
   azd init
   ```
   - **What it does:**
     - Prompts you to select a project template (or use your own code/infra).
     - Sets up an `azd.yaml` file describing your app, services, and infra.
     - Creates a `.azure/` folder for environment and state management.
     - Optionally scaffolds sample code and infrastructure (if using a template).
   - **About templates:**
     - azd templates are pre-built, best-practice solutions for common Azure scenarios (web apps, microservices, serverless, data/AI, full-stack, etc.).
     - You can browse available templates at:
       - [Official azd template gallery](https://azure.github.io/azure-dev/)
       - [Microsoft Learn: azd templates](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/templates)
     - Choose a template that matches your tech stack and architecture, or select "empty"/"custom" to use your own code and infrastructure.
     - Templates include sample code, infrastructure-as-code (Bicep), and configuration for rapid setup.
   - **Result:**
     - Your project is now azd-enabled, with configuration files for deployment and environment management.

2. **Provision Azure resources**
   ```pwsh
   azd provision
   ```
   - **What it does:**
     - Reads your infrastructure-as-code files (e.g., Bicep in `infra/`).
     - Deploys all required Azure resources (e.g., databases, web apps, key vaults) to your selected environment.
     - Stores environment-specific outputs (like connection strings) in `.env` files.
   - **Result:**
     - All Azure infrastructure for your app is created and ready for use.

3. **Deploy your app**
   ```pwsh
   azd deploy
   ```
   - **What it does:**
     - Builds and deploys your application code (frontend, backend, etc.) to the provisioned Azure resources.
     - Uses the environment settings and outputs from the provision step.
   - **Result:**
     - Your app is live and running on Azure, connected to the provisioned resources.

4. **Manage environments**
   ```pwsh
   azd env list
   azd env select <env-name>
   azd env new <env-name>
   ```
   - **What it does:**
     - Lets you create, list, and switch between multiple environments (e.g., dev, test, prod).
     - Each environment has its own Azure resources and configuration.
   - **Result:**
     - You can easily manage separate deployments for different stages or teams, with isolated resources and settings.

## Example: End-to-End Flow
```pwsh
azd init           # Set up your project (choose template, name, etc.)
azd provision      # Create Azure resources defined in your IaC files
azd deploy         # Deploy your app code to Azure
azd monitor        # (Optional) Monitor your app and resources
```

## Learn More
- [Official azd documentation](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
- [Quickstart guide](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/get-started)

## Tips
- azd works well with Bicep, ARM templates, and other Azure IaC tools.
- You can use azd to set up CI/CD pipelines and manage secrets.
- azd is designed for rapid, repeatable, and secure cloud-native development on Azure.

---

If you need a hands-on walkthrough or have specific questions about azd, just ask!
