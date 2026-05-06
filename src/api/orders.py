from fastapi import APIRouter, Depends, Query
from src.core.security import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
async def list_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    user=Depends(get_current_user),
):
    """Paginated order history for the current user."""
    pass

@router.get("/{order_id}")
async def get_order(order_id: str, user=Depends(get_current_user)):
    """Get full order detail including items, shipping, and timeline."""
    pass
