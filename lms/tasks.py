from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def my_task():
    print('zzzzzz222')
    # Код задачи
    pass


@shared_task
def send_course_email(recipients: list, subj: str, message: str):
    send_mail(subj, message, settings.DEFAULT_FROM_EMAIL, recipients)
