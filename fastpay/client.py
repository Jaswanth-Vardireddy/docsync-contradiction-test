"""FastPay Client SDK implementation."""
from __future__ import annotations
import os


class FastPayGateway:
    """The main payment gateway connection class (renamed from PaymentClient)."""

    def __init__(self, api_key: str, timeout: int = 30, environment: str = "production"):
        """Initialize gateway connection.
        
        Args:
            api_key: FastPay authentication key.
            timeout: Request timeout in seconds.
            environment: 'production' or 'sandbox'. (renamed from sandbox_mode boolean)
        """
        self.api_key = api_key
        self.timeout = timeout
        self.environment = environment

    def charge(self, amount_cents: int, currency: str = "USD", customer: str = "") -> dict:
        """Create a charge (renamed from create_charge, amount renamed to amount_cents)."""
        return {"status": "succeeded", "amount": amount_cents}

    def check_status(self, transaction_id: str) -> dict:
        """Verify transaction status (renamed from verify_transaction)."""
        return {"status": "completed", "id": transaction_id}


def get_environment_config() -> dict:
    """Load configuration from environment."""
    return {
        "api_key": os.getenv("FASTPAY_API_KEY"),
        "timeout": int(os.getenv("FASTPAY_TIMEOUT", "30")),
        "webhook_secret": os.getenv("FASTPAY_WEBHOOK_SECRET"),
    }
