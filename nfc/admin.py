from django.contrib import admin
from .models import Restaurant, Tisch, Speise, Bestellung, NFCTag

admin.site.register(NFCTag)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'adresse')
    search_fields = ('name',)

@admin.register(Tisch)
class TischAdmin(admin.ModelAdmin):
    list_display = ('nummer', 'restaurant')
    list_filter = ('restaurant',)

@admin.register(Speise)
class SpeiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'preis', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name',)

@admin.register(Bestellung)
class BestellungAdmin(admin.ModelAdmin):
    list_display = ('id', 'tisch', 'status', 'erstellt_am')
    list_filter = ('status', 'tisch__restaurant')
    date_hierarchy = 'erstellt_am'
    filter_horizontal = ('speisen',)
