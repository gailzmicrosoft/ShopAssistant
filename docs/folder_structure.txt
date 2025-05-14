ShopAssistant/
│
├── docs/
│   └── ... (architecture, prompts, scenarios, images, etc.)
│
└── src/
    ├── frontend/
    │   ├── App.jsx
    │   ├── ShopAssistant.jsx
    │   ├── SignInRegister.jsx
    │   └── README.md
    │
    └── backend/
        ├── main.py
        ├── README.md
        ├── agents/
        │   ├── __init__.py
        │   ├── cart_agent.py
        │   ├── order_agent.py
        │   ├── personalization_agent.py
        │   └── sk_orchestrator.py
        ├── api/
        │   ├── __init__.py
        │   ├── cart.py
        │   ├── chat.py
        │   ├── offers.py
        │   ├── order.py
        │   └── user.py
        ├── core/
        │   ├── __init__.py
        │   ├── config.py
        │   ├── logging.py
        │   └── security.py
        ├── db/
        │   ├── __init__.py
        │   ├── create_tables.sql
        │   ├── crud.py
        │   ├── models.py
        │   └── schemas.py
        ├── services/
        │   ├── __init__.py
        │   ├── keyvault_service.py
        │   ├── openai_service.py
        │   └── search_service.py
        └── tests/