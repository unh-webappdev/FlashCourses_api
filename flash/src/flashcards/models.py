from django.db import models
"""
Flash card models for FlashCourses application
Database: FlashCourses- mySQL
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from courses.models import Course

import uuid

class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    unique_id = models.UUIDField(default=uuid.uuid4())
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    #def __str__(self):
    #    return self.title

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
        '''

        return self.parent_user.username == user.username




class Card(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4())
    parent_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()
