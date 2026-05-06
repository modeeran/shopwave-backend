from fastapi import APIRouter, Depends, Query
from src.core.admin_security import require_permission

router = APIRouter(prefix="/admin/orders", tags=["admin"])

@router.get("/")
async def list_orders(
    status: str | None = None,
    page: int = Query(1, ge=1),
    admin=Depends(require_permission("orders:read")),
):
    pass

@router.patch("/{order_id}/status")
async def update_order_status(order_id: str, admin=Depends(require_permission("orders:write"))):
    """Update order status and trigger notifications."""
    pass

@router.post("/{order_id}/refund")
async def issue_refund(order_id: str, admin=Depends(require_permission("orders:write"))):
    pass
