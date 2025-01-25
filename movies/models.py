from django.db import models
from enum import Enum

# Create your models here.

class Salle(models.Model):
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Salle Number {self.id}"

class Category(models.Model):
    genre = models.CharField(max_length=500)

    def __str__(self):
        return self.genre

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    duration = models.DurationField()
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.date} at {self.time}"
    
