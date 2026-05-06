from fastapi import APIRouter, Depends, BackgroundTasks
from src.core.security import get_current_user

router = APIRouter(prefix="/profile", tags=["profile"])

@router.post("/delete")
async def request_account_deletion(
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user),
):
    """Schedule account deletion after 30-day grace period."""
    background_tasks.add_task(schedule_deletion, user.id)
    return {"scheduled_at": "...", "effective_at": "..."}

@router.post("/export")
async def export_data(user=Depends(get_current_user)):
    """Generate GDPR data export and email download link."""
    pass
