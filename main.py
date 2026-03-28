from flask import Flask, render_template, redirect, request, make_response, jsonify
from data.jobs import Jobs
from data.login_form import LoginForm
from data import db_session, users_resource
from data.my_jobs import JobForm
from data.register_form import RegisterForm
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template('index.html', jobs=jobs, names=names, title="Добро пожаловать на Марс!")


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


@app.route("/table/<pol>/<age>")
def table(pol, age):
    return render_template('table.html', pol=pol, age=age, title="Оформление каюты")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.job_title.data,
            team_leader=form.team_leader_id.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_job_finished.data

        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('my_jobs.html', title='Авторизация', form=form)


# @app.route('/edit_job/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_job(id):
#     form = JobForm()
#     if request.method == "GET":
#         db_sess = db_session.create_session()
#         news = db_sess.query(News).filter(News.id == id,
#                                           News.user == current_user
#                                           ).first()
#         if news:
#             form.title.data = news.title
#             form.content.data = news.content
#             form.is_private.data = news.is_private
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         news = db_sess.query(News).filter(News.id == id,
#                                           News.user == current_user
#                                           ).first()
#         if news:
#             news.title = form.title.data
#             news.content = form.content.data
#             news.is_private = form.is_private.data
#             db_sess.commit()
#             return redirect('/')
#         else:
#             abort(404)
#     return render_template('news.html',
#                            title='Редактирование новости',
#                            form=form
#                            )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    # для списка объектов
    api.add_resource(users_resource.UserListResource, '/api/v2/user')

    # для одного объекта
    api.add_resource(users_resource.UserResource, '/api/v2/user/<int:user_id>')
    app.run(port=8080, host='127.0.0.1')
