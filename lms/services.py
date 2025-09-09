import os

import stripe

from lms.models import Subscription
from lms.tasks import send_email
from users.models import User

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


def email_on_course_update(course):
    subscriptions = Subscription.objects.filter(course=course.id)
    user_ids = list(map(lambda x: x["user"], subscriptions))
    recipients = list(map(lambda x: x.email, User.objects.filter(id__in=user_ids)))
    send_email.delay(recipients, f'Course "{course.name}" updated', f"{course.name}\n{course.desc}")
