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
        fields=('ipeds', 'institution_name', 'location')

class CourseSerializer(ModelSerializer):
    """
    This serilaizes the Course model
    """
    class Meta:
        model=Course
        fields=('course_title','course_number','course_id','parent_institution')
