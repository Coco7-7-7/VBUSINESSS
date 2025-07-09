from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class NFCTag(models.Model):
    tag_id = models.CharField(max_length=100, unique=True)  # Eindeutige Tag-ID
    url = models.URLField(blank=True, null=True)  # Verlinkte URL
    created_at = models.DateTimeField(auto_now_add=True)  # Erstellungsdatum

    def __str__(self):
        return self.tag_id


class CustomUser(AbstractUser):
    # Weitere Felder hinzufügen, falls nötig
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Dies wird den Konflikt beheben
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Dies wird den Konflikt beheben
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tisch(models.Model):
    nummer = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tische')

    def __str__(self):
        return f"Tisch {self.nummer} ({self.restaurant.name})"

class Speise(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True)
    preis = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='speisen')

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

class Bestellung(models.Model):
    STATUS_CHOICES = [
        ('neu', 'Neu'),
        ('in_bearbeitung', 'In Bearbeitung'),
        ('fertig', 'Fertig'),
    ]

    tisch = models.ForeignKey(Tisch, on_delete=models.CASCADE, related_name='bestellungen')
    speisen = models.ManyToManyField(Speise)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='neu')

    def __str__(self):
        return f"Bestellung {self.id} – Tisch {self.tisch.nummer} – {self.status}"
