"""
Course models for FlashCourse application
Database: FlashCourses- mySQL
"""
from django.db import models


class Instution(models.Model):
    ipeds = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField
    location = models.CharField

class Course(models.Model):
    course_id = models.AutoField(auto_created=True, primary_key=True)
    parent_institution = models.ForeignKey(Instution, on_delete=models.CASCADE, default=1)
