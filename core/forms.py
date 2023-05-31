from django import forms

from . import models


class RepoForm(forms.ModelForm):

    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    caminho = forms.CharField(
        label="Caminho",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    link = forms.CharField(
        label="Link",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    responsavel_uso = forms.CharField(
        label="Responsável pela Autorização de Uso",
        widget=forms.Select(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    publico_alvo = forms.CharField(
        label="Público-alvo",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = models.Repo
        fields = [
            "tipo_entidade",
            "nome",
            "caminho",
            "link",
            "responsavel",
            "responsavel_uso",
            "publico_alvo",
            "tipo_distribuidora",
        ]


class RegistroDeVersoesForm(forms.ModelForm):

    versao = forms.IntegerField(
        label="Versão",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    ticket = forms.CharField(
        label="Ticket",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    comentario = forms.CharField(
        label="Comentário",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = models.RegistroDeVersoes
        fields = [
            "versao",
            "responsavel",
            "ticket",
            "comentario",
        ]
