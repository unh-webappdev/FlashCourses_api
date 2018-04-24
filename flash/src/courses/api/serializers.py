"""
FlashCourses Courses & Institutions REST API Serializers

File Path:     /flash/src/courses/api/serializers.py

Modified By:   Patrick R. McElhiney, Arjun Padaliya
Date Modified: 4/22/2018
"""


# Institution Fields Generalization
INST_UNIQUE_ID          = 'unique_id'
INST_IPEDS              = 'ipeds'
INST_INSTITUTION_NAME   = 'institution_name'
INST_LOCATION           = 'location'

# Course Fields Generalization
COUR_UNIQUE_ID          = 'unique_id'
COUR_COURSE_TITLE       = 'course_title'
COUR_COURSE_DESCRIPTION = 'course_description'
COUR_COURSE_ID          = 'course_id'
COUR_PARENT_INSTITUTION = 'parent_institution'

# Deck Fields Generalization
DECK_TITLE              = 'title'


from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from ..models import Institution, Course
from flashcards.models import Deck, Card
from flashcards.api.serializers import (
    DeckOutputSerializer,
    DeckDetailSerializer,
)


class InstitutionSerializer(ModelSerializer):
    """
    This serializes the Institution model
    """
    class Meta:
        model=Institution
        fields=(INST_UNIQUE_ID, INST_IPEDS, INST_INSTITUTION_NAME, INST_LOCATION)


class InstitutionDetailSerializer(ModelSerializer):
    """
    This serializes the Institution model for Detail
    """
    courses = SerializerMethodField(source='get_courses')
    
    class Meta:
        model=Institution
        fields=(INST_UNIQUE_ID, INST_IPEDS, INST_INSTITUTION_NAME, INST_LOCATION, 'courses')
    
    def get_courses(self, obj):
        courses_queryset = obj.course_set.all().order_by(COUR_COURSE_ID)
        return CourseOutputSerializer(courses_queryset, many=True).data


class CourseSerializer(ModelSerializer):
    """
    This serilaizes the Course model
    """
    class Meta:
        model=Course
        fields=(COUR_UNIQUE_ID, COUR_COURSE_TITLE, COUR_COURSE_DESCRIPTION, COUR_COURSE_ID, COUR_PARENT_INSTITUTION)


class CourseOutputSerializer(ModelSerializer):
    """
    This serializes the Course model for Output
    """
    parent_institution = SerializerMethodField(source='get_parent_institution')
    parent_institution_url = SerializerMethodField(source='get_parent_institution_url')

    class Meta:
        model = Course
        fields = (COUR_UNIQUE_ID, COUR_COURSE_TITLE, COUR_COURSE_DESCRIPTION, COUR_COURSE_ID, COUR_PARENT_INSTITUTION, 'parent_institution_url')

    def get_parent_institution(self, obj):
        return obj.parent_institution.unique_id

    def get_parent_institution_url(self, obj):
        return "/courses/api/institution/retrieve/{}".format(obj.parent_institution.unique_id)

class CourseDetailSerializer(ModelSerializer):
    """
    This serializes the Course model for Detail
    """
    parent_institution = SerializerMethodField(source='get_parent_institution')
    parent_institution_url = SerializerMethodField(source='get_parent_institution_url')
    decks = SerializerMethodField(source='get_decks')
    
    class Meta:
        model = Course
        fields = (COUR_UNIQUE_ID, COUR_COURSE_TITLE, COUR_COURSE_DESCRIPTION, COUR_COURSE_ID, COUR_PARENT_INSTITUTION, 'parent_institution_url', 'decks')

    def get_parent_institution(self, obj):
        return obj.parent_institution.unique_id

    def get_parent_institution_url(self, obj):
        return "/courses/api/institution/retrieve/{}".format(obj.parent_institution.unique_id)
    
    def get_decks(self, obj):
        decks_queryset = obj.deck_set.all().order_by(DECK_TITLE)
        return DeckOutputSerializer(decks_queryset, many=True).data

class CourseTreeSerializer(ModelSerializer):
    """
    This serializes the Course model for Tree
    """
    parent_institution = SerializerMethodField(source='get_parent_institution')
    parent_institution_url = SerializerMethodField(source='get_parent_institution_url')
    decks = SerializerMethodField(source='get_decks')
    
    class Meta:
        model = Course
        fields = (COUR_UNIQUE_ID, COUR_COURSE_TITLE, COUR_COURSE_DESCRIPTION, COUR_COURSE_ID, COUR_PARENT_INSTITUTION, 'parent_institution_url', 'decks')

    def get_parent_institution(self, obj):
        return obj.parent_institution.unique_id

    def get_parent_institution_url(self, obj):
        return "/courses/api/institution/retrieve/{}".format(obj.parent_institution.unique_id)
    
    def get_decks(self, obj):
        decks_queryset = obj.deck_set.all().order_by(DECK_TITLE)
        return DeckDetailSerializer(decks_queryset, many=True).data
