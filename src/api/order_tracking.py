from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/orders/{order_id}/tracking", tags=["tracking"])

@router.get("/")
async def get_tracking(order_id: str, user=Depends(get_current_user)):
    """Return tracking events and estimated delivery date."""
    pass

@router.post("/webhook")
async def carrier_webhook():
    """Receive shipping carrier status updates."""
    pass
