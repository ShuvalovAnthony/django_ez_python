from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Author, Country, Genre


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class AuthorForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label='Страна',
        widget=forms.Select(attrs={'class': 'form-select'})
        )
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        empty_label='Страна',
        widget=forms.Select(attrs={'class': 'form-select'})
        )

    class Meta:
        my_default_errors = {
            'required': 'This field is required',
            'invalid': 'Enter a valid value'
            }

        model = Author
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Никнейм',}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'hidden': ''}),
        }

# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
#     class Meta:
#         model = User
#         fields = ('username', 'password',)
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#         }
