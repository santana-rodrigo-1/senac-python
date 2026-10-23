import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import SolicitacaoOrcamento, Elevador, Pedido

# ----------------------------------------------------------------------------
# Validação de telefone BR
# ----------------------------------------------------------------------------


def _digitos(valor: str) -> str:
    return re.sub(r"\D", "", valor or "")


def normalizar_telefone_br(valor: str) -> str:
    digitos = _digitos(valor)

    if digitos.startswith("55") and len(digitos) > 11:
        digitos = digitos[2:]

    if len(digitos) not in (10, 11):
        raise ValidationError(
            "Informe um telefone com DDD (10 ou 11 dígitos). Ex.: (21) 90000-0000."
        )

    ddd = int(digitos[:2])
    if not 11 <= ddd <= 99:
        raise ValidationError("DDD inválido. Use um DDD entre 11 e 99.")

    if len(digitos) == 11:
        if digitos[2] != "9":
            raise ValidationError(
                "Celular deve começar com 9 após o DDD. Ex.: (21) 90000-0000."
            )
        return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"

    if digitos[2] not in "2345":
        raise ValidationError(
            "Telefone fixo deve começar com 2, 3, 4 ou 5 após o DDD. Ex.: (21) 3000-1234."
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


# ----------------------------------------------------------------------------
# Formulário do painel de elevadores (staff)
# ----------------------------------------------------------------------------


class ElevadorForm(forms.ModelForm):
    class Meta:
        model = Elevador
        fields = [
            "nome", "slug", "tipo", "categoria",
            "descricao_curta", "descricao",
            "capacidade_kg", "velocidade", "pavimentos",
            "preco",  # <-- ADICIONADO AQUI
            "imagem", "imagem_secundaria",
            "destaque", "ativo",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "preenchido automaticamente se vazio",
            }),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "descricao_curta": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Uma frase (máx. 200 caracteres)",
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control", "rows": 5,
                "placeholder": "Descrição completa do elevador",
            }),
            "capacidade_kg": forms.NumberInput(attrs={"class": "form-control"}),
            "velocidade": forms.NumberInput(attrs={
                "class": "form-control", "step": "0.01",
            }),
            "pavimentos": forms.NumberInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={
                "class": "form-control", "step": "0.01", "placeholder": "Ex: 45000.00"
            }), # <-- ADICIONADO AQUI
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "imagem_secundaria": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_slug(self):
        slug = (self.cleaned_data.get("slug") or "").strip()
        if not slug:
            slug = slugify(self.cleaned_data.get("nome", ""))
        return slug


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["nome", "email", "telefone", "endereco"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome completo",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "voce@email.com",
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(21) 90000-0000",
                    "inputmode": "tel",
                }
            ),
            "endereco": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Rua, número, complemento, bairro, cidade/UF, CEP",
                }
            ),
        }

    def clean_telefone(self):
        return normalizar_telefone_br(self.cleaned_data.get("telefone", ""))
