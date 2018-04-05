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
#TODO: Ask Jon what flush=True means.

def seed_users(num_entries, overwrite=False):
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

def seed_institution(num_entries, overwrite=False):
    """
    Creates num_entries worth a new Institution
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
    Creates num_entries worth a new Course
    """
    institution = list(Institution.objects.all())
    count = 0
    for _ in range(num_entries):
        new_obj = Course(
        course_number = random.randrange(num_entries),
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

def seed_deck(num_entries, overwrite=False):
    """
    Creates num_entries worth a new Deck
    """
    user = list(User.objects.all())
    course = list(Course.objects.all())
    count = 0
    for _ in range(num_entries):
        new_obj = Deck(
        parent_user = random.choice(user),
        parent_course = random.choice(course),
        title = fake.first_name(),
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
    Creates num_entries worth of new Card
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
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
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
