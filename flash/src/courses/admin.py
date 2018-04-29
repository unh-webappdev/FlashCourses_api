"""
Admin site register for the courses models
Author: Andrea Murphy
"""

from django.contrib import admin
from .models import Institution, Course


admin.site.register(Institution)
admin.site.register(Course)

