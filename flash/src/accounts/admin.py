"""
Admin site register for the accounts models
Author: Andrea Murphy
"""

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

