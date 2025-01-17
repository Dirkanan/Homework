from django.shortcuts import render
from django.views.generic import TemplateView


def head(request):
    return render(request, 'third_task/head.html')

def games(request):
    return render(request, 'third_task/games.html')

def basket(request):
    return render(request, 'third_task/basket.html')



