## GitHub Copilot Agent Mode - Prompt 2:   Architecture Design

**Prompt**: I need to add that I'd like to use Azure PostgreSQL DB as data layer, use Azure Key Vault to store sensitive information such as End Points, Keys, etc. I'd like to use Python as application programming language, and use FastAPI framework for the API App. I'd like to use Azure AI technology where appropriate. I will choose Azure Container Apps over App Services. Can you revise? Can we leverage current Azure AI services to make this Shopping Assistant smarter? We could use things like Semantic Kernel for coordination of advanced AI services, maybe we could use a few Agents?

**Note**: Additional conversation can be found in [Architecture discussions](P2A-Architecture-Design-Framework-Discussions.md), before we decided on the current architecture. 

---

## Updated Architecture for Shopping Assistant 

### 1. High-Level Architecture
- **Frontend**: React web UI with a conversational chatbot interface for all user interactions (text input only for this version).
- **Backend API**: Python (FastAPI) with a minimal set of endpoints, primarily a single `/chat/message` endpoint for all user interactions.
- **Semantic Kernel Orchestration**: FastAPI passes all user messages to a Semantic Kernel (SK) orchestrator. SK classifies intent and dynamically routes to the appropriate agent/skill (e.g., cart, order, personalization).
- **Database**: Azure PostgreSQL Server
  - Separate tabble for authentication (user credentials, roles)
  - Main DB for products, orders, chat history, user preferences, wish list, etc.
- **Authentication**: Secure password hashing, parameterized queries, managed identity for DB access. All secrets and sensitive config in Azure Key Vault.
- **Payment Gateway**: Mock API endpoint for payment processing (no real transactions).
- **Azure Hosting**: Azure Container Apps for backend/frontend deployment. Managed Identity for secure resource access.
- **Azure AI Integration**: Leverage Azure AI services (e.g., Azure OpenAI, Cognitive Search) for product recommendations, chatbot intelligence, and other smart features.

### 2. Semantic Kernel Integration Pattern
- **Single Entry Point**: All user messages (chat, commands, etc.) are sent to `/chat/message`.
- **SK Orchestration**: FastAPI passes the message and context to the SK orchestrator.
- **Intent Classification & Routing**: SK uses LLMs and planners to classify the message and route to the correct agent/skill (e.g., ShoppingCartManagementAgent, OrderManagementAgent, PersonalizationAgent).
- **Agent Execution**: Agents encapsulate business logic and can call Azure OpenAI, Cognitive Search, and other services as needed.
- **Response Flow**: SK composes the response and returns it to FastAPI, which sends it to the frontend.

#### Example Flow
1. User sends a chat message: “Add two bags of coffee to my cart.”
2. FastAPI `/chat/message` endpoint receives the message and passes it to the SK orchestrator.
3. SK classifies the intent (add to cart) and routes to the ShoppingCartManagementAgent.
4. The agent updates the cart in the database and returns a confirmation message.
5. The response is sent back to the frontend.

### 3. Benefits of This Architecture
- **Natural User Experience**: Users interact in free-form language; SK handles mapping intent to actions.
- **Minimal API Surface**: Only a few endpoints (e.g., `/chat/message`, `/health`), not one for every operation.
- **Easy to Extend**: Add new skills/agents to SK without changing FastAPI routes.
- **Centralized Orchestration**: All business logic and AI reasoning live in SK, keeping FastAPI focused on HTTP and security.

### 4. Security & Best Practices
- Use parameterized queries and proper indexing in PostgreSQL.
- Encrypt sensitive data at rest and in transit.
- Store all secrets and sensitive info in Azure Key Vault.
- Use RBAC for resource access and least privilege for DB accounts.
- Enable logging and monitoring (App Insights, Azure Monitor).
- Implement error handling and input validation throughout.
- Use managed identity for secure service-to-service communication.

### 5. Key Components Breakdown
- **/chat/message**: Main FastAPI endpoint for all user input; passes messages to SK.
- **SK Orchestrator**: Classifies intent, routes to agents/skills, composes responses.
- **Agents/Skills**: Modular Python classes for cart management, order management, personalization, etc.
- **Azure AI Services**: Used by agents for LLM, search, and recommendations.
- **Database Layer**: SQLAlchemy models and direct SQL for persistence.

---

## Leveraging Azure AI Services for a Smarter Shopping Assistant

- **Azure OpenAI Service**: GPT models for natural language understanding, product Q&A, and conversational UI.
- **Azure AI Search (Cognitive Search)**: Semantic product search and ranking.
- **Semantic Kernel & AI Orchestration**: SK coordinates multiple AI skills and services, enabling flexible, context-aware, and highly personalized shopping experiences.
- **Responsible AI & Security**: Content moderation, logging, monitoring, and secure storage of all AI endpoints, keys, and configs in Azure Key Vault.

---

**Summary:**
This architecture uses a minimal FastAPI API surface, with Semantic Kernel as the dynamic orchestrator for all business logic and AI-driven flows. It is designed for rapid prototyping, security, and easy future expansion, leveraging Azure PostgreSQL, Key Vault, Container Apps, and Azure AI services.
