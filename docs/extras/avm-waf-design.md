The code modernization SA is in published to GitHub. It has a quick deploy capability, with code in infra folder. 

We need to make a new version of it. For quick experiment, we will put the new code in a separate folder named **infra-avm**. The goal is, in the infra-avm folder which will eventually replace the infra folder, create a main.bicep that deploys the solution similar to current code in infra folder, with a main.waf.bicep that will deploy a waf-aligned version using azure verified modules (BICEP). Mainly it will need to create one Virtual Network to host all the components, with three subnets. Both main.bicep and main.waf.bicep will use same code base in modules folder. Each will have its own parameters set. 

Details illustrated in below table. The Group (module) Name column is to put all code in one BICEP module. 

| Component Name                    | Group (Module) Name   | Subnet      |
| --------------------------------- | --------------------- | ----------- |
| Front End App Service             | App Services          | Application |
| Front End App Service Plan        | App Services          | Application |
| Application Insights              | Monitoring            | Application |
| Container Apps Environment        | Container App         | Application |
| Log Analytics Workspace           | Monitoring            | Application |
| Frontend Container App            | Container App         | Application |
| Backend Container App             | Container App         | Application |
| Managed Identity (Resource Group) | Identity              | Application |
| AI Hub                            | AI Foundry            | Services    |
| AI Project                        | AI Foundry            | Services    |
| AI Services                       | AI Foundry            | Services    |
| Key Vault                         | Key Vault             | Data        |
| Cosmos DB                         | Database              | Data        |
| Storage Account Front End         | Storage               | Data        |
| Storage Account Back End          | Storage               | Data        |
| Network Security Group            | Networking            | N/A         |
| Bastion Host                      | Networking            | N/A         |
| Route Table                       | Networking            | N/A         |
| Private Endpoints (if needed)     | Networking            | N/A         |
| Private DNS Zone                  | Networking            | N/A         |

## Addtional Considerations 

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

