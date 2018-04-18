# Documentation : FlashCourses API

University of New Hampshire, Manchester  
COMP 805 - Advanced Web Development  
FlashCourses Group Project  

**api.md by Patrick R. McElhiney**  
Last Updated: 4/14/2018  

###  Installation Steps to run FlashCourses API Locally

Configuration settings to run the APIs locally

***api_settings.py***  
Do not modify api_settings.py, as it contains all of the settings that are required to run the repository both locally and on the server.

These settings include the following:
> - JWT Authentication - used to authenticate valid users.
> - Default Renderer - how the API is displayed in the web browser.
> - Throttling - used to protect the server from hacking and DDoS attacks.
> - CORS Headers - used to allow cross-site scripting.
> - Caching - used to speed up the web server. This is disabled in the local copy.



### Installing the packages needed to run the project

Within your virtual environment you will need to install all the packages that are within the requirements.txt to run the code base locally

> Run from your terminal
> - **$ pip3 install -r requirements.txt**

> Check for errors
> - **$ python3 manage.py check**

> Synchronize Apps with Database
> - **$ python manage.py migrate --run-syncdb**  
> 
**If you are unable to load requirements.txt as shown above, you may use the following commands to install the packages:**

> Install Django REST Framework
> - **$ sudo pip install djangorestframework**
> - **$ sudo pip install markdown**
> - **$ sudo pip install django-filter**

> Install SimpleJWT
> - **$ sudo pip install djangorestframework_simplejwt**

> Install Memcached
> - **$ sudo apt-get install libevent-dev**
> - **$ sudo apt-get install memcached**
> - **$ sudo pip install python-memcached**

> Verify that Memcached is working properly
> - **$ telnet localhost 11211**
> - **$ quit**

> Install CORS headers
> - **$ sudo pip install django-cors-headers**
