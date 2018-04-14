"""
FlashCourses REST API Serializers

By:    Patrick R. McElhiney
Date:  4/10/2018
"""

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
        fields = ('unique_id', 'parent_user', 'parent_course', 'title') 

class CardSerializer(ModelSerializer): 
    """ 
    This serializes the Card model 
    """ 
    class Meta: 
        model = Card 
        fields = ('unique_id', 'parent_deck', 'front', 'back') 
