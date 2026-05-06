from fastapi import APIRouter, Depends
from src.core.admin_security import require_permission

router = APIRouter(prefix="/admin/promo-codes", tags=["promotions"])

@router.get("/")
async def list_promo_codes(admin=Depends(require_permission("products:read"))):
    pass

@router.post("/")
async def create_promo_code(admin=Depends(require_permission("products:write"))):
    pass

@router.patch("/{code_id}/toggle")
async def toggle_code(code_id: str, admin=Depends(require_permission("products:write"))):
    pass

@router.post("/bulk-generate")
async def bulk_generate(admin=Depends(require_permission("products:write"))):
    """Generate N unique single-use codes for a campaign."""
    pass
