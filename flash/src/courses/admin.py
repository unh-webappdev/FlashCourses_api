"""
Admin panel for the Courses app
"""

from django.contrib import admin
from .models import Institution, Course



class InstitutionAdmin(admin.ModelAdmin):
    list_display= ('ipeds', 'institution_name', 'location')


class CourseAdmin(admin.ModelAdmin):
    list_display= ('course_id', 'parent_institution')


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)

