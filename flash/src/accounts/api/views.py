"""
Jim Canavan
FlashCourses REST API User Registration Class-Based View

File Path:     /flash/src/accounts/api/urls.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/22/2018
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User


class RegistrationAPIView(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
