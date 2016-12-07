# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#from password_reset.forms import PasswordRecoveryForm, PasswordResetForm
from .models import Usuario
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


class UsuarioModelForm(UserCreationForm):

	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'input-field-default'}))
	password2 = forms.CharField(label="Contraseña (Confirmar)", widget=forms.PasswordInput(attrs={'class':'input-field-default'}))

	class Meta():
		model  = Usuario
		fields = ['username', 'email' ]

		widgets = {
			'username'    				   : forms.TextInput(attrs={'class':'input-field-default'}),
			'password1'    				   : forms.TextInput(attrs={'class':'input-field-default'}),
			'password2'    				   : forms.TextInput(attrs={'class':'input-field-default'}),
			'email'	  					   : forms.EmailInput(attrs={'class':'input-field-default', 'placeholder':'example@example.com'}),
		
        }


class UsuarioAuthenticationForm(AuthenticationForm):
	username = forms.CharField(
	        max_length=255,
	        widget=forms.TextInput(attrs={
	        							  'class'		: 'input-field-default',
	        							 }
	        					  ),
	    )
	password = forms.CharField(
			label=("Password"),
			strip=False,
			widget=forms.PasswordInput(attrs={
				 							  'class': 'input-field-default',
											  })
			)
