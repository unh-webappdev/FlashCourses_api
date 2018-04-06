"""
FlashCourses REST API User Registration Class-Based URLs

Created By:     Patrick R. McElhiney
Modified Date:  4/6/2018
"""
from django.urls import path
from . import views

from .views import (
    RegistrationAPIView
)

app_name = 'accounts_api'

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view())
]

