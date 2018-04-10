"""
FlashCourses REST API Class-Based Views

By:    Patrick R. McElhiney
Date:  4/10/2018

NOTE: Uncomment the commented code to enable authentication with JWT.
"""

from .serializers import DeckSerializer, CardSerializer
from flashcards.models import Deck, Card
from rest_framework import generics
#from rest_framework import permissions

class CreateDeckAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RetrieveDeckAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Deck object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListDeckAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Decks associated with a Course.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyDeckAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Deck.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UpdateDeckAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Deck object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
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
    lookup_field = "unique_id"
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListCardAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Cards associated with a Deck.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyCardAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Card.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UpdateCardAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Card object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
