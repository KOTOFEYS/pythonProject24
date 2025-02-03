from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated,List
from starlette.requests import Request

app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# class Home(BaseModel):
#     id: int
#     description: str
#     is_completed: bool = False


    # Home(id=1, description="В центре района Северный", is_completed=True),
    # Home(id=2, description="Гарантия качества 10 дней",is_completed=True),
    # Home(id=3, description="Запишись уже назавтра",is_completed=True)]

@app.get('/')
async def get_home():
    return {"hgdsgf":"skjdfhiergfh"}
#     menu = ['В центре района Северный','Гарантия качества 10 дней', 'Запишись уже назавтра']
#     title = 'Главная',
#     text = 'Добро пожаловать на сайт салона красоты BEAUTY',
#     text1 = 'Наращевание ресниц'
#


# @app.get('/', responses=HTMLResponse)
# async def get_home(request:Request):
#     return templates.TemplateResponse("home_page.html")

    # "text": text, "text1": text1,, "menu": menu}
