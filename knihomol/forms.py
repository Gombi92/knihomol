from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Emailová adresa')
    password1 = forms.CharField(
        label="Heslo",
        widget=forms.PasswordInput,
        help_text="Nesmí být podobné uživatelskému jménu, musí mít minimálně 8 znaků."
    )
    password2 = forms.CharField(
        label="Potvrzení hesla",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Uživatelské jméno',
            'password1': 'Heslo',
            'password2': 'Potvrzení hesla',
        }
        help_texts = {
            'username': 'Vyžadováno. Max. 150 znaků. Povoleny jsou písmena, číslice a znaky @/./+/-/_',
        }
