from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import nfc.views as nfc_views  # 👈 So vermeiden wir den Zirkulären Import

router = DefaultRouter()
router.register(r'nfc-tags', nfc_views.NFCTagViewSet, basename='nfc-tag')  # 👈 Hier angepasst


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nfc.urls')),
]
