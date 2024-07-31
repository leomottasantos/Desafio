from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('usuario/', views.usuario, name='usuario'),
    path('usuario/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name="plataforma"),
]