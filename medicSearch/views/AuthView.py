from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from medicSearch.forms.AuthForm import LoginForm, RegisterForm
from medicSearch.models import Profile


def login_view(request):
    """Funcao de login no sistema"""
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect(to='/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')

                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect(to='/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuarios incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)


def register_view(request):
    '''Funcao de registro'''

    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect(to='/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():

            verifyUSerName = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUSerName is not None:
                message = {'type': 'danger',
                           'text': 'Já existe um usuário com este username!'}

            elif verifyEmail is not None:
                message = {'type': 'danger',
                           'text': 'Já existe um usuário com este email!'}

            else:
                user = User.objects.create_user(username, email, password)

                profile = Profile.objects.filter(id=user.id).first()
                profile.role = role
                profile.save()
                if user is not None:
                    message = {'type': 'success',
                               'text': 'Conta criada com sucesso!'}
                else:
                    message = {'type': 'danger',
                               'text': 'Um erro aconteceu ao tentar criar o usuário!'}

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)


def logout_view(request):
    logout(request)
    return redirect('/login')
