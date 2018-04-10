"""
Courses REST API Serializers

By:    Patrick R. McElhiney
Date:  4/10/2018
"""

from rest_framework.serializers import (
ModelSerializer,
)
from ..models import Institution, Course

class InstitutionSerializer(ModelSerializer):
    """
    This serializes the Institute model
    """
    class Meta:
        model=Institution
        fields=('unique_id', 'ipeds', 'institution_name', 'location')

class CourseSerializer(ModelSerializer):
    """
    This serilaizes the Course model
    """
    class Meta:
        model=Course
        fields=('unique_id', 'course_title','course_number','course_id','parent_institution')
