from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from lms.models import Course, Lesson, Subscription


class Command(BaseCommand):
    help = 'Fill database'

    def handle(self, *args, **options):
        User = get_user_model()
        email = 'admin@a.com'
        password = '123'  # Change this to a secure password

        with transaction.atomic():
            if not User.objects.filter(email=email).exists():
                self.stdout.write(self.style.HTTP_INFO(f"Creating superuser '{email}'..."))
                user = User.objects.create_superuser(email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"Superuser '{email}' created successfully."))
            else:
                self.stdout.write(self.style.WARNING(f"Superuser '{email}' already exists. Skipping creation."))
        email = 'a@a.com'
        try:
            user = User(email=email, password='123')
            user.save()
        except:
            user = User.objects.get(email=email)
        course = Course(name="Course 1", owner=user)
        course.save()
        Lesson(name="Lesson 1", course=course, owner=user).save()
        Lesson(name="Lesson 2", course=course, owner=user).save()
        Lesson(name="Lesson 3", course=course, owner=user).save()
        Subscription(course=course, user=user).save()