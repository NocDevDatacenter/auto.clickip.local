from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, IPAddress


class StaticRouteForm(FlaskForm):
    network_dest = StringField(
        'Network Destination', validators=[
            DataRequired(),
            IPAddress(ipv4=True, ipv6=True)
        ]
    )
    prefix_dest = SelectField(
        'Prefix Destination', validators=[DataRequired()],
        choices=[
            ('/48', '/48'),
            ('/30', '/30'),
            ('/29', '/29'),
            ('/28', '/28'),
        ],
        default='/30'
    )
    next_hop = StringField(
        'Next Hop', validators=[
            DataRequired(),
            IPAddress(ipv4=True, ipv6=True)
        ]
    )
