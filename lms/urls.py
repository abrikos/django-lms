from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CheckPaymentView, CourseViewSet, LessonViewSet, PaymentList, SubscriptionView

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
router.register(r"lesson", LessonViewSet, basename="lesson")

urlpatterns = router.urls

urlpatterns.append(path(r"payment/", PaymentList.as_view(), name="payments"))
urlpatterns.append(path(r"subscription/", SubscriptionView.as_view(), name="subscription"))
urlpatterns.append(path(r"check-payment/", CheckPaymentView.as_view(), name="check_payment"))
