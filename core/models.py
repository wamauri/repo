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
        blank=True
    )

    class Meta:
        verbose_name = 'Responsavel'
        verbose_name_plural = 'Responsaveis'

    def __str__(self):
        return self.nome
