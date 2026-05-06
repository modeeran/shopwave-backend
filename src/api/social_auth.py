from fastapi import APIRouter

router = APIRouter(prefix="/auth/social", tags=["auth"])

@router.get("/google/callback")
async def google_callback(code: str, state: str):
    """Handle Google OAuth2 callback, exchange code for tokens."""
    pass

@router.post("/apple/callback")
async def apple_callback():
    """Handle Sign in with Apple token validation."""
    pass
