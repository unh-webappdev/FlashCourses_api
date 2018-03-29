"""
Admin panel for the Courses app
"""

from django.contrib import admin
from .models import Institution, Course


class InstitutionAdmin(admin.ModelAdmin):
    list_display= ()



class CourseAdmin(admin.ModelAdmin):
    list_display= ()


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)

