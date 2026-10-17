# FastPay SDK

A Python client library for payment processing.

## Installation

```bash
pip install fastpay-client
```

## Quickstart

```python
from fastpay import PaymentClient

# Initialize client
client = PaymentClient(api_key="sk_live_123", timeout=30, sandbox_mode=True)

# Process a charge
result = client.create_charge(amount=5000, currency="USD", customer_id="cust_999")

# Verify charge
client.verify_transaction(tx_id="tx_12345")
```

## Configuration

You can configure the client using environment variables:

- `FASTPAY_API_KEY`: Secret API key for authentication.
- `FASTPAY_TIMEOUT`: Connection timeout in seconds (default: 30).
- `FASTPAY_LEGACY_MODE`: Set to `true` to enable legacy XML responses.

See [API Reference](docs/api.md) for parameter details.