import re

from django import forms
from django.core.exceptions import ValidationError

from .models import SolicitacaoOrcamento

# ----------------------------------------------------------------------------
# Normalização e validação de telefone brasileiro
# ----------------------------------------------------------------------------


def _digitos(valor: str) -> str:
    return re.sub(r"\D", "", valor or "")


def normalizar_telefone_br(valor: str) -> str:
    """
    Aceita:
        (21) 90000-0000
        21 90000-0000
        21900000000
        +55 21 90000-0000
        (21) 3000-1234       (fixo)
    Retorna sempre:
        "(21) 90000-0000"    (celular - 11 dígitos)
        "(21) 3000-1234"     (fixo    - 10 dígitos)
    Levanta ValidationError se não for um telefone brasileiro válido.
    """
    digitos = _digitos(valor)

    # remove +55 se vier colado
    if digitos.startswith("55") and len(digitos) > 11:
        digitos = digitos[2:]

    if len(digitos) not in (10, 11):
        raise ValidationError(
            "Informe um telefone com DDD (10 ou 11 dígitos). " "Ex.: (21) 90000-0000."
        )

    ddd = int(digitos[:2])
    if not 11 <= ddd <= 99:
        raise ValidationError("DDD inválido. Use um DDD entre 11 e 99.")

    if len(digitos) == 11:
        # celular: 9XXXX-XXXX
        if digitos[2] != "9":
            raise ValidationError(
                "Celular deve começar com 9 após o DDD. Ex.: (21) 90000-0000."
            )
        return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"

    # fixo: XXXX-XXXX começando com 2, 3, 4 ou 5
    if digitos[2] not in "2345":
        raise ValidationError(
            "Telefone fixo deve começar com 2, 3, 4 ou 5 após o DDD. "
            "Ex.: (21) 3000-1234."
        )
    return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"


# ----------------------------------------------------------------------------
# Formulário de orçamento
# ----------------------------------------------------------------------------


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
            "nome": forms.TextInput(attrs={"placeholder": "Seu nome completo"}),
            "email": forms.EmailInput(attrs={"placeholder": "voce@email.com"}),
            "telefone": forms.TextInput(
                attrs={
                    "placeholder": "(21) 90000-0000",
                    "inputmode": "tel",
                    "autocomplete": "tel",
                }
            ),
            "cidade": forms.TextInput(attrs={"placeholder": "Rio de Janeiro"}),
            "pavimentos": forms.NumberInput(attrs={"min": 1, "placeholder": "Ex.: 8"}),
            "mensagem": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Conte detalhes do seu projeto...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # aplica a classe CSS padrão de cada campo
        for campo in self.fields.values():
            eh_select = isinstance(campo.widget, forms.Select)
            classe = "form-select" if eh_select else "form-control"
            atuais = campo.widget.attrs.get("class", "")
            if classe not in atuais:
                campo.widget.attrs["class"] = f"{atuais} {classe}".strip()

        self.fields["elevador"].empty_label = (
            "Orçamento geral (nenhum modelo específico)"
        )

    def is_valid(self):
        ok = super().is_valid()
        if not ok:
            for nome in self.errors:
                if nome in self.fields:
                    classes = self.fields[nome].widget.attrs.get("class", "")
                    if "is-invalid" not in classes:
                        self.fields[nome].widget.attrs["class"] = (
                            classes + " is-invalid"
                        ).strip()
        return ok

    # ---- validações específicas ----

    def clean_nome(self):
        nome = (self.cleaned_data.get("nome") or "").strip()
        if len(nome) < 3:
            raise ValidationError("Informe seu nome completo (mínimo 3 caracteres).")
        if not re.search(r"[A-Za-zÀ-ÿ]", nome):
            raise ValidationError("O nome precisa ter pelo menos uma letra.")
        return nome

    def clean_telefone(self):
        return normalizar_telefone_br(self.cleaned_data.get("telefone", ""))

    def clean_cidade(self):
        cidade = (self.cleaned_data.get("cidade") or "").strip()
        if len(cidade) < 2:
            raise ValidationError("Informe a cidade.")
        return cidade

    def clean_pavimentos(self):
        pav = self.cleaned_data.get("pavimentos")
        if pav is None or pav < 1:
            raise ValidationError("Informe o número de pavimentos (mínimo 1).")
        if pav > 200:
            raise ValidationError("Valor muito alto. Verifique o número de pavimentos.")
        return pav

    def clean_mensagem(self):
        msg = (self.cleaned_data.get("mensagem") or "").strip()
        if msg and len(msg) < 10:
            raise ValidationError(
                "Se for escrever uma mensagem, use pelo menos 10 caracteres."
            )
        return msg
