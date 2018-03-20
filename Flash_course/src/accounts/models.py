"""
User models for FlashCourses application
Database: FlashCourses- mySQL
"""
from django.db import models

import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def get_full_name(self):
        """
        Returns full name in the following order: First name, Last Name.
        """
        return "{} {}".format(self.first_name, self.last_name)

class UserIdentification(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_user = models.ForeignKey(on_delete=models.CASCADE, default=1)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=100)

class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_user_id = models.ForeignKey(on_delete=models.CASCADE, default=1)
    parent_course = models.ForeignKey(on_delete=models.CASCADE, default=1)
    title = modles.CharField(max_length=64, null=False, blank=False)

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

