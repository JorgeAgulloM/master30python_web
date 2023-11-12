Create a virtual environment
- C:\Python311\python.exe -m venv env 

Activate env
- .\env\Scripts\activate   

Install Django
- pip install Django==4.2.7

Start proyect django
- django-admin startproject start_django 

Generar BBDD Sqlite3
- cd to new proyect path
- python manage.py migrate

Create Admin super user Django
- python manage.py createsuperuser 

Run Server
- python manage.py runserver

Generate app
- python manage.py startapp <name_of_app>

Migrate update db models
- python manage.py makemigrations