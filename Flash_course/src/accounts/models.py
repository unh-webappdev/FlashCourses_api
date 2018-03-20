"""
User models for FlashCourses application
Database: FlashCourses- mySQL
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from courses.models import Instution, Course

import uuid

class UserProfile(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    parent_user = models.ForeignKey(User,  on_delete=models.CASCADE, default=1)
    parent_institution = models.ForeignKey(Instution, on_delete=models.CASCADE, default=1)


class Deck(models.Model):
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64, null=False, blank=False)

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
