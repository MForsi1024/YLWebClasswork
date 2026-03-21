from flask import Flask, url_for, request, render_template, redirect
from data.login_form import LoginForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()
    db_sess = db_session.create_session()

    # 1
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)
    # 2
    user = User()
    user.surname = "Ivan"
    user.name = "Ridley"
    user.age = 23
    user.position = "colonist"
    user.speciality = "biolog"
    user.address = "module_1"
    user.email = "ivan_chief@mars.org"
    user.hashed_password = "ivan"
    db_sess.add(user)
    #3
    user = User()
    user.surname = "Semen"
    user.name = "Ridley"
    user.age = 45
    user.position = "colonist"
    user.speciality = "geolog"
    user.address = "module_2"
    user.email = "semen_chief@mars.org"
    user.hashed_password = "ivan"
    db_sess.add(user)
    # 4
    user = User()
    user.surname = "Mark"
    user.name = "Ridley"
    user.age = 56
    user.position = "colonist"
    user.speciality = "cook"
    user.address = "module_2"
    user.email = "mark_chief@mars.org"
    user.hashed_password = "ivan"
    db_sess.add(user)
    db_sess.commit()


if __name__ == "__main__":
    main()