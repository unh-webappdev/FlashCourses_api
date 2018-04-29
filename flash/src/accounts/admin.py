"""
Author: Andrea Murphy
Last Updated: April 2018
Relative File Path: flash/scr/accounts/admin.py
Description: Admin site register for the accounts models
"""

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

