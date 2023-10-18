from django.shortcuts import render, redirect, get_object_or_404
from medicSearch.models import Profile
from django.core.paginator import Paginator
from medicSearch.forms.UserProfieForm import UserProfileForm, UserForm


def list_profile_view(request, id=None):
    """Função para fazer a listagem de perfil"""
    profile = None
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')

    favorites = profile.show_favorites()
    ratings = profile.show_ratings()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings
    }

    return render(request, template_name='profile/profile.html', context=context, status=200)


def edit_profile(request):
    """Função para edicao dde um perfil"""
    profile = get_object_or_404(Profile, user=request.user)

    emailUnused = True
    message = None
    if request.method == 'POST':
        profileForm = UserProfileForm(
            request.POST, request.FILES, instance=profile)
        userForm = UserForm(request.POST, instance=request.user)

        verifyEmail = Profile.objects.filter(
            user__email=request.POST['email']).exclude(user__id=request.user.id).firts()
        emailUnused = verifyEmail is None

    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()
        message = {'type':	'success',	'text':	'Dados	atualizados com sucesso'}
    else:
        if request.method == 'POST':
            if emailUnused:
                message = {'type':	'danger',	'text':	'Dados invalidos'}
            else:
                message = {'type':	'warning',	'text':	'Email ja utilizado por outro usuario'}
    context = {
        'profileForm': profileForm,
        'userForm': userForm
    }
    return render(request, template_name='user/profile.html', context=context, status=200)
