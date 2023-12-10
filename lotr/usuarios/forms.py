from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    # Cambia los labels y help_text según sea necesario
    username = forms.CharField(
        label=_('Nombre de usuario'),
    )
    email = forms.EmailField(label=_('Correo electrónico'))
    password1 = forms.CharField(
        label=_('Contraseña'),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_('Confirmación de contraseña'),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User  # Asegúrate de importar User desde django.contrib.auth.models
        fields = UserCreationForm.Meta.fields + ('email',)  # Añade 'email' a los campos del formulario
        labels = {
            'username': _('Nombre de usuario'),
            'email': _('Correo electrónico'),
        }
