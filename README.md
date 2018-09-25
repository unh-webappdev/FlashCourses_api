# Documentation : FlashCourses
##  Author: Justin Kroh
##  Last Updated: September 2018
##  Description: Installation Steps to run FlashCourses Locally
##  Relative File Path: /README.md

Installing Django

Install Latest Statble version of python (3.6.6)
Install Virtual Enviroments (pip install virtualenv)
Create a folder call Venv and create a new virtual enviroment with python (3.6.6) (command depends on machine / google it)
Activate your Venv by going to either the Bin, lib, or scripts folder and typing source Activate, ./activate.ps1 on posh.
Create a folder to hold your django project for FlashCourses (project)
Clone the reposity with git clone into the project folder.
Fork the project to your github profile online
Set your cloned repo to be the origin of your forked repo. Git init, git origin, git status, git add and git push if neccessary.
Then perform the folling steps in the Django app.



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
