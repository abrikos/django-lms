import os

import stripe

stripe.api_key = os.getenv("STRIPE_API")


def stripe_create_product(name: str):
    """Create stripe product"""
    return stripe.Product.create(name=name)


def stripe_create_payment(name: str, amount: int):
    """Create stripe payment"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount,
        recurring={"interval": "month"},
        product_data={"name": name},
    )


def stripe_get_session(price_id: str, success_url):
    """Get payment session"""
    return stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[{"price": price_id, "quantity": 1}],
        mode="subscription",
    )


def stripe_check_payment(session_id: str):
    session = stripe.checkout.Session.retrieve(session_id)
    return session.payment_status
