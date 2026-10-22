from django.shortcuts import render
from django.db.models import Q
from .models import Local

# Create your views here.
def home(request):
    return render(request, "index.html")

# Inicio
def home(request):
    busca = request.GET.get('busca', '')

    locais = Local.objects.none()

    if busca:
        locais = Local.objects.filter(
            Q(nome__icontains=busca) |
            Q(predio__icontains=busca) |
            Q(sala__icontains=busca)
        )

    return render(request, "inicio.html", {
        "locais": locais,
        "busca": busca
    })


# Deslogar
def deslogar(request):
    return render(request, "deslogar.html")
```