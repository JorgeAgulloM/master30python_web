from django.db import models

# Create your models here.
#
# ¡¡¡¡ Cada vez que se modifique los modelos, es necesario ejecutar una migración!!!!
#
# > python manage.py makemigrations
# Return like this:
"""
 Migrations for 'first_app':
  first_app\migrations\0001_initial.py
    - Create model Aricle
    - Create model Category
"""

# Ahora hay que crear el sql que se ejutará en el gestor de BBDD.
# Hay que pasarle al comando la app y la mogración que debe usar.
# > python manage.py sqlmigrate first_app 0001
# Retunr like this:
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

# Para terminar la migración
# > python manage.py migrate
"""
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, first_app, sessions
Running migrations:
  Applying first_app.0001_initial... OK
"""

class Article(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    image=models.ImageField(default='null', upload_to='articles')
    public=models.BooleanField(verbose_name='Is Public?') # verbose_name - Cambiará el nombre del parámetro en el panel de admin
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Updated')
    
    class Meta:
      verbose_name='Article'
      verbose_name_plural='Articles'
      ordering=['id'] # ordering=['-id'] Invertida
      
    def __str__(self) -> str: # ¡¡¡¡¡MAGIC METHOD!!!!!! Permite mostrar de una forma personalizada el valor del modelo, por ejemplo en admin
      
      if self.public:
        public='Public article'
      else:
        public='Private article'
      
      str_date = str(self.created_at)
      date=str_date.split()[0]
      
      return f'({public}) | Created at {date} | {self.title}'

class Category(models.Model):
    name=models.CharField(max_length=110)
    description=models.CharField(max_length=250)
    creted_at=models.DateField()

    class Meta:
      verbose_name='Category'
      verbose_name_plural='Categorys'
    