from django import forms
from loja.models import Produto

class ProdutoForm(forms.modelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","ativo"]
        widget = {
            "nome": forms.TextInput(attrs= {"class":"form-control"}),
            "preco": forms.NumberInput(attrs= {"class":"form-control","step":"0.01"}),
            "ativo": forms.BooleanInput(attrs= {"class":"form-control"})
        }