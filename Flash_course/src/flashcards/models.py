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
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64, null=False, blank=False)

class Card(models.Model):
    parent_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.TextField()
    back = models.TextField()

