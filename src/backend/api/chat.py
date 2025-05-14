from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.agents.sk_orchestrator import SemanticKernelOrchestrator
from app.core.security import get_current_user

router = APIRouter()
sk_orchestrator = SemanticKernelOrchestrator()

class ChatMessageRequest(BaseModel):
    message: str
    context: dict = {}

class ChatMessageResponse(BaseModel):
    response: str
    actions: list = []
    context: dict = {}

@router.post("/message", response_model=ChatMessageResponse)
def chat_message(request: ChatMessageRequest, user=Depends(get_current_user)):
    """Entry point for all user chat/messages. Passes input to Semantic Kernel orchestrator."""
    result = sk_orchestrator.handle_message(
        user_id=user["sub"],
        message=request.message,
        context=request.context
    )
    return ChatMessageResponse(**result)
