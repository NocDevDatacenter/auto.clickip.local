from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class BgpManagerForm(FlaskForm):
    hostname = SelectField(
        'Hostname', choices=[]
    )

    action = SelectField(
        'Action', choices=[
            ('activate', 'activate'),
            ('deactivate', 'deactivate'),
        ],
        default='activate'
    )

    group = SelectField(
        'Group', choices=[
            ('Sessoes_Transito_IPv4', 'Sessoes_Transito_IPv4'),
            ('Sessoes_Transito_IPv6', 'Sessoes_Transito_IPv6'),
        ],
        default='Sessoes_Transito_IPv4'
    )

    neighbor = SelectField(
        'Neighbor', choices=[]
    )

    submit = SubmitField(
        'Commit',
    )
