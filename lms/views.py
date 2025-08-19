from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson, Payment
from lms.permissions import IsOwnerOrReadOnly, IsModerator
from lms.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """Course REST"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    """Lesson REST"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method', 'user']
    ordering_fields = ['payment_date']
