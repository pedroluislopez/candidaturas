# -*- encoding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from candidatos.forms import PasswordForm, CandidatoForm
from candidatos.models import Candidato

# Create your views here.
def index(request):
    import random
    r = random.Random()
    candidatos_sg = Candidato.objects.filter(secretario=True)
    if len(candidatos_sg) > 1:
        candidatos_sg = sorted(candidatos_sg, key=lambda L: r.random())
    candidatos_cc = Candidato.objects.filter(consejo=True)
    if len(candidatos_cc) > 1:
        candidatos_cc = sorted(candidatos_cc, key=lambda L: r.random())
    return render(request, 'index.html', {'candidatos_sg': candidatos_sg, 'candidatos_cc': candidatos_cc})
    
#def user_login(request):
#    if request.method == 'POST':
#        login_form = LoginForm(data=request.POST)
        
#        if login_form.is_valid():
#            username = login_form.cleaned_data['username']
#            password = login_form.cleaned_data['password']
#            user = authenticate(username=username, password=password)
    
#            if user:
#                if user.is_confirmed:
#                    if user.is_active:
#                        login(request, user)
#                        return redirect('index')
#                    else:
#                        login_form.add_error(None, "Tu cuenta está desactivada.")
#                else:
#                    login_form.add_error(None, "Tu cuenta no está confirmada.")
#            else:
#                login_form.add_error(None, "Usuario o contraseña inválidos")
#    else:
#        login_form = LoginForm()
#    
#    return render(request, 'login.html', {'login_form': login_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

#def register(request):
#    registered = False
#
#    if request.method == 'POST':
#        user_form = UserForm(data=request.POST)
#
#        if user_form.is_valid():
#            user = user_form.save()
#            user.set_password(user.password)
#            user.save()
#            send_mail('[Candidaturas Ahora Podemos Murcia]: Confirmar registro',
#                      u'Acceda al siguiente enlace para confirmar su cuenta: %s.' %\
#                        request.build_absolute_uri(user.confirmation_key).replace('register', 'confirm'),
#                      settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
#            registered = True
#            user_form = UserForm()
#    else:
#        user_form = UserForm()
#    
#    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})

def confirm(request, key):
    return render(request, 'confirm.html')

#def reset_password(request):
#    sent = False
#    
#    if request.method == 'POST':
#        reset_password_form = ResetPasswordForm(data=request.POST)

#        if reset_password_form.is_valid():
#            email = reset_password_form.cleaned_data['email']
#            new_password = User.objects.make_random_password(length=15)
#            user = User.objects.filter(email=email)[0]
#            user.set_password(new_password)
#            user.save()
#            send_mail('[Candidaturas Ahora Podemos Murcia]: Recuperar contraseña',
#                      u'Su nueva contraseña para el usuario "' + user.username + '" es: "' + new_password + '".',
#                      settings.EMAIL_HOST_USER, [email], fail_silently=False)
#            sent = True
#            reset_password_form = ResetPasswordForm()
#    else:
#        reset_password_form = ResetPasswordForm()
    
#    return render(request, 'reset_password.html', {'reset_password_form': reset_password_form, 'sent': sent})

@login_required
def user(request):
    success = False

    if request.method == 'POST':
        password_form = PasswordForm(data=request.POST)

        if password_form.is_valid():
            password = password_form.cleaned_data['password']
            request.user.set_password(password)
            request.user.save()
            user = authenticate(username=request.user.username, password=password)
            login(request, user)
            success = True
            password_form = PasswordForm()
    else:
        password_form = PasswordForm()
    
    return render(request, 'user.html', {'password_form': password_form, 'success': success})

@login_required
def candidatura(request):
    success = False
    instances = Candidato.objects.filter(user=request.user)
    if len(instances) > 0:
        instance = Candidato.objects.filter(user=request.user)[0]
    else:
        instance = Candidato()
    
    if request.method == 'POST':
        candidato_form = CandidatoForm(data=request.POST, files=request.FILES, instance=instance)

        if candidato_form.is_valid():
            nombre = candidato_form.cleaned_data['nombre']
            apellidos = candidato_form.cleaned_data['apellidos']
            request.user.first_name = nombre
            request.user.last_name = apellidos
            request.user.save()
            
            instance = candidato_form.save(commit=False)
            candidatura = candidato_form.cleaned_data['candidatura']
            instance.secretario = False
            instance.consejo = False
            if '1' in candidatura:
                instance.secretario = True
            if '2' in candidatura:
                instance.consejo = True
            instance.user = request.user
            instance.save()
            success = True
    else:
        candidatura = []
        if instance.secretario:
            candidatura.append('1')
        if instance.consejo:
            candidatura.append('2')
        candidato_form = CandidatoForm(
            initial={'nombre': request.user.first_name, 'apellidos': request.user.last_name, 'candidatura': candidatura},
            instance=instance)
    
    return render(request, 'candidatura.html', {'candidato_form': candidato_form, 'success': success, 'deleted': False})

@login_required
def borrar_candidatura(request):
    instances = Candidato.objects.filter(user=request.user)
    if len(instances) > 0:
        instances[0].delete()
    candidato_form = CandidatoForm(
        initial={'nombre': request.user.first_name, 'apellidos': request.user.last_name, 'candidatura': '0'},
        instance=Candidato())
    return render(request, 'candidatura.html', {'candidato_form': candidato_form, 'success': False, 'deleted': True})

def candidato(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    return render(request, 'candidato.html', {'c': candidato})

def about(request):
    return render(request, 'about.html', {})