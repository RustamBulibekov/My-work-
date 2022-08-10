from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.models import User


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#

@app.route('/index')
def index():
    user = {"username": "Rustam"}
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
    return render_template('index.html', user=user, title='Home', posts=posts)




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


@app.route("/")
@app.route('/index2')
@login_required
def index2():

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
    return render_template('index2.html',  title='Home', posts=posts)


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
    return render_template('login1.html', title="Sign IN", form=form)


@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login2'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login1.html', title='Sign In', form=form)


@app.route('/login3', methods=['GET', 'POST'])
def login3():
    if current_user.is_authenticated:
        return redirect(url_for('index2'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login3'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index2')
        return redirect(next_page)
    return render_template('login1.html', title='Sign In', form=form)


"""Операция, которая преобразует шаблон в полную HTML-страницу, называется рендерингом. Чтобы отобразить шаблон, 
мне пришлось импортировать функцию, которая поставляется с флаговой инфраструктурой под названием render_template(). 
Эта функция принимает имя файла шаблона и переменную список аргументов шаблона и возвращает один и тот же шаблон, 
но при этом все заполнители в нем заменяются фактическими значениями."""
