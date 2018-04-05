# make sure to install faker...
# pip install faker
import time
import random
from faker import Faker
fake = Faker()
from django.contrib.auth.models import User
from accounts.models import UserProfile
from courses.models import Institution, Course
from flashcards.models import Deck, Card
from faker.providers import BaseProvider

#TODO: Ask Jon if we need the overwrite
#TODO: Jon used count = 1, why not 0?
#TODO: Ask Jon why we don't need course_id, it's not an auto field
#TODO: Ask Jon what flush=True means.
#TODO: Seed all function

def seed_users(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Users")
        Users.objects.all().delete()
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

def seed_institution(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new Institution
    """
    count = 0
    for _ in range(10):
        new_obj = Institution(
            ipeds = random.randrange(11),
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

def seed_course(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new Course
    """
    institution = list(Institution.objects.all())
    count = 0
    for _ in range(10):
        new_obj = Course(
        course_number = random.randrange(11),
        parent_institution = random.choice(institution),
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

def seed_deck(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new Deck
    """
    user = list(User.objects.all())
    course = list(Course.objects.all())
    count = 0
    for _ in range(10):
        new_obj = Deck(
        UUID = random.randrange(11),
        parent_user = random.choice(user),
        parent_course = random.choice(course),
        title = fake.first_name(),
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Decks: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_card(num_entries=10, overwrite=False):
    """
    Creates num_entries worth of new Card
    """
    user = list(Deck.objects.all())
    count = 0
    for _ in range(10):
        new_obj = Card(
        UUID = random.randrange(11),
        parent_deck = random.choice(deck),
        front = fake.text(),
        back = fake.text(),
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Cards: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()
