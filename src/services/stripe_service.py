import stripe
from src.core.config import settings

stripe.api_key = settings.stripe_secret_key

async def create_payment_intent(amount_pence: int, currency: str = "gbp",
                                 metadata: dict | None = None) -> dict:
    """Create a Stripe PaymentIntent for the given amount."""
    intent = stripe.PaymentIntent.create(
        amount=amount_pence,
        currency=currency,
        automatic_payment_methods={"enabled": True},
        metadata=metadata or {},
    )
    return {"client_secret": intent.client_secret, "payment_intent_id": intent.id}

async def handle_webhook(payload: bytes, sig_header: str) -> dict:
    """Process Stripe webhook events."""
    event = stripe.Webhook.construct_event(payload, sig_header, settings.stripe_webhook_secret)
    if event["type"] == "payment_intent.succeeded":
        pass  # fulfil order
    elif event["type"] == "payment_intent.payment_failed":
        pass  # notify user
    return {"received": True}
