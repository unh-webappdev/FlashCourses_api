"""
Courses REST API Class-Based URLs

By:    Patrick R. McElhiney
Date:  4/10/2018
"""

from django.urls import path
from . import views

from .views import (
    CreateInstitutionAPIView,
    RetrieveInstitutionAPIView,
    ListInstitutionAPIView,
    DestroyInstitutionAPIView,
    UpdateInstitutionAPIView,
    CreateCourseAPIView,
    RetrieveCourseAPIView,
    ListCourseAPIView,
    DestroyCourseAPIView,
    UpdateCourseAPIView
)

app_name = 'courses_api'

urlpatterns = [
    path('institution/create/', views.CreateInstitutionAPIView.as_view()),
    path('institution/retrieve/<uuid:unique_id>', views.RetrieveInstitutionAPIView.as_view()),
    path('institution/list/', views.ListInstitutionAPIView.as_view()),
    path('institution/delete/<uuid:unique_id>', views.DestroyInstitutionAPIView.as_view()),
    path('institution/update/<uuid:unique_id>', views.UpdateInstitutionAPIView.as_view()),
    path('course/create/', views.CreateCourseAPIView.as_view()),
    path('course/retrieve/<uuid:unique_id>', views.RetrieveCourseAPIView.as_view()),
    path('course/list/', views.ListCourseAPIView.as_view()),
    path('course/delete/<uuid:unique_id>', views.DestroyCourseAPIView.as_view()),
    path('course/update/<uuid:unique_id>', views.UpdateCourseAPIView.as_view())
]
