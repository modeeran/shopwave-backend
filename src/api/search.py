from fastapi import APIRouter, Query
from sqlalchemy import text
from src.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/")
async def search_products(
    q: str = Query(..., min_length=1, max_length=200),
    page: int = Query(1, ge=1),
    limit: int = Query(24, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """Full-text search using PostgreSQL tsvector."""
    query = text(
        """SELECT * FROM products
           WHERE search_vector @@ plainto_tsquery(:q)
           ORDER BY ts_rank(search_vector, plainto_tsquery(:q)) DESC
           LIMIT :limit OFFSET :offset"""
    )
    result = await db.execute(query, {"q": q, "limit": limit, "offset": (page - 1) * limit})
    return result.mappings().all()
