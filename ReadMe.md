## 
## Installation du projet 
 
Installer python et django (dans la rubrique Installation de l'URL) :   
Installer le projet :  
   
	git clone https://github.com/florianva/WebServicePython.git 
 
Installer python : 
 
	https://www.python.org/downloads/ 
 
Installer django (dans la rubrique Installation de l'URL) :   
   
 	pip install Django 
  	https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/creez-vos-applications-web-avec-django 
 
Installer CORS pour faire la requête ajax: 
   
  	pip install django-cors-headers 
 
Installer sqlite :  
 
  	https://www.sqlite.org/ 

Installer Django REST framework :
  
	http://www.django-rest-framework.org/#installation 
 
Pour lancer le projet (à la racine du projet) : 
 
	python server/manage.py runserver   
 
## Installation Client 
 
Installer nodejs: 
   
 	https://openclassrooms.com/courses/des-applications-ultra-rapides-avec-node-js/installer-node-js   
 
Installer bower : 
   
  	https://bower.io/ 
 
Pour lancer le client (dans le dossier client):  
 
  	node client/bin/www   
 
Pour lancer la requête sur postman: 
   
  	http://localhost:8000 
 
Pour lancer le client depuis un navigateur: 
 
  	http://localhost:3000 
	
 ## Documentation
 
  ### GET http://localhost/books/
  return json data with all books
 
  ### GET http://localhost/books/ID
  return json data with the detail of the book number ID
 
  ### POST http://localhost/books/
  create a book with data send in the body request. 
  Exemple of data : 
  ```
 {"name": "star wars", "category": "science-fiction"}
  ```
 
  ### PUT http://localhost/books/ID
  update the book ID with data send in the body request. 
  Exemple of data : 
  ```
 {"name": "wars des étoiles", "category": "science-pas-fiction"}
  ```
  
  ### GET http://localhost/members/
  return json data with all members
 
  ### GET http://localhost/members/ID
  return json data with the detail of the member number ID
 
  ### POST http://localhost/members/
  create a member with data send in the body request. 
  Exemple of data : 
  ```
{"idBook": "2", "name":"kirikou le petit"}
  ```
 
  ### PUT http://localhost/members/ID
  update the members ID with data send in the body request. 
  Exemple of data : 
  ```
{"idBook": "2", "name":"kirikou le grand"}
  ```
 

 
 
 
