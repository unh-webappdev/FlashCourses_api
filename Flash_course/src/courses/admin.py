"""
Admin panel for the Courses app
"""

from django.contrib import admin
<<<<<<< HEAD
from .models import Institution, Course

=======

from .models import Institution, Course
>>>>>>> e4fe2af44ce442e64d6c364d527789deb22c51cf

class InstitutionAdmin(admin.ModelAdmin):
    list_display= ()



class CourseAdmin(admin.ModelAdmin):
    list_display= ()


<<<<<<< HEAD
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)

=======

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)
>>>>>>> e4fe2af44ce442e64d6c364d527789deb22c51cf
