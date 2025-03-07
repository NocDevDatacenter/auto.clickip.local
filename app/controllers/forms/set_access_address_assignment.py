import ipaddress
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, \
    Length, NumberRange


# personal validator
def cidr_Validator():
    try:
        ipaddress.ip_network(strict=False)
    except ValueError:
        raise ValidationError('Invalid Network, example: 192.168.0.1/24')


class AddressAssignmentForm(FlaskForm):
    vlan = IntegerField(
        'vlan',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=4096)
        ]
    )

    network = StringField(
        'Network',
        validators=[
            DataRequired(),
            Length(min=9, max=18),
        ]
    )

    description = StringField(
        'Description',
        validators=[
            DataRequired(),
            Length(max=30)
        ]
    )

    submit = SubmitField('Enviar')
