"""
FlashCourses- Test cases for API endpoints for deleting data in card
Created By: Swechchha Tiwari  4/13/2018

Relative File Path:  /flash/src/flashcards/test_flashcards/test_card_delete.py
Modified Date:  4/22/2018
"""

import json
import uuid

from django.shortcuts import reverse
from django.test import Client, TestCase
from flashcards.models import Deck, Card
from courses.models import Institution, Course
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class APIdeleteStatusCodeCard(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add all endpoints to be tested
        """
        userone = User.objects.create_user(
            'Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        course_tbl = Course.objects.create(
            course_title='test',
            course_id='2',
            course_description='this is a test data')
        deck_tbl = Deck.objects.create(
            title='testone',
            deck_description='testdescription')
        card_tbl = Card.objects.create(
            front='test',
            back='testone')

        self.delete_method_endpoints_card = [
            reverse(
                'flashcards:flashcards_api:card_delete',
                kwargs={'unique_id': Card.objects.first().unique_id}),

        ]

    def test_self_delete_method_endpoints_card(self):
        """
        Create a request to every endpoint in delete_method_endpoints.
        Ensure returns a 204 response status code
        """
        c = Client()

        deck = Deck.objects.first()
        for endpoint in self.delete_method_endpoints_card:
            response = c.delete(endpoint)
        self.assertEqual(response.status_code, 204)
