from django.contrib import admin

from . import models


def get_fields_model(model):
    """Returns model fields list"""
    fields = [field.name for field in model._meta.local_fields]

    return fields


@admin.register(models.Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Repo)


@admin.register(models.TipoEntidade)
class TipoEntidadeAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.TipoEntidade)


@admin.register(models.TipoGrupo)
class TipoGrupoAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.TipoGrupo)


@admin.register(models.TipoDistribuidora)
class TipoDistribuidoraAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.TipoDistribuidora)


@admin.register(models.TipoOrigemDados)
class TipoOrigemDadosAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.TipoOrigemDados)


@admin.register(models.Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Responsavel)


@admin.register(models.RegistroDeVersoes)
class RegistroDeVersoesAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.RegistroDeVersoes)


@admin.register(models.LGPD)
class LGPDAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.LGPD)


@admin.register(models.Tabelas)
class TabelasAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Tabelas)


@admin.register(models.Abas)
class AbasAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Abas)


@admin.register(models.Querys)
class QuerysAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Querys)
