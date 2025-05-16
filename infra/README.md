# Deployment Plan

The deployment code will be in **infra** folder. The **modules** subfolder contains reusable modules. There will be two main deployment files: `main.bicep` and `main.waf.bicep`, each having its own parameters, and both utilizing the code in the **modules** subfolder. 

The `main.bicep` is a lightweight deployment. It will be used as quick and economic deployment, for solution exploration, demonstration, customization, and decision making. Once it is decided to adopt the solution, you can redeploy the solution using `main.waf.bicep`. 

The `main.waf.bicep` will create one Virtual Network to host all the components, with subnets. It will deploy private end points for the solution resources and services utilized, for example, Azure AI Foundry, Azure Storage, Azure Cosmos DB, and Azure Key Vault. It will creates a Bastion Host. It will create all the networking and security resources recommended by WAF Security Guidelines. The deployment will leverage Azure Verified Modules where appropriate.  For more information, please refer to [Microsoft Azure Well-Architected Framework (WAF) Security design principles](https://learn.microsoft.com/en-us/azure/well-architected/security/principles) and [Azure Verified Modules (AVM)](https://azure.github.io/Azure-Verified-Modules/).

If you are new to AVM BICEP implementation, refer to [AVM Bicep Quickstart Guide](https://azure.github.io/Azure-Verified-Modules/usage/quickstart/bicep/).

Below table illustrates an example deployment design. The Group (module) Name column is to put all code in one BICEP module. 

| Component Name                    | Group (Module) Name | Subnet      |
| --------------------------------- | ------------------- | ----------- |
| Front End App Service             | App Services        | Application |
| Front End App Service Plan        | App Services        | Application |
| Application Insights              | Monitoring          | Application |
| Container Apps Environment        | Container App       | Application |
| Log Analytics Workspace           | Monitoring          | Application |
| Frontend Container App            | Container App       | Application |
| Backend Container App             | Container App       | Application |
| Managed Identity (Resource Group) | Identity            | Application |
| AI Hub                            | AI Foundry          | Services    |
| AI Project                        | AI Foundry          | Services    |
| AI Services                       | AI Foundry          | Services    |
| Key Vault                         | Key Vault           | Data        |
| Cosmos DB                         | Database            | Data        |
| Storage Account Front End         | Storage             | Data        |
| Storage Account Back End          | Storage             | Data        |
| Network Security Group            | Networking          | N/A         |
| Bastion Host                      | Networking          | N/A         |
| Route Table                       | Networking          | N/A         |
| Private Endpoints                 | Networking          | N/A         |
| Private DNS Zone                  | Networking          | N/A         |

## Deployment Considerations 

### Add Networking Components
- **Network Security Group (NSG):** Protects subnets and controls inbound/outbound traffic. One NSG per subnet is recommended.
- **Bastion Host:** Provides secure RDP/SSH access to VMs without exposing public IPs.
- **Route Table:** Custom route tables for advanced routing scenarios (optional, but recommended for segmented networks).
- **Private Endpoints:** For secure, private connectivity to PaaS services (Key Vault, Storage, Cosmos DB, etc.), consider adding private endpoints in the relevant subnets.
- **Private DNS Zone:** Required for name resolution of private endpoints, ensuring resources in your VNet can resolve the private DNS names of Azure PaaS services to their private IP addresses.

### Subnet Design (Recommended)
- **Application Subnet:** Hosts App Services, Container Apps, and supporting resources.
- **Services Subnet:** Hosts AI Foundry and related services.
- **Data Subnet:** Hosts Key Vault, Cosmos DB, Storage, and other data services.

### Security & Best Practices
- Use Managed Identity for all services that support it.
- Store secrets and connection strings in Key Vault; never hardcode credentials.
- Enable diagnostic logging for all resources (send to Log Analytics Workspace).
- Apply NSGs to each subnet with least-privilege rules.
- Use Bastion Host for secure admin access.
- Consider DDoS Protection for the VNet if required.
- Use Private Endpoints for PaaS services to avoid public exposure.

### Bicep Module Structure (Suggested)
- **modules/networking.bicep:** VNet, subnets, NSGs, Bastion, route tables, private endpoints
- **modules/app-services.bicep:** App Service, App Service Plan
- **modules/container-app.bicep:** Container Apps Environment, frontend/backend apps
- **modules/monitoring.bicep:** Application Insights, Log Analytics
- **modules/identity.bicep:** Managed Identity
- **modules/ai-foundry.bicep:** AI Hub, AI Project, AI Services
- **modules/keyvault.bicep:** Key Vault
- **modules/database.bicep:** Cosmos DB
- **modules/storage.bicep:** Storage Accounts

