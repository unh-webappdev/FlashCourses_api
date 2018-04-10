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
    path('institution/retrieve/<pk>', views.RetrieveInstitutionAPIView.as_view()),
    path('institution/list/', views.ListInstitutionAPIView.as_view()),
    path('institution/delete/<pk>', views.DestroyInstitutionAPIView.as_view()),
    path('institution/update/<pk>', views.UpdateInstitutionAPIView.as_view()),
    path('course/create/', views.CreateCourseAPIView.as_view()),
    path('course/retrieve/<pk>', views.RetrieveCourseAPIView.as_view()),
    path('course/list/', views.ListCourseAPIView.as_view()),
    path('course/delete/<pk>', views.DestroyCourseAPIView.as_view()),
    path('course/update/<pk>', views.UpdateCourseAPIView.as_view())
]
