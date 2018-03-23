"""
Admin panel for the Accounts app
"""

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display= ()

admin.site.register(UserProfile, UserProfileAdmin)

