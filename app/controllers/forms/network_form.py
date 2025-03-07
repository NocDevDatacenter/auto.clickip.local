from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, IPAddress, NumberRange
from wtforms import StringField, SubmitField, SelectField, IntegerField


class NetworkForm(FlaskForm):
    hostname = SelectField(
        'Hostname', choices=[]
    )
    unit_vlan = IntegerField(
        'Unit VLAN', validators=[
            DataRequired(),
            NumberRange(min=1, max=4096)
        ]
    )
    description = StringField(
        'Description', validators=[
            DataRequired()
        ]
    )
    bandwidth = IntegerField(
        'Bandwidth', validators=[
            DataRequired(),
            NumberRange(min=1, max=9999)
        ]
    )
    ipv4_gw = StringField(
        'IPv4 Address', validators=[
            DataRequired(),
            IPAddress(ipv4=True)
        ]
    )
    ipv6_gw = StringField(
        'IPv6 Gateway', validators=[
            DataRequired(),
            IPAddress(ipv6=True)
        ]
    )
    ipv6_cli = StringField(
        'IPv6 Client', validators=[
            DataRequired(),
            IPAddress(ipv6=True)
        ]
    )
    ipv6_48 = StringField(
        'IPv6 /48', validators=[
            DataRequired(),
            IPAddress(ipv6=True)
        ]
    )
    submit = SubmitField('Commitar')
