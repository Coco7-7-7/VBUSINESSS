from django.http import HttpResponse
from rest_framework import viewsets
from .models import NFCTag, CustomUser, Tisch
from .serializers import NFCTagSerializer, UserSerializer
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

def home(request):
    return HttpResponse("Welcome to the NFC Management System!")

class NFCTagViewSet(viewsets.ModelViewSet):
    queryset = NFCTag.objects.all()
    serializer_class = NFCTagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
     

def tisch_view(request, tisch_id):
    tisch = get_object_or_404(Tisch, id=tisch_id)
    speisen = tisch.restaurant.speisen.all()
    return render(request, 'main/tisch.html', {'tisch': tisch, 'speisen': speisen})
