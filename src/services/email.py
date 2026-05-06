import httpx
from src.core.config import settings

async def send_verification_email(to: str, token: str) -> None:
    """Send account verification email via SendGrid."""
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://api.sendgrid.com/v3/mail/send",
            headers={"Authorization": f"Bearer {settings.sendgrid_api_key}"},
            json={
                "to": [{"email": to}],
                "from": {"email": "noreply@shopwave.io"},
                "subject": "Verify your ShopWave account",
                "content": [{"type": "text/plain", "value": f"Token: {token}"}],
            },
        )

async def send_order_confirmation(to: str, order_id: str) -> None:
    """Send order confirmation email."""
    pass
