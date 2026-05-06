from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.get("/preferences")
async def get_preferences(user=Depends(get_current_user)):
    pass

@router.patch("/preferences")
async def update_preferences(user=Depends(get_current_user)):
    pass

@router.get("/history")
async def notification_history(user=Depends(get_current_user)):
    """Return last 30 days of notifications."""
    pass
