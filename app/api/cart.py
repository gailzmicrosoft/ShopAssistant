from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_cart_items():
    """Get all items in the shopping cart."""
    return {"cart": []}

# Cart endpoints
