from django.contrib import admin
from .models import Category, Movie, Showtime

# Register your models here.


admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Showtime)