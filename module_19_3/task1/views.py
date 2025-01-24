from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Buyer, Game
def head(request):
    return render(request, 'fourth_task/head.html')

def games(request):
    games = []
    for game in Game.objects.all():
        games.append(game)
    context = {'games': games }
    return render(request, 'fourth_task/games.html', context)

def basket(request):

    return render(request, 'fourth_task/basket.html')

info = {}
def valid(users: list, name: str, pas: str, rep_pas: str, age: int) -> bool:
    if (name not in users) and (pas == rep_pas) and int(age) > 18:
        return True
def sign_up_by_html(request):
    global info
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if not Buyer.objects.filter(name=username).exists():
            Buyer.objects.create(name=username, age = age)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            info = {'error': 'Пользователь уже существует'}
        if password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    global info
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if valid(users, username, password, repeat_password, int(age)):
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                info = {'error': 'Пользователь уже существует'}
            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
    else:
        form = ContactForm()

    return render(request, 'fifth_task/registration_page.html', context=info)