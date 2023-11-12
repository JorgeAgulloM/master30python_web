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

### Create models:

#### ¡¡¡¡ Cada vez que se modifique los modelos, es necesario ejecutar una migración!!!!

#### > python manage.py makemigrations
#### Return like this:
    """
        Migrations for 'first_app':
        first_app\migrations\0001_initial.py
            - Create model Aricle
            - Create model Category
    """

#### Ahora hay que crear el sql que se ejutará en el gestor de BBDD.
#### Hay que pasarle al comando la app y la mogración que debe usar.
#### > python manage.py sqlmigrate first_app 0001
#### Retunr like this:
    """
        BEGIN;
        --
        -- Create model Aricle
        --
        CREATE TABLE "first_app_aricle" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "public" bool NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
        --
        -- Create model Category
        --
        CREATE TABLE "first_app_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "description" varchar(250) NOT NULL, "creted_at" date NOT NULL);   
        COMMIT;
    """

#### Para terminar la migración
#### > python manage.py migrate
    """
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, first_app, sessions
        Running migrations:
        Applying first_app.0001_initial... OK
    """