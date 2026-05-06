from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/auth/sessions", tags=["sessions"])

@router.get("/")
async def list_sessions(user=Depends(get_current_user)):
    """List all active sessions (device, IP, last seen)."""
    pass

@router.delete("/{session_id}")
async def revoke_session(session_id: str, user=Depends(get_current_user)):
    """Revoke a specific session by ID."""
    pass

@router.delete("/")
async def revoke_all_sessions(user=Depends(get_current_user)):
    """Revoke all sessions except current."""
    pass
