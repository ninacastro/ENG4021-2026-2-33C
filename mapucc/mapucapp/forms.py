from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model= Movie
        fields= ['title', 'description', 'image.url']
        labels = {
            'title': 'Titulo',
            'description': 'Descrição',
            'image_url': 'URL da imagem',
        }
