from rest_framework.serializers import ( 
    ModelSerializer, 
) 
from ..models import Deck, Card 

class DeckSerializer(ModelSerializer): 
    """ 
    This serializes the Deck model 
    """ 
    class Meta: 
        model = Deck 
        fields = ('UUID', 'parent_user', 'parent_course', 'title') 

class CardSerializer(ModelSerializer): 
    """ 
    This serializes the Card model 
    """ 
    class Meta: 
        model = Card 
        fields = ('UUID', 'deck', 'front', 'back') 
