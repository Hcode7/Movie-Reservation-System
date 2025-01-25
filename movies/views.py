from django.shortcuts import render
from .models import Movie, Category, Showtime, Salle
from .serializer import CategorySerializer, MovieSerializer, ShowTimeSerializer, SalleSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadonly
from rest_framework import filters

# Create your views here.

class SalleViewset(ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class ShowTimeViewset(ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowTimeSerializer
    permission_classes = [permissions.IsAdminUser]

class MoviesViewset(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadonly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "release_date"]

