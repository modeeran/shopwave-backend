from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/auth/mfa", tags=["mfa"])

@router.post("/enable")
async def enable_mfa(user=Depends(get_current_user)):
    """Generate TOTP secret, return QR code URI."""
    pass

@router.post("/verify")
async def verify_mfa(user=Depends(get_current_user)):
    """Verify TOTP code to confirm MFA setup."""
    pass

@router.post("/disable")
async def disable_mfa(user=Depends(get_current_user)):
    """Disable MFA — requires current TOTP code."""
    pass
