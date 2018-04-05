"""
Admin panel for the Accounts app
"""

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

