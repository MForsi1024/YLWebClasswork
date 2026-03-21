from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import EmailField, BooleanField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job_title = StringField('Job title', validators=[DataRequired()])
    team_leader_id = StringField('Team leader id', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_job_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')