# Offers/recommendations endpoints

from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def get_offers():
    """Get personalized offers."""
    return {"offers": []}
