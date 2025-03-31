from flask_wtf import FlaskForm
from wtforms.validators import NumberRange, DataRequired
from wtforms import SelectField, SubmitField, IntegerField


class GetIntConfForm(FlaskForm):
    hostname = SelectField(
        label='Hostname',
        description='show configuration interfaces ae0 unit {unit}',
        choices=[],
    )
    unit = IntegerField(
        'Unit Vlan', validators=[
            DataRequired(),
            NumberRange(min=1, max=4096)
        ],
        default=1258
    )
    submit = SubmitField(
        'Enviar'
    )
