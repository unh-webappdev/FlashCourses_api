"""
Author: Andrea Murphy
Last Updated: April 2018
Relative File Path: flash/scr/courses/admin.py
Description: Admin site register for the courses models
"""

from django.contrib import admin
from .models import Institution, Course


admin.site.register(Institution)
admin.site.register(Course)

