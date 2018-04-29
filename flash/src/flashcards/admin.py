"""
Admin site register for the flashcard models
Author: Andrea Murphy
"""

from django.contrib import admin
from .models import Card, Deck


admin.site.register(Card)
admin.site.register(Deck)
