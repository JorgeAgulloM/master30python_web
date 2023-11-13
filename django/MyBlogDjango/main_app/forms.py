from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User # Le decimos a la clase sobre que modelo vamos a construir nuestro fomulario
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] # Le decimos que objetos queremos que se visualicen en el formulario