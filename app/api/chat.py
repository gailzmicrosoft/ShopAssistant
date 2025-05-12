from fastapi import APIRouter

router = APIRouter()

@router.post("/message")
def chat_message():
    """Handle a chat message from the user."""
    return {"response": "Hello! How can I help you?"}

# Chatbot endpoints
