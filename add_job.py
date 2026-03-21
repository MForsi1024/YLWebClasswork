from flask import Flask, url_for, request, render_template, redirect
from data.login_form import LoginForm
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()
    db_sess = db_session.create_session()
    # 1
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)
    # 2
    job = Jobs()
    job.team_leader = 2
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 23
    job.collaborators = '2, 4'
    job.is_finished = False
    db_sess.add(job)

    db_sess.commit()


if __name__ == "__main__":
    main()