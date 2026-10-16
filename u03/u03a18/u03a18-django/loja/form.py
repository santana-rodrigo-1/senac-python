from django import forms
from loja.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","ativo"]
        widgets = {
            "nome": forms.TextInput(attrs= {"class":"form-control"}),
            "preco": forms.NumberInput(attrs= {"class":"form-control","step":"0.01"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"})
            # "ativo": forms.BooleanInput(attrs= {"class":"form-control"})
        }