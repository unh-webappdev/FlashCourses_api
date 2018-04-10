from django.urls import path, re_path, include

app_name = 'courses'

urlpatterns = [
    path('api/', include('courses.api.urls', namespace='courses_api')),
]
