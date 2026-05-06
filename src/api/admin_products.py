from fastapi import APIRouter, Depends
from src.core.admin_security import require_permission

router = APIRouter(prefix="/admin/products", tags=["admin"])

@router.get("/")
async def list_products(admin=Depends(require_permission("products:read"))):
    pass

@router.post("/")
async def create_product(admin=Depends(require_permission("products:write"))):
    pass

@router.put("/{product_id}")
async def update_product(product_id: str, admin=Depends(require_permission("products:write"))):
    pass

@router.delete("/{product_id}")
async def archive_product(product_id: str, admin=Depends(require_permission("products:write"))):
    """Soft-delete (archive) product — never hard-delete."""
    pass
