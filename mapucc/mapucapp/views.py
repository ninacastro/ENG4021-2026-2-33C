from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'movie_form.html', {'form': form, 'title': 'Registrar filme'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movie_form.html', {'form': form, 'title': 'Atualizar filme'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    return render(request, 'movie_confirm_delete.html', {'movie': movie})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=matricula).exists():
            messages.error(request, 'Essa matrícula já está cadastrada.')
            return redirect('cadastro')

        User.objects.create_user(
            username=matricula,
            email=email,
            password=senha,
            first_name=nome
        )

        return redirect('login')

    return render(request, 'cadastro.html')


def login_usuario(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=matricula,
            password=senha
        )

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('movie_list')
        else:
            messages.error(request, 'Matrícula ou senha incorretas.')

    return render(request, 'login.html')


def logout_usuario(request):
    auth_logout(request)
    return redirect('login')
