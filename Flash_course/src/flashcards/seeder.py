# make sure to install faker...
# pip install faker
import time
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from models import Deck, Card

def seed_deck(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new Deck
    """
    if overwrite:
        print("Overwriting Institution")
        Deck.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        parent_user = fake.parent_user()
        parent_course = fake.parent_course()
        title = title()
        d = Institution.objects.create_deck(
            parent_user = parent_user,
            parent_course = parent_course,
            title = title,
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Deck: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_card(num_entries=10, overwrite=False)):
    """
    Creates num_entries worth a new Card
    """
    if overwrite:
        print("Overwriting Institution")
        Card.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        deck = fake.deck()
        front = fake.front()
        back= fake.back()
        c = Card.objects.create_card(
            deck = deck,
            front = front,
            back = back,
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Card: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_all(num_entries=10, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_deck(num_entries=num_entries, overwrite=overwrite)
    seed_card(num_entries=num_entries, overwrite=overwrite)
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
