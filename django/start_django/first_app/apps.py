from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_app'
    verbose_name = 'My First App with Django' # verbose_name - Cambiará el nombre del parámetro en el panel de admin
