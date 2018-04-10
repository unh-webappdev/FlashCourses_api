"""
Flashcards REST API Class-Based URLs

By:    Patrick R. McElhiney
Date:  4/10/2018
"""

from django.urls import path
from . import views

from .views import (
    CreateDeckAPIView,
    RetrieveDeckAPIView,
    ListDeckAPIView,
    DestroyDeckAPIView,
    UpdateDeckAPIView,
    CreateCardAPIView,
    RetrieveCardAPIView,
    ListCardAPIView,
    DestroyCardAPIView,
    UpdateCardAPIView
)

app_name = 'flashcards_api'

urlpatterns = [
    path('deck/create/', views.CreateDeckAPIView.as_view()),
    path('deck/retrieve/<uuid:unique_id>', views.RetrieveDeckAPIView.as_view()),
    path('deck/list/', views.ListDeckAPIView.as_view()),
    path('deck/delete/<uuid:unique_id>', views.DestroyDeckAPIView.as_view()),
    path('deck/update/<uuid:unique_id>', views.UpdateDeckAPIView.as_view()),
    path('card/create/', views.CreateCardAPIView.as_view()),
    path('card/retrieve/<uuid:unique_id>', views.RetrieveCardAPIView.as_view()),
    path('card/list/', views.ListCardAPIView.as_view()),
    path('card/delete/<uuid:unique_id>', views.DestroyCardAPIView.as_view()),
    path('card/update/<uuid:unique_id>', views.UpdateCardAPIView.as_view())
]

