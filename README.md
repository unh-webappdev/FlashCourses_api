# Documentation : FlashCourses
##  Author: George Harvey
##  Last Updated: September 2018
##  Description: Installation Steps to run FlashCourses Locally
##  Relative File Path: /README.md


***Set Up Git Environemnt***
* cd workspace/${SOMEPROJECT}/
* Clone the Repo: git clone -o upstream https://github.com/unh-webappdev/FlashCourses_api.git
* Connect to your own remote origin: git remote add origin <SOME GIT REPO URL> 
* Verify Setup: cd workspace/${SOMEPROJECT}/; git remote -v
* You should see a push and pull for upstream and origin

***Create a New venv***
* cd workspace/venv/
* virtenv <name of new venv>

***Activate venv***
* source workspace/venv/<<name of new venv>/bin/activate

***Install Dependencies***
* cd FlashCourses_api/flash/docs/
* pip install -r requirements.txt

***Check Project***
* cd FlashCourses_api/flash/src/
* python manage.py check
* If you recieve the error "django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty." follow the following steps if not skip to makemigrations
* Creat a new file FlashCourses_api/flash/src/FlashCourses/settings/settings_private.py
* Add in the following two lines:
*		DEBUG = True
*		SECRET_KEY = "SOME_RANDOM_VALUE"

***Make Migrations***
* cd FlashCourses_api/flash/src/
* python manage.py makemigrations

***Migrate***
* cd FlashCourses_api/flash/src/
* python manage.py migrate

***Run Server***
* cd FlashCourses_api/flash/src/
* python manage.py runserver

