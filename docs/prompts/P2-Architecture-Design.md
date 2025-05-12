## GitHub Copilot Agent Mode - Prompt 2:   Architecture Design

**Agent**: Would you like a suggested architecture, database schema, or a breakdown of the next steps for any of these prioritized features?

**Prompt**: Yes, I need to add that I'd like to use Azure PostgreSQL DB as data layer, use Azure Key Vault to store sensitive information such as End Points, Keys, etc. I'd like to use Python as application programming language, and use FastAPI framework for the API App. I'd like to use Azure AI technology where appropriate.

**Additional Input**: 

I will choose Azure Container Apps over App Services. Can you revise? 

Can we leverage current azure AI services to make this Shopping Assistant smarter? We could use things like Semantic Kernel for coordination of advanced AI services, maybe we could use a few Agents?


**Agent**: A new section has been added to your architecture document detailing how to leverage Azure AI services—including OpenAI, Cognitive Search, Language, Vision, and Semantic Kernel—for a smarter, more adaptive Shopping Assistant. It also outlines how to use agents for modular, advanced AI-driven features.

Would you like a concrete example of how to integrate Semantic Kernel and Azure OpenAI in your FastAPI backend, or a sample agent design next?

**Prompts**: This is great. For Front End web UI, lets use React. Also I'd just use text input at this time, lets not use Azure VISION APIs at this time. I really like the 5. Semantic Kernel & AI Orchestration idea. Can you revise? 


**Agent**: The architecture has been revised to specify React for the frontend web UI, clarify that only text input will be used (no Azure Vision APIs for now), and retain the Semantic Kernel & AI Orchestration approach as a key feature.


**Additional Input**: Asked Agent to simplify the Semantic Kernel portion to make it only two agents to reduce the overhead. In addition, asked Agent to remvove sections that having contents no longer used. 

We need to add some logic that Semantic Kernel will be integrated with FAST API framework for 1. High-Level Architecture


Would you like a sample Semantic Kernel agent design, FastAPI backend scaffold, or a suggested database schema next?


---

## Suggested Architecture for Shopping Assistant (Quick Experiment)

### 1. High-Level Architecture
- **Frontend**: React web UI with a conversational chatbot interface for all user interactions (text input only for this version).
- **Backend API**: Python (FastAPI) RESTful API to handle business logic, product search, recommendations, cart, orders, etc.
- **Database**: Azure PostgreSQL Server
  - Separate DB/schema for authentication (user credentials, roles)
  - Main DB for products, orders, chat history, user preferences, wish list, etc.
- **Authentication**: Use secure password hashing, parameterized queries, and managed identity for DB access. Never hardcode credentials; use Azure Key Vault for secrets and sensitive configuration (endpoints, keys, etc.).
- **Payment Gateway**: Mock API endpoint for payment processing (no real transactions).
- **Azure Hosting**: Use Azure Container Apps for backend/frontend deployment. Use Managed Identity for secure resource access.
- **Azure AI Integration**: Leverage Azure AI services (e.g., Azure OpenAI, Cognitive Search) for product recommendations, chatbot intelligence, or other smart features where appropriate. 
- **Semantic Kernel Orchestration**: Integrate Semantic Kernel with the FastAPI backend to coordinate AI skills and agents. Semantic Kernel will be invoked from FastAPI endpoints to enable advanced conversational flows, product recommendations, and personalized offers through modular orchestration of Azure AI services.

### Integration of Semantic Kernel Agents with FastAPI

The integration of Semantic Kernel agents with FastAPI is central to enabling advanced conversational and AI-driven features in the Shopping Assistant. Here’s how the integration works:

- **Agent Implementation**: Three main agents are implemented as Python classes or modules:
  - **Shopping Cart Management Agent**: Handles all cart-related actions, such as adding, removing, and updating items in the cart, as well as managing the current cart state for the user.
  - **Order Management Agent**: Manages order placement, order confirmation, payment processing (mock), and order tracking. This agent is responsible for finalizing the cart into an order and handling post-order actions.
  - **Personalization Agent**: Provides product recommendations and personalized offers to users based on their preferences, history, and context.
  These agents encapsulate business logic and orchestrate calls to Azure OpenAI, Cognitive Search, and other AI services via Semantic Kernel.

- **FastAPI Endpoints**: FastAPI endpoints (routes) are defined for user actions such as chat, cart updates, order placement, and offers. When a request is received, the endpoint invokes the appropriate agent, passing user input and context.

- **Semantic Kernel Orchestration**: Within each agent, Semantic Kernel is used to coordinate AI skills—such as intent recognition, product recommendation, or personalized offers—by composing prompts and managing responses from Azure AI services.

- **Response Flow**: The agent processes the AI responses, applies business rules, and returns a structured result to the FastAPI endpoint, which then sends the response to the frontend (e.g., chatbot UI).

**Example Flow:**
1. User sends a chat message: “Add two bags of coffee to my cart.”
2. FastAPI chat endpoint receives the message and calls the Shopping Cart Management Agent.
3. The agent uses Semantic Kernel to interpret the intent and update the cart in the database.
4. The agent returns a confirmation message, which the endpoint sends back to the frontend.

This modular approach keeps business logic, AI orchestration, and HTTP handling cleanly separated, making the system maintainable and extensible.

### 2. Security & Best Practices
- Use parameterized queries and proper indexing in PostgreSQL.
- Encrypt sensitive data at rest and in transit.
- Store all secrets and sensitive info in Azure Key Vault.
- Use RBAC for resource access and least privilege for DB accounts.
- Enable logging and monitoring (App Insights, Azure Monitor).
- Implement error handling and input validation throughout.
- Use managed identity for secure service-to-service communication.

### 3. Key Components Breakdown
- **Product Search**: FastAPI endpoint to query products table with filters.
- **Recommendations**: FastAPI endpoint to suggest products (simple logic or Azure AI-powered in future).
- **Cart Management**: FastAPI endpoints for add/remove/update cart items (per user).
- **User Auth**: Registration, login, JWT/session management, password reset (using separate auth DB/schema).
- **Order Placement**: FastAPI endpoint to create orders, chatbot triggers confirmation.
- **Order Tracking**: FastAPI endpoint to fetch order status/history.
- **Wishlist**: FastAPI endpoint to manage user favorites.
- **Chatbot UI**: Web component for chat, connects to backend for all actions (optionally powered by Azure OpenAI or Bot Service).
- **Personalized Offers**: FastAPI endpoint to fetch/apply offers based on user profile and AI insights.

### 4. Next Steps
1. Define database schema (tables for users, products, orders, cart, chat, etc.).
2. Scaffold FastAPI backend with endpoints for each feature.
3. Set up authentication and RBAC.
4. Build frontend with chatbot UI and connect to backend.
5. Implement mock payment API.
6. Integrate Azure AI services where appropriate.
7. Integrate Semantic Kernel with FastAPI backend to enable agent-based orchestration of AI skills (recommendations, order management, personalization).
8. Add logging, error handling, and security controls.

---

## Leveraging Azure AI Services for a Smarter Shopping Assistant

To make the Shopping Assistant more intelligent and adaptive, you can integrate the following Azure AI services and technologies:

### 1. Azure OpenAI Service
- Use GPT models for natural language understanding, product Q&A, and conversational UI.
- Enable the assistant to interpret user intent, summarize product details, and provide personalized recommendations.

### 2. Azure AI Search (Cognitive Search)
- Power semantic product search and ranking using vector search and semantic capabilities.
- Index product catalog and enable users to search using natural language queries.

### 3. Semantic Kernel & AI Orchestration
- Use Semantic Kernel to coordinate multiple AI skills and services (e.g., OpenAI, Search).
- Build three main agents for clarity and maintainability:
  - **Shopping Cart Management Agent**: Handles all cart-related actions, such as adding, removing, and updating items in the cart, as well as managing the current cart state for the user.
  - **Order Management Agent**: Manages order placement, order confirmation, payment processing (mock), and order tracking. This agent is responsible for finalizing the cart into an order and handling post-order actions.
  - **Personalization Agent**: Provides product recommendations and personalized offers to users based on their preferences, history, and context.
- Agents collaborate to fulfill complex user requests, improving flexibility and user experience while minimizing overhead.

### 4. Azure AI Studio & Prompt Flow
- Use Azure AI Studio to design, test, and deploy prompt flows for advanced conversational experiences.

### 5. Responsible AI & Security
- Use content moderation, logging, and monitoring to ensure safe and responsible AI usage.
- Store all AI endpoints, keys, and configs in Azure Key Vault.

---

**Summary:**
By integrating Azure OpenAI, Cognitive Search, and orchestrating them with Semantic Kernel and custom agents, your Shopping Assistant delivers advanced, context-aware, and highly personalized shopping experiences. This modular approach is future-proof, allowing you to add or update AI skills as needed.

---

This architecture is designed for rapid prototyping, security, and easy future expansion. It uses Azure PostgreSQL for data, Azure Key Vault for secrets, Python/FastAPI for the backend, Azure Container Apps for hosting, and Azure AI for intelligent features, following Azure best practices.
