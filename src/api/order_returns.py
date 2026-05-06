from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/orders", tags=["returns"])

@router.post("/{order_id}/cancel")
async def cancel_order(order_id: str, user=Depends(get_current_user)):
    """Cancel order if still in cancellable state; refund via Stripe."""
    pass

@router.post("/{order_id}/return")
async def request_return(order_id: str, user=Depends(get_current_user)):
    """Initiate return request for delivered orders."""
    pass
