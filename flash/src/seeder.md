# Documentation : FlashCourses Database Seeder

University of New Hampshire, Manchester  
COMP 805 - Web Application Development  
FlashCourses Group Project  

**seeder.md by Bridget Franciscovich**  
Last Updated: 4/24/2018  

##  Steps to run seeder.py

### Open a bash shell:
> - **$ cd projectname**

## Activate a virtual environment:
> You must be in the directory with your virtual environment
> - **$ source venv/bin/activate 		#activates your a virtual environment in that path**

## Configure a virtual environment:
> - **$ cd flash**
> - **$ cd docs				#use ls command to see the requirements.txt folder**
> - **$$ pip3 install -r requirements.txt	#installs all needed applications for the project; faker is needed**

## Create a superuser:
> - **$ cd flash**
> - **$ cd src**
> - **$ python3 manage.py createsuperuser		#creates a super user for your local repository
   Username (leave blank to use yourname):
   Email address:
   Password:
   Password (again):
   Superuser created successfully.**

## Open a Python shell:
> - **$ cd flash**
> - **$ cd src**
> - **$ python3 manage.py shell		#Manage.py first sets the default environment to be used
                                  #Shell launches a Django environment in a Python shell**

## Run seeder.py:
> - **>>> import seeder			#imports seeder.py**
> - **>>> seeder.seed_all(num_entries)	#change num_entries to the number of fake entries wanted**

## Seeing the fake data:
> - **$ cd flash**
> - **$ cd src**
> - **$ python3 manage.py runserver				#runs your local server**
> - **On a browser, go to http://localhost:8000/admin	#or any port specified**
> - Log in using super user credentials
> - Click on models in the admin panel

## Helpful Information:
> - seed_users and seed_intitution can be run at any time.
> - seed_course can be run only if seed_institution has been run at least once on your local database.
> - seed_deck can be run only if seed_user and seed_course have been run at least once on your local database.
> - seed_card can be run only if seed_deck has been run at least once on your local database.
> - You should have the most updated project on the master to successfully run the seeder.
