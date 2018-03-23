"""
Admin panel for the Courses app
"""

from django.contrib import admin
from .models import Instution, Course

class InstutionAdmin(admin.ModelAdmin):
    list_display= ()



class CourseAdmin(admin.ModelAdmin):
    list_display= ()



admin.site.register(Instution, InstutionAdmin)
admin.site.register(Course, CourseAdmin)
