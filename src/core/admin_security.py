from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

ROLES = {
    "super_admin": ["*"],
    "product_manager": ["products:read", "products:write", "inventory:read"],
    "order_manager": ["orders:read", "orders:write"],
    "analyst": ["analytics:read"],
}

async def require_admin(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload or payload.get("role") not in ROLES:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return payload

def require_permission(permission: str):
    async def _check(admin=Depends(require_admin)):
        role = admin.get("role")
        allowed = ROLES.get(role, [])
        if "*" not in allowed and permission not in allowed:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return admin
    return _check
