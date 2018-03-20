"""
Course models for FlashCourse application
Database: FlashCourses- mySQL
"""
from django.db import models
<<<<<<< HEAD
import uuid

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class College(models.Model):
    ipeds = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField
    location = models.CharField
=======
>>>>>>> 040e10a905c2a95c6e0ee1b105fffa607719a7cb
