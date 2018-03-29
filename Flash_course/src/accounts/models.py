from django.db import models
"""
User models for FlashCourses application
Database: FlashCourses- mySQL
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

from courses.models import Institution

import uuid

class UserProfile(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    parent_user = models.ForeignKey(User,  on_delete=models.CASCADE, default=1)
    parent_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=1)

