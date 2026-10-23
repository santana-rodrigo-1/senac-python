from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

# Formulário para Editar Perfil (Nome, Email, Tel, Endereço)
class UserUpdateForm(forms.ModelForm):
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(21) 90000-0000'}),
        required=False,
        label='Telefone'
    )
    endereco = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Rua, número, complemento, bairro, cidade/UF, CEP'}),
        required=False,
        label='Endereço de Entrega'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
        }
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'perfil'):
            self.fields['telefone'].initial = self.instance.perfil.telefone
            self.fields['endereco'].initial = self.instance.perfil.endereco

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            perfil, created = Perfil.objects.get_or_create(usuario=user)
            perfil.telefone = self.cleaned_data.get('telefone')
            perfil.endereco = self.cleaned_data.get('endereco')
            perfil.save()
        return user

# Novo Formulário de Cadastro com Checkbox de Termos
class CustomUserCreationForm(UserCreationForm):
    aceite_termos = forms.BooleanField(
        required=True,
        label="Li e aceito os termos de uso e a política de privacidade.",
        error_messages={'required': 'Você precisa aceitar os termos para se cadastrar.'},
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class ContatoForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'})
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Como podemos ajudar?'})
    )
