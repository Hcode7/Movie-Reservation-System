from rest_framework import serializers
from .models import Movie, Showtime, Category, Salle


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['genre']


class ShowTimeSerializer(serializers.ModelSerializer):
    movie_display = serializers.StringRelatedField(source='movie', read_only=True)
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Showtime
        fields = ['movie', 'movie_display', 'date', 'time']

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ["seats"]

class MovieSerializer(serializers.ModelSerializer):
    category_display = serializers.StringRelatedField(source='category', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    showtimes = ShowTimeSerializer(many=True, read_only=True)
    salle = serializers.PrimaryKeyRelatedField(queryset=Salle.objects.all())

    class Meta:
        model = Movie
        fields = ['category', 'category_display', 'title' , 'description', 'img', 'salle', 'release_date', 'duration', 'showtimes']
    
    