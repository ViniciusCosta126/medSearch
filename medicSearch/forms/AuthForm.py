from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    ROLE_CHOICE = (
        (2, 'Medico'),
        (3, 'Paciente')
    )
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.CharField(required=True, widget=forms.Select(
        attrs={'class': 'form-control'}, choices=ROLE_CHOICE))
