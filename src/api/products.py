from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(24, ge=1, le=100),
    category: Optional[str] = None,
    sort: str = Query("newest", enum=["newest", "price_asc", "price_desc", "popular"]),
):
    """Paginated product catalogue with optional category filter."""
    pass

@router.get("/{slug}")
async def get_product(slug: str):
    """Get product detail by URL slug."""
    pass
