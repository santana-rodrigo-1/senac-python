from django import forms
from .models import Elevador


class ElevadorForm(forms.ModelForm):
    class Meta:
        model = Elevador
        fields = ["nome", "categoria", "preco", "estoque", "imagem", "ativo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "estoque": forms.NumberInput(attrs={"class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
