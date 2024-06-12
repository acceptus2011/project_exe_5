from django import forms
from myspa.models import SpaUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Confirm password'}))

    class Meta:
        model = SpaUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))

    class Meta:
        model = SpaUser
        fields = ('username', 'password', 'email',)

