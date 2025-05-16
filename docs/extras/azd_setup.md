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
winget install Microsoft.Azure.DevCLI
```
Or follow the official instructions:  
https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd

## Basic Workflow
1. **Initialize a project**
   ```pwsh
   azd init
   ```
2. **Provision Azure resources**
   ```pwsh
   azd provision
   ```
3. **Deploy your app**
   ```pwsh
   azd deploy
   ```
4. **Manage environments**
   ```pwsh
   azd env list
   azd env select <env-name>
   ```

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
