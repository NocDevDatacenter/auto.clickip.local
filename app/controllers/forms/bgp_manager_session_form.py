from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class BgpManagerSessionForm(FlaskForm):
    hostname = SelectField(
        'Hostname', choices=[]
    )

    action = SelectField(
        'Action', choices=[
            ('activate', 'activate'),
            ('deactivate', 'deactivate'),
        ]
    )

    group = SelectField(
        'Group', choices=[
            ('Sessoes_Transito_IPv4', 'Sessoes_Transito_IPv4'),
            ('Sessoes_Transito_IPv6', 'Sessoes_Transito_IPv6'),
        ],
        default='Sessoes_Transito_IPv6'
    )

    neighbor = SelectField(
        'Neighbor', choices=[]
    )

    submit = SubmitField('Enviar')
