from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/checkout", tags=["checkout"])

@router.post("/")
async def initiate_checkout(user=Depends(get_current_user)):
    """Start checkout session, return available shipping options."""
    pass

@router.post("/confirm")
async def confirm_order(user=Depends(get_current_user)):
    """Confirm order after payment intent created."""
    pass
