import os
from app import db, admin
from flask import url_for
from dotenv import load_dotenv
from flask_admin.menu import MenuLink
from cryptography.fernet import Fernet
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, IPAddress, InputRequired
from app.models import Users, Routers, Switches, Olts, NeighborBgpIpv4, NeighborBgpIpv6

load_dotenv()


class UsersView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'username'
    column_exclude_list = 'password'

    form_extra_fields = {
        'username': StringField(
            validators=[
                DataRequired(),
                Length(min=5, max=30)
            ]
        ),
        'password': PasswordField(
            validators=[
                DataRequired(),
                Length(min=6)
            ]
        ),
        'Password Confirm': PasswordField(
            validators=[
                DataRequired(),
                EqualTo('password', message='Your password must be match')
            ]
        ),
    }

    def on_model_change(self, form, model, is_created):
        fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))
        if form.password.data:
            model.password = fernet_key.encrypt(
                form.password.data.encode('utf-8')
            )


class RoutersView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'hostname'

    form_extra_fields = {
        'ip_address': StringField(
            'IP Address', validators=[
                InputRequired(),
                IPAddress(ipv4=True)
            ]
        ),
    }


class SwitchView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'hostname'

    form_extra_fields = {
        'ip_address': StringField(
            'IP Address', validators=[
                InputRequired(),
                IPAddress(ipv4=True)
            ]
        ),
    }


class OltView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'hostname'

    form_extra_fields = {
        'ip_address': StringField(
            'IP Address', validators=[
                InputRequired(),
                IPAddress(ipv4=True)
            ]
        ),
    }


class BgpNeighborIpv4View(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'description'

    form_extra_fields = {
        'neighbor': StringField(
            'Neighbor', validators=[
                InputRequired(),
                IPAddress(ipv4=True, ipv6=True)
            ]
        ),
    }


class BgpNeighborIpv6View(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True

    edit_modal = True
    details_modal = True

    can_view_details = False
    can_set_page_size = True

    column_default_sort = 'description'

    form_extra_fields = {
        'neighbor': StringField(
            'Neighbor', validators=[
                InputRequired(),
                IPAddress(ipv4=True, ipv6=True)
            ]
        ),
    }


def flask_admin():
    admin.name = 'auto.clickip.local'
    admin.add_view(UsersView(Users, db.session))
    admin.add_view(RoutersView(Routers, db.session, category='Ativos'))
    admin.add_view(SwitchView(Switches, db.session, category='Ativos'))
    admin.add_view(OltView(Olts, db.session, category='Ativos'))
    admin.add_view(BgpNeighborIpv4View(NeighborBgpIpv4, db.session, category='Neighbor'))
    admin.add_view(BgpNeighborIpv6View(NeighborBgpIpv6, db.session, category='Neighbor'))

    class LogoutLink(MenuLink):
        def get_url(self):
            return url_for('auth_bp.logout')

    admin.add_link(LogoutLink(name='Logout', category=''))
