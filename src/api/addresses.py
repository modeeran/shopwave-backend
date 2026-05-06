from fastapi import APIRouter, Depends
from src.core.security import get_current_user

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("/")
async def list_addresses(user=Depends(get_current_user)):
    pass

@router.post("/")
async def add_address(user=Depends(get_current_user)):
    pass

@router.put("/{address_id}")
async def update_address(address_id: str, user=Depends(get_current_user)):
    pass

@router.delete("/{address_id}")
async def delete_address(address_id: str, user=Depends(get_current_user)):
    pass

@router.patch("/{address_id}/default")
async def set_default(address_id: str, user=Depends(get_current_user)):
    pass
