"""
Course models for FlashCourse application
Database: FlashCourses- mySQL
"""
from django.db import models
import uuid

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class College(models.Model):
    ipeds = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField
    location = models.CharField
