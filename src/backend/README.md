# ShopAssistant Backend (FastAPI + Semantic Kernel)

This folder contains the backend API for the ShopAssistant project, built with FastAPI and designed for integration with Semantic Kernel (SK) and Azure services. The backend provides secure authentication, business logic, and AI-powered orchestration for the frontend React app.

---

## 🚀 Quick Start: Running the FastAPI Backend

1. **Set up Python environment**
   - Install Python 3.9 or newer from [python.org](https://www.python.org/downloads/).
   - (Recommended) Create a virtual environment:
     ```pwsh
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

2. **Install dependencies**
   - In this `backend` folder, run:
     ```pwsh
     pip install -r ../../requirements.txt
     ```

3. **Set environment variables**
   - Configure your database, Azure, and secret settings in a `.env` file or via environment variables. See `core/config.py` for details.

4. **Create the database tables**
   - Run the SQL in `db/create_tables.sql` against your PostgreSQL database.

5. **Start the FastAPI server**
   - Run:
     ```pwsh
     uvicorn main:app --reload
     ```
   - The API will be available at [http://localhost:8000](http://localhost:8000)

---

## 📝 Project Structure

- `main.py` — FastAPI entry point, includes all routers.
- `api/` — Route definitions for chat, user, order, cart, offers, etc.
- `agents/` — Semantic Kernel agents/skills for cart, order, personalization, and orchestration.
- `db/` — SQLAlchemy models, Pydantic schemas, CRUD logic, and SQL scripts.
- `core/` — Configuration, security, and logging utilities.
- `services/` — Azure OpenAI, Cognitive Search, and Key Vault integration stubs.

---

## 🔑 Key Backend Concepts

- **FastAPI**: Modern, async Python web framework for building APIs.
- **Semantic Kernel (SK)**: Orchestrates AI skills/agents for intent classification and dynamic routing.
- **JWT Authentication**: Secure token-based authentication for all API requests.
- **SQLAlchemy**: ORM for database models and queries.
- **Pydantic**: Data validation and serialization for API requests/responses.
- **Azure Integration**: Stubs for OpenAI, Cognitive Search, and Key Vault.

**Learn more:**
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

## ⚙️ Development Tips
- Use `uvicorn main:app --reload` for hot-reloading during development.
- Test endpoints with [http://localhost:8000/docs](http://localhost:8000/docs) (FastAPI’s interactive Swagger UI).
- Update `.env` or environment variables for secrets and connection strings.
- Use the `db/create_tables.sql` script to initialize or reset your database schema.

---

## 📚 More Resources
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Azure for Python Developers](https://learn.microsoft.com/en-us/azure/developer/python/)
- [Semantic Kernel Samples](https://github.com/microsoft/semantic-kernel)

---

Happy coding! If you have questions, check the docs above or ask for help.
