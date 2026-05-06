from fastapi import APIRouter, Depends, UploadFile, File
from src.core.security import get_current_user

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/")
async def get_profile(user=Depends(get_current_user)):
    pass

@router.patch("/")
async def update_profile(user=Depends(get_current_user)):
    pass

@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...), user=Depends(get_current_user)):
    """Upload avatar image; resize to 256x256 and store in S3."""
    pass
