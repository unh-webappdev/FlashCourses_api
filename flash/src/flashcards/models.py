"""
Flash card models for FlashCourses application
Database: FlashCourses- mySQL
"""
from django.db import models
from courses.models import Course
from accounts.models import User

import uuid

class Deck(models.Model):
    """
    Deck model
    Primary Key: Django auto ID
    Foreign Key: User from django.contrib.auth.models
    Foreign Key: Institition from courses.models
    """
    title = models.CharField(
                            max_length=64,
                            null=False,
                            blank=False)
    parent_user = models.ForeignKey(
                            User,
                            on_delete=models.CASCADE,
                            default=1)
    parent_course = models.ForeignKey(
                            Course,
                            on_delete=models.CASCADE,
                            default=1)
    deck_description = models.CharField(
                            max_length=64,
                            null=False,
                            blank=False)
    unique_id = models.UUIDField(
                            default=uuid.uuid4,
                            editable= False,
                            unique=True)

    def __str__(self):
        return self.title

    def get_number_cards(self):
        """
        checks the number of cards.
        """
        return self.card_set.count()

    def has_duplicates(self, card):
        """
        checks if the card already exists,
        returns False if it does and return True if not.
        """
        cards = self.card_set.all()
        qs = cards.filter(front=card.front)
        if qs.count() > 1:
            return True
        return False

    def is_owner(self, user):
        '''
        checks the owner and username
        '''
        return self.parent_user.username == user.username


class Card(models.Model):
    """
    Card model
    Primary Key: Django auto ID
    Foreign Key: Deck from flashcards/models.py
    """
    parent_deck = models.ForeignKey(
                            Deck,
                            on_delete=models.CASCADE,
                            default=1)
    front = models.TextField()
    back = models.TextField()
    unique_id = models.UUIDField(
                                default=uuid.uuid4,
                                editable= False,
                                unique=True)

    def __str__(self):
        return self.front + ' , ' + self.back
