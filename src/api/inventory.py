from fastapi import APIRouter, Depends
from src.core.security import require_admin

router = APIRouter(prefix="/admin/inventory", tags=["inventory"])

@router.get("/")
async def list_inventory(admin=Depends(require_admin)):
    pass

@router.patch("/{variant_id}")
async def update_stock(variant_id: str, admin=Depends(require_admin)):
    pass

@router.get("/low-stock")
async def low_stock_report(admin=Depends(require_admin)):
    """Return variants with stock below threshold."""
    pass
