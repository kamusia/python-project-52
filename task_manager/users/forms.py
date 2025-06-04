from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator
from .models import User


class BootstrapStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].validators = [MinLengthValidator(3)]

        self.fields['password1'].help_text = 'Минимум 3 символа'
        self.fields['password2'].help_text = 'Повторите пароль для подтверждения'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')
        help_texts = {
            'username': 'Минимум 3 символа. Только буквы, цифры и @/./+/-/_',
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
