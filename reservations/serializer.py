from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Reservation
from django.db.models import Sum
from django.db.models.functions import Coalesce
from datetime import timezone

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "movie", "showtimes", "seats", "reserved_at"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        movie = data['movie']
        requested_Seats = data['seats']
        reserved_at = data['reserved_at']

        total_reserved_seats = Reservation.objects.filter(movie=movie).aggregate(total_seats=Coalesce(Sum('seats'), 0))['total_seats']

        salle_capacity = movie.salle.seats

        if total_reserved_seats + requested_Seats > salle_capacity:
            raise ValidationError(
                f"Not enough seats available. Only {salle_capacity - total_reserved_seats} seats are left."
            )
        
        

        return data