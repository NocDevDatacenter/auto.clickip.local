from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class RegisterForm(FlaskForm):
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

    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(),
            Length(max=30),
            EqualTo('password')
        ]
    )

    checkbox = BooleanField(
        'Accept Terms', validators=[
            DataRequired()
        ],
        default=False
    )

    submit = SubmitField('Entrar')


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
