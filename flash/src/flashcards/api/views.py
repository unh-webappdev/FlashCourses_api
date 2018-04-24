"""
FlashCourses Decks & Cards REST API Class-Based Views

File Path:     /flash/src/flashcards/api/views.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/22/2018

NOTE: Uncomment the commented code below to enable authentication with JWT.
"""


# Deck Fields Generalization
DECK_UNIQUE_ID = 'unique_id'

# Card Fields Generalization
CARD_UNIQUE_ID = 'unique_id'


from .serializers import (
    DeckSerializer,
    DeckOutputSerializer,
    DeckDetailSerializer,
    CardSerializer,
    CardOutputSerializer,
)
from flashcards.models import Deck, Card
from rest_framework import generics
from .permissions import IsDeckOwner, IsCardOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class CreateDeckAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)

class RetrieveDeckAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Deck object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = DECK_UNIQUE_ID
    queryset = Deck.objects.all()
    serializer_class = DeckOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListDeckAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Decks associated with a Course.
    """
    queryset = Deck.objects.all().order_by('title')
    serializer_class = DeckOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyDeckAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Deck.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = DECK_UNIQUE_ID
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (IsDeckOwner,IsAdminUser)

class UpdateDeckAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Deck object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = DECK_UNIQUE_ID
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (IsDeckOwner,IsAdminUser)

class DetailDeckAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for getting the Detail of a Deck object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = DECK_UNIQUE_ID
    queryset = Deck.objects.all()
    serializer_class = DeckDetailSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CreateCardAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Card.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RetrieveCardAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Card object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = CARD_UNIQUE_ID
    queryset = Card.objects.all()
    serializer_class = CardOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListCardAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Cards associated with a Deck.
    """
    queryset = Card.objects.all()
    serializer_class = CardOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyCardAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Card.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = CARD_UNIQUE_ID
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (IsCardOwner, IsAdminUser)

class UpdateCardAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Card object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = CARD_UNIQUE_ID
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (IsCardOwner, IsAdminUser)
