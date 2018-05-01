"""
Author: Andrea Murphy
Last Updated: April 2018
Relative File Path: flash/scr/flashcards/admin.py
Description: Admin site register for the flashcards models
"""

from django.contrib import admin
from .models import Card, Deck


admin.site.register(Card)
admin.site.register(Deck)
