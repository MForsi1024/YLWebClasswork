from flask import Flask, url_for, request, render_template, redirect

from data.login_form import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key!!!'


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title='Подро дожаловать!')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, title="Тренировки")


@app.route("/list_prof/<type>")
def list_prof(type):
    profs = ['Инженер', "Врач", "Метеоролог", "Инженер-строитель", "Штурман", "Иженер-исследователь"]
    return render_template("list_prof.html", type=type, profs=profs)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    param = {}
    param["title"] = "Анкета"
    param["surname"] = "Иванов"
    param["name"] = "Иван"
    return render_template('answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/answer')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/table/<pol>/<age>")
def table(pol, age):
    return render_template('table.html', pol=pol, age=age, title='Цвет каюты')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
