from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import HTMLResponse
from backend.db import SessionLocal
from schemas import CreateUsers
from sqlalchemy.sql import text
from models import Person
from typing import Annotated
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from sqlalchemy import insert, select

router = APIRouter(prefix='', tags=['Frontend'])
templates = Jinja2Templates(directory="templates")


menu = ['В центре района Северный','Гарантия качества 10 дней', 'Запишись уже назавтра']
menu1 = ['Классика - 1300 рублей', '2D - 1500 рублей', '3D - 1800рублей', '4D - 2000 рублей',
         'трендовый эффект - 2500 рублей', 'Мокрый эффект - 2000 рублей']
menu2 = [{"name":'Главная страница', "url":"/"},
         {"name":'Услуги', "url": "services"},
         {"name":'Цены', "url": "prices"},
         {"name":'О нас', "url": "about"},
         {"name":'Фотогалерея', "url": "gallery"},
         {"name": 'Записаться сейчас', "url": "online_registration"}
         ]

visitors = []

@router.get('/')
async def home(request:Request):
    title = 'Главная'
    text3 = 'Добро пожаловать на сайт салона красоты BEAUTY'
    text1 = 'Наращевание ресниц'
    return templates.TemplateResponse(name='home_page.html', context={'request': request,
                                                                      "title":title,
                                                                      "menu":menu,
                                                                      "text3":text3,
                                                                      "text1":text1,
                                                                      "menu2":menu2
                                                                      })

@router.get('/services')
async def service(request:Request):
    title = 'Услуги'
    text1 = 'Услуги'
    return templates.TemplateResponse(name='services.html', context={'request': request,
                                                                      "title":title,
                                                                      "menu2":menu2,
                                                                      "text1":text1
                                                                      })
@router.get('/prices')
async def prices(request:Request):
    text1 = 'Цены на наращивание ресниц'
    title = 'Цены'
    return templates.TemplateResponse(name='prices.html', context={'request': request,
                                                                     "title": title,
                                                                     "menu2": menu2,
                                                                     "text1": text1,
                                                                     "menu1": menu1
                                                                     })

@router.get('/about')
async def about(request:Request):
    title = 'О нас'
    text1 = 'О нас'
    text2 = 'Начав работу в 2015 году, мы создали сеть студий с тысячами клиентов и сотнями довольных отзывов и реализовали строгую систему контроля качества каждой работы. В числе самых значимых достижений мастеров студии – призовые места в самых престижных международных чемпионатах: – World Lash; – Колибри Фест; –  Brow Star. Главный приоритет нашей работы – качество и гарантия результата получаемого клиентом. Что включает в себя: создание цельного и законченного образа клиента, ежедневный комфорт и большой срок носки ресничек, а также идеальные условия для проведения процедуры. Мы бережно храним память о каждом Вашем визите, а самый большой комплимент для нас услышать от клиента: “Делаем как в прошлый раз!” перед началом новой процедуры.'

    return templates.TemplateResponse(name='about.html', context={'request': request,
                                                                     "title": title,
                                                                     "menu2": menu2,
                                                                     "text1": text1,
                                                                     "text2": text2
                                                                     })
@router.get('/gallery')
async def gallery(request:Request):
    title = 'Галерея'
    text1 = 'Наши работы'

    return templates.TemplateResponse(name='gallery.html', context={'request': request,
                                                                     "title": title,
                                                                     "menu2": menu2,
                                                                     "text1": text1

                                                                     })

@router.get('/online_registration')
async def online_reg(request:Request):
    title='Регистрация'
    text3='Перед тем как записаться вам необходимо зарегистрироваться'

    return templates.TemplateResponse(name='online_registration.html', context={'request': request,
                                                                     "title": title,
                                                                     "menu2": menu2,
                                                                     "text3": text3
                                                                                })



@router.post('/reg')
async def reg(db: Annotated[Session, Depends(get_db)],data: CreateUsers = Form()):

    query = text("INSERT INTO users (name, num_tel) VALUES (:name, :num_tel)")
    db.execute(query, {"name": data.name, "num_tel": data.num_tel})
    db.commit()
    return {'message': "Вы успешно зарегистрировались"}
