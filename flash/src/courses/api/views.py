"""
FlashCourses Courses & Institutions REST API Class-Based Views

File Path:     /flash/src/courses/api/views.py

Modified By:   Patrick R. McElhiney, Arjun Padaliya
Date Modified: 4/22/2018

NOTE: Uncomment the commented code below to enable authentication with JWT.
"""


# Institution Fields Generalization
INST_UNIQUE_ID = 'unique_id'

# Course Fields Generalization
COUR_UNIQUE_ID = 'unique_id'


from .serializers import (
    InstitutionSerializer,
    InstitutionDetailSerializer,
    CourseSerializer,
    CourseOutputSerializer,
    CourseDetailSerializer,
    CourseTreeSerializer,
)
from courses.models import Institution, Course
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class CreateInstitutionAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Institution.
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (IsAdminUser,)

class RetrieveInstitutionAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving an Institution object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = INST_UNIQUE_ID
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListInstitutionAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Institutions associated with a Course.
    """
    queryset = Institution.objects.all().order_by('institution_name')
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyInstitutionAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting an Institution.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = INST_UNIQUE_ID
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (IsAdminUser,)

class UpdateInstitutionAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Institution object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = INST_UNIQUE_ID
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (IsAdminUser,)

class DetailInstitutionAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for getting the Detail of a Institution object.
    The Detail is a branched view of a single Institution --> Courses
    associated with the Institution object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = INST_UNIQUE_ID
    queryset = Institution.objects.all()
    serializer_class = InstitutionDetailSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CreateCourseAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAdminUser,)

class RetrieveCourseAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Course object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = COUR_UNIQUE_ID
    queryset = Course.objects.all()
    serializer_class = CourseOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListCourseAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Courses associated with a Deck.
    """
    queryset = Course.objects.all().order_by('course_id')
    serializer_class = CourseOutputSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyCourseAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Course.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = COUR_UNIQUE_ID
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAdminUser,)

class UpdateCourseAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Course object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = COUR_UNIQUE_ID
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAdminUser,)

class DetailCourseAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for getting the Detail of a Course object.
    The Detail is a branched view of a single Course --> Decks
    associated with the Course object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = COUR_UNIQUE_ID
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TreeCourseAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for getting the Tree of a Course object.
    The Tree is a branched view of a single Course --> Decks
    associated with the Course object --> Cards associated with
    each of the Deck objects.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = COUR_UNIQUE_ID
    queryset = Course.objects.all()
    serializer_class = CourseTreeSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
