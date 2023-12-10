from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    # Cambia los labels y help_text según sea necesario
    username = forms.CharField(
        label=_('Nombre de usuario'),
        help_text=_(
            '<br><p class="textoRegistro"> 150 caracteres como máximo. Solo letras, dígitos y @/./+/-/_.</p>'
        )
    )
    email = forms.EmailField(label=_('Correo electrónico'))
    password1 = forms.CharField(
        label=_('Contraseña'),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_(
            '<br><p class="textoRegistro">Tu contraseña debe cumplir con los siguientes requisitos:<br>'
            '- Al menos 8 caracteres<br>'
            '- No demasiado similar a tu otra información personal<br>'
            '- No una contraseña comúnmente utilizada<br>'
            '- No completamente numérica</p>'
        ),
    )
    password2 = forms.CharField(
        label=_('Confirmación de contraseña'),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_('<br><p class="textoRegistro">Ingresa la misma contraseña que antes, para verificación.</p>'),
    )

    class Meta:
        model = User  # Asegúrate de importar User desde django.contrib.auth.models
        fields = UserCreationForm.Meta.fields + ('email',)  # Añade 'email' a los campos del formulario
        labels = {
            'username': _('Nombre de usuario'),
            'email': _('Correo electrónico'),
        }
