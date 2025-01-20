
from django.shortcuts import render
from django.views.generic import TemplateView


def head(request):
    return render(request, 'fourth_task/head.html')

def games(request):
    context = {'game':['Baldrus Gate', 'Baldrus Gate 2', 'Baldrus Gate 3']}
    return render(request, 'fourth_task/games.html', context)

def basket(request):

    return render(request, 'fourth_task/basket.html')



