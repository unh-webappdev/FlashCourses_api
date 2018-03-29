"""
Admin panel for the Flashcard app
"""
<<<<<<< HEAD
=======
from django.contrib import admin
>>>>>>> e4fe2af44ce442e64d6c364d527789deb22c51cf

from django.contrib import admin
from .models import Card, Deck

class CardAdmin(admin.ModelAdmin):
    list_display= ()

class DeckAdmin(admin.ModelAdmin):
    list_display= ()


admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
