from django.contrib import admin

from . import models


def get_fields_model(model):
    """Returns model fields list"""
    fields = [field.name for field in model._meta.local_fields]

    return fields

@admin.register(models.Repo)
class ClientesModelAdmin(admin.ModelAdmin):
    list_display = get_fields_model(models.Repo)
