from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class BootstrapStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Упрощенные требования к паролю
        self.fields['password1'].validators = [forms.MinLengthValidator(3)]
        self.fields['password2'].help_text = ''

        # Единое оформление для всех полей
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
        help_texts = {
            'username': 'Минимум 3 символа. Допустимы буквы, цифры и @/./+/-/_',
            'password1': 'Минимум 3 символа'
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
