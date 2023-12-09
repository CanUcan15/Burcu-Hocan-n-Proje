from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import COUNTRIES, UserProfile

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True, label="Kullanıcı Adı", widget=forms.TextInput())
    password1 = forms.CharField(required=True, label="Şifre", widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, label="Şifrenizi Onaylayın", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    username = forms.CharField(max_length=25, required=True, label="Kullanıcı Adı", widget=forms.TextInput())
    password = forms.CharField(required=True, label="Şifre", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
	'''
	Basic model-form for our user profile
	'''
	avatar = forms.ImageField(required=False)
	telephone = forms.CharField(max_length=255, required=False, label="Telefon Numarası", widget=forms.TextInput())
	address = forms.CharField(max_length=255, required=False, label="Adres", widget=forms.TextInput())
	town = forms.CharField(max_length=100, required=False, label="Şehir", widget=forms.TextInput())
	county = forms.CharField(max_length=100, required=False, label="İlçe", widget=forms.TextInput())
	post_code = forms.CharField(max_length=8, required=False, label="Posta Kodu", widget=forms.TextInput())
	country = forms.CharField(max_length=100, required=False, label="Ülke", widget=forms.Select(choices=COUNTRIES))
	
	class Meta:
		model = UserProfile
		fields = ('avatar','telephone', 'address', 'town', 'county', 'post_code', 'country')


class UserAlterationForm(forms.ModelForm):
	'''
	Basic model-form for our user
	'''
	first_name = forms.CharField(max_length=150, required=True, label="İsim", widget=forms.TextInput())
	last_name = forms.CharField(max_length=150, required=True,label="Soyisim", widget=forms.TextInput())
	email = forms.EmailField(max_length=254, required=True, label="E-Posta", widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')