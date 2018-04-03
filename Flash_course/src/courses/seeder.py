# make sure to install faker...
# pip install faker
import time
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from models import Institution, Course

def seed_institution(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new Institution
    """
    if overwrite:
        print("Overwriting Institution")
        Institution.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        name = fake.first_name()
        location = fake.location()
        i = Institution.objects.create_institution(
            name = name,
            location = location,
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Institution: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()

def seed_course(num_entries=10, overwrite=False)):
    """
    Creates num_entries worth a new Course
    """
    if overwrite:
        print("Overwriting Institution")
        Course.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        course_name = fake.course_name()
        parent_institution = fake.parent_institution()
        c = Course.objects.create_course(
            course_name = name,
            parent_institution = location,
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Course: {:.2f}%".format(num_entries, percent_complete),
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
    seed_institution(num_entries=num_entries, overwrite=overwrite)
    seed_course(num_entries=num_entries, overwrite=overwrite)
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
