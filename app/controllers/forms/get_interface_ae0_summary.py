from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class SummaryForm(FlaskForm):
    hostname = SelectField(
        label='Hostname',
        description='show interfaces terse lo0 | match lo',
        choices=[],

    )
    submit = SubmitField(
        'Enviar'
    )
