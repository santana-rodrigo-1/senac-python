from django import forms
from .models import Elevador


class ElevadorForm(forms.ModelForm):
    class Meta:
        model = Elevador
        fields = ["nome", "categoria", "preco", "estoque", "imagem", "ativo"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-secondary"}
            ),
            "categoria": forms.Select(
                attrs={"class": "form-select bg-dark text-white border-secondary"}
            ),
            "preco": forms.NumberInput(
                attrs={"class": "form-control bg-dark text-white border-secondary"}
            ),
            "estoque": forms.NumberInput(
                attrs={"class": "form-control bg-dark text-white border-secondary"}
            ),
            "imagem": forms.ClearableFileInput(
                attrs={"class": "form-control bg-dark text-white border-secondary"}
            ),
        }
