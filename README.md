# FlashCourses_api
Repository for the FlashCourses API

## API Generic Views
**/flashcards/api/deck/create**  
**/flashcards/api/deck/retrieve/**`<pk>`  
**/flashcards/api/deck/list/**  
**/flashcards/api/deck/delete/**`<pk>`   
**/flashcards/api/deck/update/**`<pk>`   
**/flashcards/api/card/create**  
**/flashcards/api/card/retrieve/**`<pk>`   
**/flashcards/api/card/list/**  
**/flashcards/api/card/delete/**`<pk>`     
**/flashcards/api/card/update/**`<pk>`    

To access any of these URLs, navigate your browser to the server's address, followed by the URL. When we refer to `<pk>`, this always means that you must specify the Primary Key value, which is the model's UUID. You can retrieve these values with the /list/ URLs.

## Installation:
The following commands need to be run to install the necessary software for the REST API at the command prompt:

### Install REST Framework:
sudo pip install djangorestframework  
sudo pip install markdown  
sudo pip install django-filter  

### Install SimpleJWT:
sudo pip install djangorestframework_simplejwt  

### Install Memcached: (https://www.memcached.org/) 
sudo apt-get install libevent-dev  
sudo apt-get install memcached  
sudo pip install python-memcached  

#### Verify that Memcached is working:
telnet localhost 11211  
quit  

### Install CORS headers:
sudo pip install django-cors-headers  
