from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("/")
async def get_cart(user=Depends(get_current_user)):
    """Return current user's cart contents."""
    pass

@router.post("/items")
async def add_to_cart(user=Depends(get_current_user)):
    """Add a product variant to the cart."""
    pass

@router.patch("/items/{item_id}")
async def update_quantity(item_id: str, user=Depends(get_current_user)):
    """Update cart item quantity."""
    pass

@router.delete("/items/{item_id}")
async def remove_from_cart(item_id: str, user=Depends(get_current_user)):
    """Remove an item from the cart."""
    pass

@router.delete("/")
async def clear_cart(user=Depends(get_current_user)):
    """Clear all items from the cart."""
    pass
