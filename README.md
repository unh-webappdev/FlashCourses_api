# Documentation : FlashCourses
##  Author: Justin Kroh
##  Last Updated: September 2018
##  Description: Installation Steps to run FlashCourses Locally
##  Relative File Path: /README.md

***Settings Configuration-***
* To run the project locally without posting private information on GitHub

* You will need to create your own settings_private.py file to be able to run the project correctly
with the common.py file in the same directory as common.py

>  In your new settings_private.py you only need to have 2 items in this settings file
> - DEBUG = True
> - SECRET_KEY = "MADE_UP_CAPITAL_STRINGS’

### Installing the packages needed to run the project

Within your virtual environment you will need to install all the packages
> Run from your terminal-
> **$ pip(3) install djangorestframework
  pip(3) install djangorestframework_simplejwt
  pip(3) install django-cors-headers

  

> Check for errors
> **$ python3 manage.py check**

> Migrate the database
> - **$ python3 manage.py makemigrations**
> - **$ python3 manage.py migrate**
