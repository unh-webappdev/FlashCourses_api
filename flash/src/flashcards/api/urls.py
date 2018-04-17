"""
FlashCourses Decks & Cards REST API Class-Based URLs

File Path:     /flash/src/flashcards/api/urls.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/16/2018
"""

from django.urls import path
from . import views

from .views import (
    CreateDeckAPIView,
    RetrieveDeckAPIView,
    ListDeckAPIView,
    DestroyDeckAPIView,
    UpdateDeckAPIView,
    DetailDeckAPIView,
    CreateCardAPIView,
    RetrieveCardAPIView,
    ListCardAPIView,
    DestroyCardAPIView,
    UpdateCardAPIView,
)

app_name = 'flashcards_api'

urlpatterns = [
    path('deck/create/', views.CreateDeckAPIView.as_view(), name='deck_create'),
    path('deck/retrieve/<uuid:unique_id>', views.RetrieveDeckAPIView.as_view(), name='deck_retrieve'),
    path('deck/list/', views.ListDeckAPIView.as_view(), name='deck_list'),
    path('deck/delete/<uuid:unique_id>', views.DestroyDeckAPIView.as_view(), name='deck_delete'),
    path('deck/update/<uuid:unique_id>', views.UpdateDeckAPIView.as_view(), name='deck_update'),
    path('deck/detail/<uuid:unique_id>', views.DetailDeckAPIView.as_view(), name='deck_detail'),
    path('card/create/', views.CreateCardAPIView.as_view(), name='card_create'),
    path('card/retrieve/<uuid:unique_id>', views.RetrieveCardAPIView.as_view(), name='card_retrieve'),
    path('card/list/', views.ListCardAPIView.as_view(), name='card_list'),
    path('card/delete/<uuid:unique_id>', views.DestroyCardAPIView.as_view(), name='card_delete'),
    path('card/update/<uuid:unique_id>', views.UpdateCardAPIView.as_view(), name='card_update')
]

