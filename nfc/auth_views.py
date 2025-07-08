from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import re

def is_password_strong(password):
    # Mindestens 8 Zeichen, mindestens 1 Zahl, 1 Großbuchstabe und 1 Sonderzeichen
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):  # prüft auf Zahl
        return False
    if not re.search(r"[A-Z]", password):  # prüft auf Großbuchstaben
        return False
    if not re.search(r"[\W_]", password):  # prüft auf Sonderzeichen
        return False
    return True
 
# User Registrierung
@api_view(['POST'])
def register(request):
    # Eingabedaten abrufen
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    
    # Überprüfe, ob alle Felder ausgefüllt sind
    if not username or not password or not email:
        return Response({"error": "Benutzername, Passwort und Email sind erforderlich"}, status=status.HTTP_400_BAD_REQUEST)

    # Überprüfe, ob der Benutzername bereits existiert
    if get_user_model().objects.filter(username=username).exists():
        return Response({"error": "Benutzername bereits vergeben"}, status=status.HTTP_400_BAD_REQUEST)

    # Überprüfe, ob die E-Mail-Adresse bereits registriert wurde
    if get_user_model().objects.filter(email=email).exists():
        return Response({"error": "Diese E-Mail-Adresse wird bereits verwendet"}, status=status.HTTP_400_BAD_REQUEST)
    
    is_strong, message = is_password_strong(password)
    if not is_strong:
        return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)


    # Benutzer erstellen
    user = get_user_model().objects.create_user(username=username, password=password, email=email)

    # Token für den Benutzer erstellen
    token, created = Token.objects.get_or_create(user=user)

    # Erfolgreiche Antwort mit Token
    return Response({
        "token": token.key,
        "message": "Registrierung erfolgreich",
        "username": user.username,
        "email": user.email
    }, status=status.HTTP_201_CREATED)

# User Login
@api_view(['POST'])
def login(request):
    from django.contrib.auth import authenticate

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Login erfolgreich"})
    return Response({"error": "Ungültige Anmeldedaten"}, status=status.HTTP_400_BAD_REQUEST)

# User Logout (Token löschen)
@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response({"message": "Logout erfolgreich"}, status=status.HTTP_200_OK)
