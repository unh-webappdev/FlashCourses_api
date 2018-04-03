"""
Admin panel for the Accounts app
"""

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display= ('user_id', 'parent_user', 'parent_institution')

admin.site.register(UserProfile, UserProfileAdmin)

