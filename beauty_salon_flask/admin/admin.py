import sqlite3
from flask import Blueprint, request, url_for, render_template, flash, session, g
from werkzeug.utils import redirect

admin = Blueprint('admin',__name__, template_folder='templates', static_folder='static')

def isLogged():
    return True if session.get('admin_logged') else False

def login_admin():
    session['admin_logged'] = 1

def logout_admin():
    session.pop('admin_logged',None)

menu1 = [{'url': '.index','title': 'Панель'},
            {'url': '.database','title': 'Список пользователей'},
            {'url': '.logout','title': 'Выйти'}]

db = None
@admin.before_request
def before_request():
    global db
    db = g.get('link_db')

@admin.teardown_request
def teardown_request(request):
    global db
    db = None
    return request

@admin.route('/')
def index():
    if not isLogged():
        return redirect(url_for('.login'))

    return render_template('admin/index.html', menu = menu1, title='Админ-панель')

@admin.route('/login', methods=["POST", "GET"])
def login():
    if isLogged():
        return redirect(url_for('.index'))

    if request.method == "POST":
        if request.form['user'] == "admin" and request.form["psw"] == "12345":
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash("Неверная пара логин/пароль", "error")
    return render_template('admin/login.html',title='Админ-панель')

@admin.route('/logout', methods=['POST','GET'])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))
    logout_admin()
    return redirect(url_for('.login'))

@admin.route('/database')
def database():
    if not isLogged():
        return redirect(url_for('.login'))

    list = [ ]
    if db:
        try:

            cur = db.cursor()
            cur.execute(f"SELECT username, num_tel FROM menu")
            list = cur.fetchall()
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))

    return render_template('admin/database.html', title = 'Список данных', menu = menu1, list = list)
    prin(list)
