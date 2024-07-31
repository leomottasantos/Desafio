from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def usuario(request):
  myusuario = Usuario.objects.all().values()
  template = loader.get_template('all_usuario.html')
  context = {
    'myusuario': myusuario,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myusuario = Usuario.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myusuario': myusuario,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            user = User.objects.get(username=username)
            return HttpResponse('Já existe um usuário com esse username')

            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
        except User.DoesNotExist:
            
            return HttpResponse('usuário cadastrado com sucesso!')




def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
      login_django(request, user)

      return HttpResponse('autenticado')
    else:
      return HttpResponse('Email ou senha iválido')

@login_required
def plataforma(request):
  return HttpResponse('Você precisa estar logado')
