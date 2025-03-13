from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired(),
            Length(max=30),
        ]
    )

    password = PasswordField(
        'Password', validators=[
            DataRequired(),
            Length(max=30),
        ]
    )

    checkbox = BooleanField(
        'Remember me!', default=True
    )

    submit = SubmitField('Entrar')
