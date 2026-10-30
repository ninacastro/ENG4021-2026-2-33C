from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.models import User
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
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            error = 'Nome de usuário já cadastrado.'
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('login')

    return render(request, 'cadastro.html', {
        'action': 'Cadastrar',
        'error': error
    })


def login_usuario(request):
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('movie_list')
        else:
            error = 'Usuário ou senha incorretos.'

    return render(request, 'login.html', {'error': error})


def logout_usuario(request):
    auth_logout(request)
    return redirect('login')
