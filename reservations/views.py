from django.shortcuts import render
from movies.models import Movie, Showtime
from .models import Reservation
from .serializer import ReservationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ReservationViewset(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(user=self.request.user)