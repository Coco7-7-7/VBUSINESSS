from django.http import HttpResponse
from rest_framework import viewsets
from .models import NFCTag, CustomUser
from .serializers import NFCTagSerializer, UserSerializer
from rest_framework import viewsets

def home(request):
    return HttpResponse("Welcome to the NFC Management System!")

class NFCTagViewSet(viewsets.ModelViewSet):
    queryset = NFCTag.objects.all()
    serializer_class = NFCTagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    