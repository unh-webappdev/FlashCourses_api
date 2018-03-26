"""
Admin panel for the Flashcard app
"""
from django.contrib import admin

from django.contrib import admin
from .models import Card, Deck

class CardAdmin(admin.ModelAdmin):
    list_display= ()

class DeckAdmin(admin.ModelAdmin):
    list_display= ()


admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
