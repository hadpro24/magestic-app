from django.urls import path

from . import views

app_name = 'employe_app'

urlpatterns =  [
    path('', views.employe, name='list-employe'),
    path('profile/<int:id_employe>/', views.profile, name='profile'),
    path('create-employe', views.create_employe, name='create-employe'),
]
