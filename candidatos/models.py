# -*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


class User(SimpleEmailConfirmationUserMixin, AbstractUser):
    pass

# Create your models here.
class Candidato(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    nif = models.CharField('NIF', max_length=9, unique=True)
    telefono = models.CharField('Teléfono', max_length=9)
    imagen = models.ImageField('Imagen', upload_to='profile_images', blank=True)
    secretario = models.BooleanField('Secretario General', default=False)
    consejo = models.BooleanField('Consejo Ciudadano', default=False)
    biografia = models.TextField('Biografía', max_length=2000, blank=True)
    motivacion = models.TextField('Motivación', max_length=2000, blank=True)
    youtube = models.CharField('Vídeo youtube', max_length=50, blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def get_imagen(self):
        if not self.imagen:
            return 'http://placehold.it/200x200'
        return self.imagen.url
    
    def get_candidatura(self):
        if self.secretario and self.consejo:
            return 'Secretaría general y Consejo ciudadano'
        elif self.secretario:
            return 'Secretaría general'
        elif self.consejo:
            return 'Consejo ciudadano'
        else:
            return ''
        
    def get_youtube_src(self):
        if self.youtube:
            return self.youtube\
                .replace('http:', '')\
                .replace('https:', '')\
                .replace('watch?v=', 'embed/')
        return ''
    
    def get_resumen(self):
        return (self.motivacion[:500] + ' ...') if len(self.motivacion) > 500 else self.motivacion
    