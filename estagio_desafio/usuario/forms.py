from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'firstname', 'lastname', 'phone', 'joined_date']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado.")
        return email