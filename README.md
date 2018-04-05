# Documentation : FlashCourses

###  Installation Steps to run FlashCourses Locally

COMP-805 Django-FlashCourses group project
Configuration of the settings to run the project locally without posting private information on GitHub

***Settings-***
You will need to create your own settings_private.py file to be able to run the project correctly
with the common.py file

> - Create a new folder named: “settings”
> - Move common.py to the new settings file
> - Create a new file in the same folder and save it as **private_settings.py**

>  In your new private_settings.py you only need to have 2 items in this settings file
> - DEBUG = True
> - SECRET_KEY = os.environ.get     SECRET_KEY = os.environ.get "MADE_UP_CAPITAL_STRINGS’

### Installing the packages needed to run the project

Within your virtual environment you will need to install all the packages that are within the requirements.txt to run the code base locally

> Run from your terminal-
> **$ pip3 install -r requirements.txt**

> Check for errors
> **$ python3 manage.py check**

> Migrate the database
> **$ python3 manage.py makemigrations**
> **$ python3 manage.py migrate**
