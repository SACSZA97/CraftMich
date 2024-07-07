from django import forms
from .models import Articulos

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['imagen', 'producto', 'precio', 'descripcion']
        
from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'usuario',
            'nombre',
            'email',
            'password',
            'fecha',
            'roles',
        ]
