"""
FlashCourses Decks & Cards REST API Serializers

File Path:     /flash/src/flashcards/api/serializers.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/16/2018
"""


# Deck Fields Generalization
deck_unique_id        = 'unique_id'
deck_parent_user      = 'parent_user'
deck_parent_course    = 'parent_course'
deck_title            = 'title'
deck_deck_description = 'deck_description'

# Card Fields Generalization
card_unique_id     = 'unique_id'
card_parent_deck   = 'parent_deck'
card_front         = 'front'
card_back          = 'back'


from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from ..models import Deck, Card

class DeckSerializer(ModelSerializer):
    """
    This serializes the Deck model
    """
    class Meta:
        model = Deck
        fields = (deck_unique_id, deck_parent_user, deck_parent_course, deck_title, deck_deck_description)


class DeckOutputSerializer(ModelSerializer):
    """
    This serializes the Deck model for Output
    """
    parent_user = SerializerMethodField(source='get_parent_user')
    parent_course = SerializerMethodField(source='get_parent_course')
    parent_course_url = SerializerMethodField(source='get_parent_course_url')

    class Meta:
        model = Deck
        fields = (deck_unique_id, deck_parent_user, deck_parent_course, deck_title, deck_deck_description, 'parent_course_url')

    def get_parent_user(self, obj):
        return obj.parent_user.username

    def get_parent_course(self, obj):
        return obj.parent_course.unique_id

    def get_parent_course_url(self, obj):
        return "/courses/api/course/retrieve/{}".format(obj.parent_course.unique_id)


class DeckDetailSerializer(ModelSerializer):
    """
    This serializes the Deck model for Detail
    """
    parent_user = SerializerMethodField(source='get_parent_user')
    parent_course = SerializerMethodField(source='get_parent_course')
    parent_course_url = SerializerMethodField(source='get_parent_course_url')
    cards = SerializerMethodField(source='get_cards')
    
    class Meta:
        model = Deck
        fields = (deck_unique_id, deck_parent_user, deck_parent_course, deck_title, deck_deck_description, 'parent_course_url', 'cards')
    
    def get_parent_user(self, obj):
        return obj.parent_user.username

    def get_parent_course(self, obj):
        return obj.parent_course.unique_id

    def get_parent_course_url(self, obj):
        return "/courses/api/course/retrieve/{}".format(obj.parent_course.unique_id)
    
    def get_cards(self, obj):
        cards_queryset = obj.card_set.all()
        return CardOutputSerializer(cards_queryset, many=True).data


class CardSerializer(ModelSerializer):
    """
    This serializes the Card model
    """
    class Meta:
        model = Card
        fields = (card_unique_id, card_parent_deck, card_front, card_back)

class CardOutputSerializer(ModelSerializer):
    """
    This serializes the Card model for Output
    """
    parent_deck = SerializerMethodField(source='get_parent_deck')
    parent_deck_url = SerializerMethodField(source='get_parent_deck_url')

    class Meta:
        model = Card
        fields = (card_unique_id, card_parent_deck, card_front, card_back, 'parent_deck_url')

    def get_parent_deck(self, obj):
        return obj.parent_deck.unique_id

    def get_parent_deck_url(self, obj):
        return "/flashcards/api/deck/retrieve/{}".format(obj.parent_deck.unique_id)
