from django.db import models


class TipoEntidade(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Tipo Entidade'
        verbose_name_plural = 'Tipos Entidade'

    def __str__(self):
        return self.nome


class TipoGrupo(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Tipo Grupo'
        verbose_name_plural = 'Tipos Grupo'

    def __str__(self):
        return self.nome


class TipoDistribuidora(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Tipo Distribuidora'
        verbose_name_plural = 'Tipos Distribuidora'

    def __str__(self):
        return self.nome


class TipoOrigemDados(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Tipo Origem Dados'
        verbose_name_plural = 'Tipos Origem Dados'

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    GRAU_STATUS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    )
    codigo = models.CharField(
        verbose_name="Código",
        max_length=255,
        null=True,
        blank=True
    )
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255,
        null=True,
        blank=True
    )
    grau_status = models.CharField(
        verbose_name="Nome",
        max_length=255,
        choices=GRAU_STATUS,
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Responsavel'
        verbose_name_plural = 'Responsaveis'

    def __str__(self):
        return self.nome


class Repo(models.Model):
    tipo_entidade = models.ForeignKey(
        to=TipoEntidade,
        on_delete=models.CASCADE,
        verbose_name="Tipo Entidade",
        related_name="repo"
    )
    nome = models.CharField(
        verbose_name="Nome",
        max_length=255
    )
    caminho = models.CharField(
        verbose_name="Caminho",
        max_length=255
    )
    link = models.CharField(
        verbose_name="Link",
        max_length=255
    )
    responsavel = models.ForeignKey(
        to=Responsavel,
        on_delete=models.CASCADE,
        verbose_name="Responsavel",
        related_name="core_repo_responsavel"
    )
    responsavel_uso = models.CharField(
        verbose_name="Responsavel Uso",
        max_length=255,
        null=True,
        blank=True
    )
    publico_alvo = models.CharField(
        verbose_name="Público-alvo",
        max_length=255,
        null=True,
        blank=True
    )
    tipo_distribuidora = models.ForeignKey(
        to=TipoDistribuidora,
        on_delete=models.CASCADE,
        verbose_name="Tipo Distribuidora",
        related_name="repo"
    )

    class Meta:
        verbose_name = 'Repo'
        verbose_name_plural = 'Repos'

    def __str__(self):
        return self.nome


class RegistroDeVersoes(models.Model):
    versao = models.IntegerField(
        verbose_name="Versão",
    )
    responsavel = models.ForeignKey(
        to=Responsavel,
        on_delete=models.CASCADE,
        verbose_name="Responsavel",
        related_name="registro_de_versoes"
    )
    ticket = models.CharField(
        verbose_name="Ticket",
        max_length=255
    )
    comentario = models.CharField(
        verbose_name="Comentário",
        max_length=255
    )

    class Meta:
        verbose_name = 'Registro de Versão'
        verbose_name_plural = 'Registro de Versões'

    def __str__(self):
        return self.ticket


class LGPD(models.Model):
    ANONIMIZADO = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )
    nome_coluna = models.CharField(
        verbose_name="Nome Coluna",
        max_length=255,
        null=True,
        blank=True
    )
    conteudo_anonimizado = models.CharField(
        verbose_name="Conteúdo Anonimizado",
        max_length=255,
        null=True,
        blank=True,
        choices=ANONIMIZADO
    )
    justificativa_para_uso = models.CharField(
        verbose_name="Nome Coluna",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'LGPD'
        verbose_name_plural = 'LGPD'

    def __str__(self):
        return self.nome_coluna


class Tabelas(models.Model):
    nome_tabela = models.CharField(
        verbose_name="Nome Tabela",
        max_length=255,
    )
    origem_dados = models.ForeignKey(
        to=TipoOrigemDados,
        on_delete=models.CASCADE,
        verbose_name="Tipo Origem Dados",
        related_name="tabelas"
    )

    class Meta:
        verbose_name = 'Tabela'
        verbose_name_plural = 'Tabelas'

    def __str__(self):
        return self.nome_tabela
