from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NFCTagViewSet, UserViewSet, home
from .auth_views import register, login, logout

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'nfc-tags', NFCTagViewSet, basename='nfc-tag')


urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    path('api/logout/', logout, name='logout'),
]
