from django.urls import path

from core.views import index, user_logout

urlpatterns = [
    path(
        route='', 
        view=index, 
        name='index'
    ),
    path(
        route='accounts/logout/', 
        view=user_logout, 
        name='logout'
    ),
]