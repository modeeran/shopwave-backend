from fastapi import APIRouter, Depends, Query
from src.core.admin_security import require_permission

router = APIRouter(prefix="/admin/users", tags=["admin"])

@router.get("/")
async def search_users(
    q: str | None = None,
    page: int = Query(1, ge=1),
    admin=Depends(require_permission("users:read")),
):
    pass

@router.get("/{user_id}")
async def get_user_detail(user_id: str, admin=Depends(require_permission("users:read"))):
    pass

@router.patch("/{user_id}/status")
async def update_user_status(user_id: str, admin=Depends(require_permission("users:write"))):
    """Suspend or reinstate a user account."""
    pass
