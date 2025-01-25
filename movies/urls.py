from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.MoviesView.as_view(), name='movie'),
#     path('movie/<int:pk>/', views.SingleMovieView.as_view(), name='movie_detail'),
#     path('create-movie/', views.CreateMovieView.as_view(), name='create-movie'),
#     path('update-movie/<int:pk>/', views.AdminSingleMovieView.as_view(), name='update'),
# ]