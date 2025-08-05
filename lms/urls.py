from django.urls import path
from rest_framework.routers import DefaultRouter

from .models import Lesson
from .serializers import LessonSerializer
from .views import CourseViewSet, LessonList, LessonRetrieve, LessonDelete, LessonUpdate

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = router.urls
urlpatterns.append(path(r'lessons/', LessonList.as_view(), name='lessons'))
urlpatterns.append(path(r'lessons/<int:pk>/', LessonRetrieve.as_view(), name='lessons-view'))
urlpatterns.append(path(r'lessons-delete/<int:pk>/', LessonDelete.as_view(), name='lessons-delete'))
urlpatterns.append(path(r'lessons-update/<int:pk>/', LessonUpdate.as_view(), name='lessons-update'))