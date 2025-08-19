from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserRegistrationSerializer, UserSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """Token view"""
    serializer_class = MyTokenObtainPairSerializer

def register(request):
    """Registration"""
    if request.method == 'POST':
        for key, value in request.POST.items():
            print(f"{key}: {value}")

    return HttpResponse()

class RegisterView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    """User REST"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            # Apply specific permissions for the create action
            permission_classes = []
        else:
            # Apply different permissions for other actions (list, retrieve, update, destroy)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]