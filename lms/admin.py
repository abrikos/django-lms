from django.contrib import admin
from .models import Course, Lesson, Payment, Subscription
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
admin.site.register(Subscription)
