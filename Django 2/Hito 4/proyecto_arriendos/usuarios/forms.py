from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arrendatario, Arrendador

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormularioArrendatario(forms.ModelForm):
    class Meta:
        model = Arrendatario
        fields = ['nombre', 'rut', 'direccion', 'telefono', 'email']

class FormularioArrendador(forms.ModelForm):
    class Meta:
        model = Arrendador
        fields = ['nombre', 'rut', 'direccion', 'telefono', 'email']