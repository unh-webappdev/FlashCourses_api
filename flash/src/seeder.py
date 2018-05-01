"""
Author: Bridget Franciscovich
Last Updated: April 2018
Relative File Path: flash/scr/seeder.py
Description: Generates fake data for the database
"""

#pip3 install faker
import time
import random
import uuid
from faker import Faker
fake = Faker()
from django.contrib.auth.models import User
from courses.models import Institution, Course
from flashcards.models import Deck, Card
from faker.providers import BaseProvider

def seed_users(num_entries, overwrite=False):
    """
    Explanation of function:Creates num_entries worth of new users
    Arguments: num_entries, overwrite=False
    Returns: The number of new fake users with print
    """
    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = first_name + "." + last_name + "@fakermail.com",
            username = first_name + last_name,
            password="password"
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Users: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_institution(num_entries, overwrite=False):
    """
    Explanation of function: Creates num_entries worth of new Institution
    Arguments: num_entries, overwrite=False
    Returns: The number of new fake institutions with print
    """
    count = 0
    for _ in range(num_entries):
        new_obj = Institution(
            ipeds = random.randrange(num_entries),
            institution_name = fake.company(),
            location = fake.address(),
            )
        new_obj.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Institutions: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_course(num_entries, overwrite=False):
    """
    Explanation of function: Creates num_entries worth of new Course
    Arguments: num_entries, overwrite=False
    Returns: The number of new fake courses with print
    """
    institution = list(Institution.objects.all())
    count = 0
    for _ in range(num_entries):
        new_obj = Course(
        course_title = fake.first_name(),
        course_id = random.randrange(100),
        parent_institution = random.choice(institution),
        course_description= fake.text(),
        )
        new_obj.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Courses: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_deck(num_entries, overwrite=False):
    """
    Explanation of function: Creates num_entries worth of new Deck
    Arguments: num_entries, overwrite=False
    Returns: The number of new fake decks with print function
    """
    user = list(User.objects.all())
    course = list(Course.objects.all())
    count = 0
    for _ in range(num_entries):
        new_obj = Deck(
            title = fake.first_name(),
            parent_user = random.choice(user),
            parent_course = random.choice(course),
            deck_description = fake.text(),
        )
        new_obj.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Decks: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_card(num_entries, overwrite=False):
    """
    Explanation of function: Creates num_entries worth of new Card
    Arguments: num_entries, overwrite=False
    Retuns: The number of new fake cards with print function
    """
    deck = list(Deck.objects.all())
    count = 0
    for _ in range(num_entries):
        new_obj = Card(
        parent_deck = random.choice(deck),
        front = fake.text(),
        back = fake.text(),
        )
        new_obj.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Cards: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_all(num_entries, overwrite=False):
    """
    Explanation of function: Runs all seeder functions
    Arguments: num_entries, overwrite=False
    Returns: The number of new fake users, institutions, courses, decks, and cards with print function
    """
    start_time = time.time()

    seed_users(num_entries=num_entries, overwrite=overwrite)
    seed_institution(num_entries=num_entries, overwrite=overwrite)
    seed_course(num_entries=num_entries, overwrite=overwrite)
    seed_deck(num_entries=num_entries, overwrite=overwrite)
    seed_card(num_entries=num_entries, overwrite=overwrite)

    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
