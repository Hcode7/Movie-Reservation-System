from django.shortcuts import render
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class RegistrationView(generics.CreateAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]