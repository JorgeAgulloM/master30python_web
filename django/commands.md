Create a virtual environment
- C:\Python311\python.exe -m venv env 

Activate env
- .\env\Scripts\activate   

Install Django
- pip install Django==4.2.7

Start proyect django
- django-admin startproject start_django 

Generar BBDD Sqlite3
- python manage.py migrate

Run Server
- python manage.py runserver