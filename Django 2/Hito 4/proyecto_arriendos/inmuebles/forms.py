from django import forms
from .models import Inmueble

class FormularioInmueble(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['titulo', 'descripcion', 'tipo', 'precio', 'region', 'comuna', 'direccion', 'disponible']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }