from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/change-password")
async def change_password(user=Depends(get_current_user)):
    """Change password — requires current password confirmation."""
    pass

@router.post("/forgot-password")
async def forgot_password():
    """Send password reset link to email."""
    pass

@router.post("/reset-password")
async def reset_password():
    """Reset password using token from email."""
    pass
