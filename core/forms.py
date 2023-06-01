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
        widget=forms.TextInput(
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
        widget=forms.Textarea(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
                "cols": 80,
                "rows": 3,
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


class LGPDForm(forms.ModelForm):

    nome_coluna = forms.CharField(
        label="Nome Coluna",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    justificativa_para_uso = forms.CharField(
        label="Justificativa Para Uso",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = models.LGPD
        fields = [
            "nome_coluna",
            "conteudo_anonimizado",
            "justificativa_para_uso",
        ]


class TabelasForm(forms.ModelForm):

    nome_tabela = forms.CharField(
        label="Nome Tabela",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = models.Tabelas
        fields = [
            "nome_tabela",
            "origem_dados",
        ]


class AbasForm(forms.ModelForm):

    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    descricao = forms.CharField(
        label="Descrição",
        widget=forms.Textarea(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
                "cols": 80,
                "rows": 3,
            }
        )
    )

    class Meta:
        model = models.Abas
        fields = [
            "nome",
            "descricao",
        ]


class QuerysForm(forms.ModelForm):

    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    query = forms.CharField(
        label="Query",
        widget=forms.Textarea(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
                "cols": 80,
                "rows": 3,
            }
        )
    )
    tempo = forms.CharField(
        label="Tempo",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    linhas = forms.CharField(
        label="Linhas",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )
    colunas = forms.CharField(
        label="Colunas",
        widget=forms.TextInput(
            attrs={
                "placeholder": "", 
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = models.Querys
        fields = [
            "nome",
            "query",
            "tempo",
            "linhas",
            "colunas",
        ]
