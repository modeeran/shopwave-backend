from fastapi import APIRouter, Depends, Query
from src.core.security import get_current_user

router = APIRouter(prefix="/products/{product_id}/reviews", tags=["reviews"])

@router.get("/")
async def list_reviews(product_id: str, page: int = Query(1, ge=1)):
    pass

@router.post("/")
async def submit_review(product_id: str, user=Depends(get_current_user)):
    """Submit review — only allowed if user has purchased the product."""
    pass

@router.post("/{review_id}/helpful")
async def mark_helpful(product_id: str, review_id: str, user=Depends(get_current_user)):
    pass
