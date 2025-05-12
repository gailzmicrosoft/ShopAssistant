# User/auth endpoints

from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user():
    """Register a new user."""
    return {"user": "registered"}
