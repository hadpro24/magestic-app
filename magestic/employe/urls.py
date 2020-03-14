from django.urls import path

from . import views

app_name = 'employe'

urlpatterns =  [
    path('', views.employe, name='list_employe'),
]
