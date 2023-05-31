from django.urls import path

from . import views

urlpatterns = [
    path(
        route='', 
        view=views.index, 
        name='index'
    ),
    path(
        route='repos', 
        view=views.repos, 
        name='repos'
    ),
    path(
        route='accounts/logout/', 
        view=views.user_logout, 
        name='logout'
    ),
]
