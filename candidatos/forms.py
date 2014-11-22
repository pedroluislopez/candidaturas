# -*- encoding: utf-8 -*-

from django import forms

from candidatos.models import Candidato, User

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput({'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput({'class': 'form-control'}))

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Usuario', help_text='30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.', widget=forms.TextInput({'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput({'class': 'form-control'}))
    password = forms.CharField(label='Clave', help_text='8 caracteres como mínimo', min_length=8, widget=forms.PasswordInput({'class': 'form-control'}))
    password2 = forms.CharField(label='Repite la clave', widget=forms.PasswordInput({'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
    
        if not password2:
            raise forms.ValidationError("Debes confirmar tu password")
        if password != password2:
            raise forms.ValidationError("Las passwords no coinciden")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)
        if len(users) > 0:
            raise forms.ValidationError("Email ya dado de alta")
        return email

class ResetPasswordForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput({'class': 'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)
        if len(users) == 0:
            raise forms.ValidationError("El email introducido no existe")
        return email
    
class PasswordForm(forms.Form):
    password = forms.CharField(label='Clave', help_text='8 caracteres como mínimo', min_length=8, widget=forms.PasswordInput({'class': 'form-control'}))
    password2 = forms.CharField(label='Repite la clave', widget=forms.PasswordInput({'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
    
        if not password2:
            raise forms.ValidationError("Debes confirmar tu password")
        if password != password2:
            raise forms.ValidationError("Las passwords no coinciden")
        return password2
    
class CandidatoForm(forms.ModelForm):
    id = forms.HiddenInput
    CHOICES = (('1', 'Secretario General',), ('2', 'Consejo ciudadano',))
    candidatura = forms.MultipleChoiceField(required=True, widget=forms.SelectMultiple({'class': 'form-control'}), choices=CHOICES)
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput({'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', widget=forms.TextInput({'class': 'form-control'}))
    nif = forms.CharField(label='NIF', widget=forms.TextInput({'class': 'form-control'}))
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput({'class': 'form-control'}))
    imagen = forms.ImageField(label='Imagen', required=False)
    biografia = forms.CharField(label='Biografía', widget=forms.Textarea({'class': 'form-control'}))
    motivacion = forms.CharField(label='Motivación', widget=forms.Textarea({'class': 'form-control'}))
    youtube = forms.CharField(label='Vídeo de youtube', required=False, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'https://www.youtube.com/watch?v=AXo1axHT0lc'}))
    
    class Meta:
        model = Candidato
        fields = ('id', 'candidatura', 'nombre', 'apellidos', 'nif', 'telefono', 'imagen', 'biografia', 'motivacion', 'youtube')
    