from django.urls import path

from . import views

urlpatterns = [
    path(
        route='', 
        view=views.index, 
        name='index'
    ),
    path(
        route='repos/', 
        view=views.repos, 
        name='repos'
    ),
    path(
        route='registro_versoes_create/', 
        view=views.registro_versoes_create, 
        name='registro_versoes_create'
    ),
    path(
        route='lgpd_create/', 
        view=views.lgpd_create, 
        name='lgpd_create'
    ),
    path(
        route='tabelas_create/', 
        view=views.tabelas_create, 
        name='tabelas_create'
    ),
    path(
        route='abas_create/', 
        view=views.abas_create, 
        name='abas_create'
    ),
    path(
        route='querys_create/', 
        view=views.querys_create, 
        name='querys_create'
    ),
    path(
        route='accounts/logout/', 
        view=views.user_logout, 
        name='logout'
    ),
]
