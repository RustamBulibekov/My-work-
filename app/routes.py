from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/index1')
def index1():
    user = {'username': 'Rustam'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index_1.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route("/login1", methods=["GET", "POST"])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, {form.remember_me.data} ")
        return redirect(url_for('index'))
    return render_template('/login1.html', title="Sign IN", form=form)


"""Операция, которая преобразует шаблон в полную HTML-страницу, называется рендерингом. Чтобы отобразить шаблон, 
мне пришлось импортировать функцию, которая поставляется с флаговой инфраструктурой под названием render_template(). 
Эта функция принимает имя файла шаблона и переменную список аргументов шаблона и возвращает один и тот же шаблон, 
но при этом все заполнители в нем заменяются фактическими значениями."""
