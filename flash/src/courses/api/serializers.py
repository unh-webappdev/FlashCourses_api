"""
FlashCourses Courses & Institutions REST API Serializers

File Path:     /flash/src/courses/api/serializers.py

Modified By:   Patrick R. McElhiney, Arjun Padaliya
Date Modified: 4/16/2018
"""


# Institution Fields Generalization
inst_unique_id          = 'unique_id'
inst_ipeds              = 'ipeds'
inst_institution_name   = 'institution_name'
inst_location           = 'location'

# Course Fields Generalization
cour_unique_id          = 'unique_id'
cour_course_title       = 'course_title'
cour_course_number      = 'course_number'
cour_course_id          = 'course_id'
cour_parent_institution = 'parent_institution'

# Deck Fields Generalization
deck_title              = 'title'


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
        fields=(inst_unique_id, inst_ipeds, inst_institution_name, inst_location)


class InstitutionDetailSerializer(ModelSerializer):
    """
    This serializes the Institution model for Detail
    """
    courses = SerializerMethodField(source='get_courses')
    
    class Meta:
        model=Institution
        fields=(inst_unique_id, inst_ipeds, inst_institution_name, inst_location, 'courses')
    
    def get_courses(self, obj):
        courses_queryset = obj.course_set.all().order_by(cour_course_id)
        return CourseOutputSerializer(courses_queryset, many=True).data


class CourseSerializer(ModelSerializer):
    """
    This serilaizes the Course model
    """
    class Meta:
        model=Course
        fields=(cour_unique_id, cour_course_title, cour_course_number, cour_course_id, cour_parent_institution)


class CourseOutputSerializer(ModelSerializer):
    """
    This serializes the Course model for Output
    """
    parent_institution = SerializerMethodField(source='get_parent_institution')
    parent_institution_url = SerializerMethodField(source='get_parent_institution_url')

    class Meta:
        model = Course
        fields = (cour_unique_id, cour_course_title, cour_course_number, cour_course_id, cour_parent_institution, 'parent_institution_url')

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
        fields = (cour_unique_id, cour_course_title, cour_course_number, cour_course_id, cour_parent_institution, 'parent_institution_url', 'decks')

    def get_parent_institution(self, obj):
        return obj.parent_institution.unique_id

    def get_parent_institution_url(self, obj):
        return "/courses/api/institution/retrieve/{}".format(obj.parent_institution.unique_id)
    
    def get_decks(self, obj):
        decks_queryset = obj.deck_set.all().order_by(deck_title)
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
        fields = (cour_unique_id, cour_course_title, cour_course_number, cour_course_id, cour_parent_institution, 'parent_institution_url', 'decks')

    def get_parent_institution(self, obj):
        return obj.parent_institution.unique_id

    def get_parent_institution_url(self, obj):
        return "/courses/api/institution/retrieve/{}".format(obj.parent_institution.unique_id)
    
    def get_decks(self, obj):
        decks_queryset = obj.deck_set.all().order_by(deck_title)
        return DeckDetailSerializer(decks_queryset, many=True).data
