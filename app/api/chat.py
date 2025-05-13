from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.agents.sk_orchestrator import SemanticKernelOrchestrator

router = APIRouter()
sk_orchestrator = SemanticKernelOrchestrator()

class ChatMessageRequest(BaseModel):
    user_id: int
    message: str
    context: dict = {}

class ChatMessageResponse(BaseModel):
    response: str
    actions: list = []
    context: dict = {}

@router.post("/message", response_model=ChatMessageResponse)
def chat_message(request: ChatMessageRequest):
    """Entry point for all user chat/messages. Passes input to Semantic Kernel orchestrator."""
    result = sk_orchestrator.handle_message(
        user_id=request.user_id,
        message=request.message,
        context=request.context
    )
    return ChatMessageResponse(**result)
