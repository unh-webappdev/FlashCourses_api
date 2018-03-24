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
    path('deck/retrieve/<pk>', views.RetrieveDeckAPIView.as_view()),
    path('deck/list/', views.ListDeckAPIView.as_view()),
    path('deck/delete/<pk>', views.DestroyDeckAPIView.as_view()),
    path('deck/update/<pk>', views.UpdateDeckAPIView.as_view()),
    path('card/create/', views.CreateCardAPIView.as_view()),
    path('card/retrieve/<pk>', views.RetrieveCardAPIView.as_view()),
    path('card/list/', views.ListCardAPIView.as_view()),
    path('card/delete/<pk>', views.DestroyCardAPIView.as_view()),
    path('card/update/<pk>', views.UpdateCardAPIView.as_view())
]
