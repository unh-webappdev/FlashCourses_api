# Documentation : FlashCourses

###  Installation Steps to run FlashCourses Locally

COMP-805 Django-FlashCourses group project
Configuration of the settings to run the project locally without posting private information on GitHub

***Settings-***
You will need to create your own settings_private.py file to be able to run the project correctly
with the common.py file

> - Create a new folder named: “settings”
> - Move common.py to the new settings file
> - Copy and paste the contents of common.py settings into a new file save that file as **private_settings.py**

In your newly created **private_settings.py**
>  **Replace**
>  SECRET_KEY = os.environ.get('SECRET_KEY')
> **To**
> SECRET_KEY = os.environ.get "MADE_UP_CAPITAL_STRINGS’
> **Replace**
> DEBUG = False
> **To**
> DEBUG = True

>  Remove the remaining code from new private_settings.py
     You should only have 2 items now in the file
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
