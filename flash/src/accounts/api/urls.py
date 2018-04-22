"""
FlashCourses REST API User Registration Class-Based URLs

File Path:     /flash/src/accounts/api/urls.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/22/2018
"""
from django.urls import path
from . import views

from .views import (
    RegistrationAPIView
)

app_name = 'accounts_api'

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name="registration")
]

