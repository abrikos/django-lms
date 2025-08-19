from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterView, UserViewSet
router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = router.urls


