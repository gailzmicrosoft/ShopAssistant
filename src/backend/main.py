from fastapi import FastAPI
from app.api import chat

app = FastAPI(title="Shop Assistant API")

# Main entry point for all user interactions
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# Health check endpoint
define_health = lambda: {"status": "ok"}
app.get("/health")(define_health)

"""
Architecture Note:
- All user messages are sent to /chat/message.
- FastAPI passes the message to the Semantic Kernel orchestrator.
- SK classifies intent and routes to the correct agent/skill.
- This enables flexible, AI-driven routing and minimal API surface.
"""
