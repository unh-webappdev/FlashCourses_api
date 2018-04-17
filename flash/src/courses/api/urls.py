"""
FlashCourses Courses & Institutions REST API Class-Based URLs

File Path:     /flash/src/courses/api/urls.py

Modified By:   Patrick R. McElhiney, Arjun Padaliya
Date Modified: 4/16/2018
"""

from django.urls import path
from . import views

from .views import (
    CreateInstitutionAPIView,
    RetrieveInstitutionAPIView,
    ListInstitutionAPIView,
    DestroyInstitutionAPIView,
    UpdateInstitutionAPIView,
    DetailInstitutionAPIView,
    CreateCourseAPIView,
    RetrieveCourseAPIView,
    ListCourseAPIView,
    DestroyCourseAPIView,
    UpdateCourseAPIView,
    DetailCourseAPIView,
    TreeCourseAPIView,
)

app_name = 'courses_api'

urlpatterns = [
    path('institution/create/', views.CreateInstitutionAPIView.as_view(), name='institution_create'),
    path('institution/retrieve/<uuid:unique_id>', views.RetrieveInstitutionAPIView.as_view(), name='institution_retrieve'),
    path('institution/list/', views.ListInstitutionAPIView.as_view(), name='institution_list'),
    path('institution/delete/<uuid:unique_id>', views.DestroyInstitutionAPIView.as_view(), name='institution_delete'),
    path('institution/update/<uuid:unique_id>', views.UpdateInstitutionAPIView.as_view(), name='institution_update'),
    path('institution/detail/<uuid:unique_id>', views.DetailInstitutionAPIView.as_view(), name='institution_detail'),
    path('course/create/', views.CreateCourseAPIView.as_view(), name='course_create'),
    path('course/retrieve/<uuid:unique_id>', views.RetrieveCourseAPIView.as_view(), name='course_retrieve'),
    path('course/list/', views.ListCourseAPIView.as_view(), name='course_list'),
    path('course/delete/<uuid:unique_id>', views.DestroyCourseAPIView.as_view(), name='course_delete'),
    path('course/update/<uuid:unique_id>', views.UpdateCourseAPIView.as_view(), name='course_update'),
    path('course/detail/<uuid:unique_id>', views.DetailCourseAPIView.as_view(), name='course_detail'),
    path('course/tree/<uuid:unique_id>', views.TreeCourseAPIView.as_view(), name='course_tree'),
]
