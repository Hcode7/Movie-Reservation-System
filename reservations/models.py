from django.db import models
from movies.models import Movie, Showtime
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtimes = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.seats >= self.movie.salle.seats:
            raise ValidationError("The number of seats exceeds the capacity of the salle.")
        super().clean()
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)