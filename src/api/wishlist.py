from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

@router.get("/")
async def get_wishlist(user=Depends(get_current_user)):
    pass

@router.post("/{product_id}")
async def add_to_wishlist(product_id: str, user=Depends(get_current_user)):
    pass

@router.delete("/{product_id}")
async def remove_from_wishlist(product_id: str, user=Depends(get_current_user)):
    pass

@router.post("/{product_id}/move-to-cart")
async def move_to_cart(product_id: str, user=Depends(get_current_user)):
    pass
