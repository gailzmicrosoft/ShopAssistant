# Order endpoints

from fastapi import APIRouter

router = APIRouter()

@router.post("/place")
def place_order():
    """Place a new order."""
    return {"order": "created"}
