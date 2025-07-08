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
