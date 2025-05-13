## GitHub Copilot Agent Mode - Prompt 4:   Scaffolding Code Generation 

**Prompt**: I bet you are eager to generate code! Lets go! Use the file structure, all the documents we created in prompts folder. Let me know if you need additional information.

**Agent**: Great! I’m ready to start scaffolding your backend FastAPI application using the file structure and architecture you’ve defined. Here’s the plan for the initial code generation:

1. Create a minimal FastAPI app in main.py that includes routers for each API module.
2. Scaffold the API route files (cart.py, order.py, user.py, offers.py, chat.py) with basic route definitions.
3. Set up the agents directory with class stubs for each agent.
4. Scaffold the db directory with SQLAlchemy models, Pydantic schemas, and CRUD stubs.
5. Add service stubs for Azure OpenAI, Cognitive Search, and Key Vault.
6. Add config, security, and logging utilities in core.

The initial FastAPI app scaffolding and API route files have been created with basic routers and sample endpoints. However, it appears that **FastAPI** is not yet installed in your environment, which is causing import errors.

Next steps:

1. Install FastAPI and Uvicorn (for running the app) in your Python environment.
2. Continue scaffolding the agents, database models, and service stubs.

Would you like me to install the required Python packages for you before proceeding?

**Prompt**: Lets continue with 2, Continue scaffolding the agents, database models, and service stubs. I will install FastAPI and Uvicorn later. And plese give me instructions for them. 

**Agent**: The agents, database models, Pydantic schemas, CRUD stubs, and service stubs for Azure OpenAI, Cognitive Search, and Key Vault have all been scaffolded. Core utilities for config, security, and logging are also in place.

To run your FastAPI app, you will need to install the following packages:

- fastapi
- uvicorn
- sqlalchemy
- pydantic
- passlib[bcrypt]

You can install them with:

`pip install fastapi uvicorn sqlalchemy pydantic "passlib[bcrypt]"`

Also need these packages: 

`pip install python-dotenv azure-identity azure-keyvault-secrets requests`

Let me know if you want to scaffold the frontend, add more backend features, or need help with anything else!

**Prompt**: I reviewed the code in app/db folder. Looks like we are missing some key tables and attributes. For example I need a customer table, without it, how can we recommend products. 

**Agent**: Good observations! Yes you are right. Added customer table. 

**Additional Prompt Input**: Worked with Agent on specific attributes. 

**Prompt**: Can you create the requirements.txt file for this app?

**Agent** created it with instructions:

`pip install -r requirements.txt`

After installation, did this 

`pip show fastapi uvicorn sqlalchemy pydantic passlib` 

`pip show python-dotenv azure-identity azure-keyvault-secrets requests`   

And noted the versions in requirements.txt 

