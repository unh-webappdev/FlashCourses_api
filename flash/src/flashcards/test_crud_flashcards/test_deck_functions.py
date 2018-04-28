"""
FlashCards- Test cases for deck model functions
Created By: Swechchha Tiwari  4/25/2018

Relative File Path:  /flash/src/flashcards/test_crud_flashcards/test_deck_functions.py
Modified Date:  4/25/2018
"""

import json
import uuid

from django.shortcuts import reverse
from django.test import Client, TestCase
from flashcards.models import Deck, Card
from courses.models import Institution, Course
from accounts.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class CardTest(TestCase):

    def setUp(self):
        """
        setUp needed to perform the tests, it is called before every test function.
        """

        self.user = User.objects.create_user(username = 'Swechchha', email = 'swechchha@gmail.com', password = 'imppwdswe')
        self.course_one = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        self.deck_one = Deck.objects.create(parent_user = self.user, title = 'test title', deck_description = 'this is a test')
        self.card = Card.objects.create(front = 'test', back = 'testsback', parent_deck = self.deck_one)
        self.card = Card.objects.create(front = 'test', back = 'testsback', parent_deck = self.deck_one)
        self.card = Card.objects.create(front = 'testfront', back = 'testsback', parent_deck = self.deck_one)

    def test_get_number_cards(self):
        """
        Test for get_number_cards method defined in models.py
        """

        d_one =  Deck.objects.first()
        result = d_one.get_number_cards()
        self.assertEqual(result,3)

    def test_has_duplicates(self, card=None):
        """
        Test for has_duplicates method defined in models.py
        """

        if card is None:
           d_one = Deck.objects.first()
           c_one = Card.objects.all()
           self.assertEqual(Card.objects.count(), 3)
           result = d_one.has_duplicates(self.card)
           self.assertIs(result, False)

    def test_is_owner(self, user=None):
        """
        Test for is_owner method defined in models.py
        """

        if user is None:
           self.user =  User.objects.first()
           self.assertEqual(User.objects.count(), 1)
           d_one =  Deck.objects.first()
           actual = d_one.is_owner(self.user)
           self.assertTrue(actual,'Swechchha')
