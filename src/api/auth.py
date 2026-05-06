from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.security import create_access_token, verify_password
from src.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(db: AsyncSession = Depends(get_db)):
    """Register a new customer account."""
    pass

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_db)):
    """Authenticate and return JWT access + refresh tokens."""
    pass

@router.post("/refresh")
async def refresh_token():
    """Rotate refresh token and return new access token."""
    pass

@router.post("/logout")
async def logout():
    """Revoke refresh token."""
    pass
