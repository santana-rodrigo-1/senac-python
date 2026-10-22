from django import forms
from .models import SolicitacaoOrcamento


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoOrcamento
        fields = [
            "elevador",
            "nome",
            "email",
            "telefone",
            "cidade",
            "pavimentos",
            "mensagem",
        ]
        widgets = {
            "elevador": forms.Select(attrs={"class": "form-select"}),
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Seu nome completo"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "voce@email.com"}
            ),
            "telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "(21) 90000-0000"}
            ),
            "cidade": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Rio de Janeiro"}
            ),
            "pavimentos": forms.NumberInput(
                attrs={"class": "form-control", "min": 1, "placeholder": "Ex.: 8"}
            ),
            "mensagem": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Conte detalhes do seu projeto...",
                }
            ),
        }
