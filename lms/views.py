from django_filters.rest_framework import DjangoFilterBackend
from dotenv import load_dotenv
from rest_framework import generics, permissions, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Payment, Subscription
from lms.paginators import MyPagination
from lms.permissions import IsModerator, IsOwnerOrReadOnly
from lms.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from lms.services import stripe_create_product, stripe_create_payment, stripe_check_payment, stripe_get_session

load_dotenv()


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """Course REST"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = MyPagination

    def get_permissions(self):
        if self.action in ["list"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ~IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    """Lesson REST"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ~IsModerator]
    pagination_class = MyPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PaymentList(generics.ListCreateAPIView):
    """Get payments list"""
    pagination_class = MyPagination
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method", "user"]
    ordering_fields = ["payment_date"]


class SubscriptionView(APIView):
    """Subscribe to course"""

    def post(self, request):
        user = self.request.user
        course_id = self.request.data["course_id"]
        course = get_object_or_404(Course, pk=course_id)
        user_subs = Subscription.objects.filter(user=user, course=course)
        if user_subs.exists():
            user_subs.delete()
            message = "Subscription deleted"
            return Response({"message": message})
        else:
            domain = self.request.get_host()
            scheme = self.request.scheme
            new_sub = Subscription(user=user, course=course)
            new_sub.save()
            message = "Subscription added"
            product = stripe_create_product(name=course.name)
            price = stripe_create_payment(name=course.name, amount=1000)
            success_url = f"{scheme}://{domain}/payment-done"
            session = stripe_get_session(success_url=success_url, price_id=price.id)
            return Response({"message": message, "payment_url": session.url, "session_id": session.id})


class CheckPaymentView(APIView):
    """Check stripe session payment"""

    def get(self, request):
        return Response(stripe_check_payment(request.query_params.get('session_id')))
