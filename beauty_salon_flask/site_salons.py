import sqlite3
import os
from flask import Flask, render_template, url_for, request,g
from FDataBase import FDataBase
from admin.admin import admin


DATABASE = '/tmp/site_salons.db'
DEBUG = True
SECRET_KEY = 'ncbvasgt3fyef8hefa'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'site_salons.db')))
app.register_blueprint(admin, url_prefix='/admin')

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql',mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
def get_db():
    if not hasattr(g,'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'link_db'):
        g.link_db.close()

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

@app.route('/')
def home():
    print(url_for('home'))
    return render_template(
        'home_page.html', title = 'Главная',
        text = 'Добро пожаловать на сайт салона красоты BEAUTY',
        text1 = 'Наращевание ресниц',
        menu = menu,
        menu2 = menu2
    )

@app.route('/services')
def service():
    print(url_for('service'))
    return render_template('services.html', text1 = 'Услуги', title = 'Услуги',
                           menu2 = menu2)

@app.route('/prices')
def prices():
    print(url_for('prices'))
    return render_template('prices.html',title = 'Цены',
                           text1 = 'Цены на наращивание ресниц',menu = menu1,
                           menu2 = menu2)

@app.route('/online_registration',methods=['POST','GET'])
def online_reg():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        res = dbase.online_reg(request.form['username'], request.form['num_tel'])
        print(request.form)
    return render_template('online_registration.html', title = 'Регистрация',
                    text = 'Перед тем как записаться вам необходимо зарегистрироваться.',
                           menu2 = menu2
                    )


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title = 'О нас', text1 = 'О нас', text2 = 'Начав работу в 2015 году, мы создали'
                                                                 ' сеть студий с тысячами клиентов и сотнями довольных '
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
                                                                 ' “Делаем как в прошлый раз!” перед началом новой процедуры.',
                           menu2 = menu2)

@app.route('/gallery')
def gallery():
    print(url_for('gallery'))
    return render_template('gallery.html', title = 'Галерея',text1 = 'Наши работы',
                           menu2 = menu2
                           )


if __name__ == '__main__':
    app.run(debug=True)
