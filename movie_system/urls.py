from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account.views import RegistrationView
from movies.views import CategoryViewset, ShowTimeViewset, MoviesViewset, SalleViewset
from rest_framework.routers import DefaultRouter

from reservations import views




router = DefaultRouter()

router.register(r'category', CategoryViewset, basename='category')
router.register(r'show-time', ShowTimeViewset, basename='showtime')
router.register(r'salle', SalleViewset, basename='salle')
router.register(r'movies', MoviesViewset, basename='movie')

router.register(r'reservation', views.ReservationViewset, basename='rservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(router.urls))
]
