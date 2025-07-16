from django.urls import path
from .views import tisch_view, bestellung_absenden, home

urlpatterns = [
    path('', home, name='home'),
    path('tisch/<int:tisch_id>/', tisch_view, name='tisch_view'),
    path('tisch/<int:tisch_id>/bestellen/', bestellung_absenden, name='bestellung_absenden'),
    
]
