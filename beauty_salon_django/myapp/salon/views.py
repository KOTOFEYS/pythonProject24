from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
from .forms import UserRegister


# Create your views here.
menu = ['В центре района Северный', 'Гарантия качества 10 дней', 'Запишись уже назавтра']
menu1 = ['Классика - 1300 рублей', '2D - 1500 рублей', '3D - 1800рублей', '4D - 2000 рублей',
         'трендовый эффект - 2500 рублей', 'Мокрый эффект - 2000 рублей']
menu2 = [{"name":'Главная страница', "url":"/"},
         {"name":'Услуги', "url": "/services"},
         {"name":'Цены', "url": "/prices"},
         {"name":'О нас', "url": "/about"},
         {"name":'Фотогалерея', "url": "/gallery"},
         {"name": 'Записаться сейчас', "url": "/online_registration"}
         ]

def home_page(request):
    title = 'Главная'
    text = 'Добро пожаловать на сайт салона красоты BEAUTY'
    text1 = 'Наращевание ресниц'
    context = {'title': title,
               'text': text,
               'text1': text1,
               'menu2': menu2,
               'menu': menu
               }
    return render(request, 'temp_dir/home_page.html', context)

def services(request):
    text1 = 'Услуги'
    title = 'Услуги'
    context = {'title': title,
               'text1': text1,
               'menu2': menu2,
               }
    return render(request, 'temp_dir/services.html', context)

def prices(request):
    title = 'Цены'
    text1 = 'Цены на наращивание ресниц'
    context = {
                'title': title,
               'text1': text1,
               'menu2': menu2,
               'menu1': menu1,
               }
    return render(request, 'temp_dir/prices.html', context)



def about(request):
    title = 'О нас'
    text1 = 'О нас'
    text2 = ('Начав работу в 2015 году, мы создали'
            'сеть студий с тысячами клиентов и сотнями довольных '
            'отзывов и реализовали строгую систему контроля'
            ' качества каждой работы. В числе самых значимых'
            ' достижений мастеров студии – призовые места в самых '
            'престижных международных чемпионатах:'
            ' – World Lash;'
            ' – Колибри Фест;'
            ' –  Brow Star. '
            'Главный приоритет нашей работы – качество и гарантия '
            'результата получаемого клиентом. Что включает в себя:'
            ' создание цельного и законченного образа клиента, '
            'ежедневный комфорт и большой срок носки ресничек, '
            'а также идеальные условия для проведения процедуры.'
            ' Мы бережно храним память о каждом Вашем визите, '
            'а самый большой комплимент для нас услышать от клиента:'
             ' “Делаем как в прошлый раз!” перед началом новой процедуры.')

    context = {
                'title': title,
               'text1': text1,
                'text2': text2,
               'menu2': menu2,
               }
    return render(request, 'temp_dir/about.html', context)

def gallery(requests):
    title = 'Галерея'
    text1 = 'Наши работы'
    context = {
                'title': title,
               'text1': text1,
               'menu2': menu2,
               }
    return render(requests, 'temp_dir/gallery.html', context)

# def online_reg(request):
#     title = 'Регистрация'
#     text1 = 'Перед тем как записаться вам необходимо зарегистрироваться'
#     # form = UserRegister()
#     # if request.method == 'POST':
#     #     form = UserRegister(request.POST)
#     #     if form.is_valid():
#     #         username = form.cleaned_data['username']
#     #         num_tel = form.cleaned_data['num_tel']
#     #         Person.objects.create(name=username, num_tel=num_tel)
#     #         return HttpResponse(f"Приветствуем, {username}!")
#     # else:
#     #     form = UserRegister()
#
#     return render(request, 'temp_dir/online_registration.html', context = {
#                 'title': title,
#                'text1': text1,
#                'menu2': menu2,
#                 # 'form': form
#     } )

# def reg(request):
#     # Person.objects.all()
#     form = UserRegister()
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             num_tel = form.cleaned_data['num_tel']
#             Person.objects.create(name=username, num_tel=int(num_tel))
#             return HttpResponse(f"Приветствуем, {username}!")
#     else:
#         form = UserRegister()
#     return render(request, 'temp_dir/online_registration.html', {'form': form})


def online_reg(request):
    title = 'Регистрация'
    text1 = 'Перед тем как записаться вам необходимо зарегистрироваться'
    if request.method == 'POST':
        username = request.POST.get('username')
        num_tel = request.POST.get('num_tel')
        Person.objects.create(name=username, num_tel=int(num_tel))
        return HttpResponse(f"Приветствуем, {username}!")


    return render(request, 'temp_dir/online_registration.html', context = {
                'title': title,
               'text1': text1,
               'menu2': menu2,

    } )