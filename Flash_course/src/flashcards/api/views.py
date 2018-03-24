from .serializers import DeckSerializer, CardSerializer
from flashcards.models import Deck, Card
from rest_framework import generics

class CreateDeckAPIView(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class RetrieveDeckAPIView(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class ListDeckAPIView(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DestroyDeckAPIView(generics.DestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class UpdateDeckAPIView(generics.UpdateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class CreateCardAPIView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class RetrieveCardAPIView(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ListCardAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class DestroyCardAPIView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class UpdateCardAPIView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
