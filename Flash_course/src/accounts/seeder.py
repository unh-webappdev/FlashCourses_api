# make sure to install faker...
# pip install faker
import time
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from models import UserPorfile

def seed_user_profile(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new user profiles
    """
    if overwrite:
        print("Overwriting Users")
        UserProfile.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        parent_user = fake.parent_user()
        parent_institution = fake.parent_institution()
        u = User.objects.create_user(
            parent_user = parent_user,
            parent_institution = parent_institution,
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Users: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

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

def seed_all(num_entries=10, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_user_profile(num_entries=num_entries, overwrite=overwrite)
    seed_users(num_entries=num_entries, overwrite=overwrite)
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
