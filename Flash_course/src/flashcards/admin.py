"""
Admin panel for the Flashcard app
"""

from django.contrib import admin

from django.contrib import admin
from .models import Deck, Card

class CardAdmin(admin.ModelAdmin):
    list_display= ()



class DeckAdmin(admin.ModelAdmin):
    list_display= ()



admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)

