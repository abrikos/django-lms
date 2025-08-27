from django.db import models

from config import settings


# Create your models here.
class Course(models.Model):
    """Course model"""

    name = models.CharField(max_length=150, verbose_name="Name", null=True)
    desc = models.CharField(verbose_name="Desc", null=True, blank=True)
    image = models.ImageField(upload_to="course/", verbose_name="Course picture", null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="course_owner_set", null=True
    )

    def __str__(self):
        return f"{self.id}, {self.name}, {self.desc}"


class Lesson(models.Model):
    """Lesson model"""

    name = models.CharField(max_length=150, verbose_name="Name", null=True)
    desc = models.CharField(verbose_name="Desc", null=True, blank=True)
    url = models.CharField(verbose_name="Video url", null=True, blank=True)
    image = models.ImageField(upload_to="course/", verbose_name="Lesson picture", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_lessons", null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lesson_owner_set", null=True
    )

    def __str__(self):
        return f"{self.id}, {self.name}, {self.desc}"


class Payment(models.Model):
    """Payment model"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="User", null=True)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Payment date")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course", null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson", null=True)
    amount = models.PositiveIntegerField(verbose_name="Payment amount")
    payment_method = models.CharField(
        max_length=50, default="cash", choices=[("cash", "Cash payment"), ("transfer", "Bank transfer")]
    )

    def __str__(self):
        return f"{self.user}, {self.payment_date}, {self.amount}"


class Subscription(models.Model):
    """Subscription model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_subscriptions", null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_subscriptions", null=True)

    def __str__(self):
        return f"{self.user}, {self.course}"
