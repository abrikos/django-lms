from datetime import datetime, timezone

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import User


@shared_task
def block_inactive_users():
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login and (datetime.now(timezone.utc) - user.last_login).days > 30:
            user.is_active = False
            user.save()



@shared_task
def send_email(recipients: list, subj: str, message: str):
    send_mail(subj, message, settings.DEFAULT_FROM_EMAIL, recipients)
