import os
from app import db, admin
from dotenv import load_dotenv

from flask import url_for, redirect
from flask_login import current_user
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from wtforms import PasswordField
from wtforms.validators import Length, IPAddress, InputRequired
from app.models import Users, Routers, Switches, Olts, NeighborBgpIpv4, NeighborBgpIpv6
from cryptography.fernet import Fernet

load_dotenv()
path = os.path.join(os.path.dirname(__file__), 'static')


class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_bp.login'))

    edit_modal = details_modal = True
    can_view_details = can_set_page_size = True
    can_edit = can_create = can_export = can_delete = True

    column_default_sort = 'username'
    column_exclude_list = 'password'

    column_searchable_list = column_filters = column_editable_list = ['username', 'is_admin']

    form_overrides = {
        'password': PasswordField
    }

    form_args = {
        'password': {
            'validators': [
                InputRequired(),
                Length(min=6, max=30)
            ],
        }
    }

    def on_model_change(self, form, model, is_created):
        fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))
        if form.password.data:
            model.password = fernet_key.encrypt(form.password.data.encode('utf-8'))


class DeviceView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_bp.login'))

    edit_modal = details_modal = True
    can_view_details = can_set_page_size = True
    can_edit = can_create = can_export = True

    can_delete = False

    column_default_sort = 'hostname'
    column_searchable_list = column_filters = column_editable_list = ['hostname', 'ip_address']

    form_args = {
        'ip_address': {
            'label': 'Endereço IP',
            'validators': [InputRequired(), IPAddress(ipv4=True)],
            'description': 'Digite um IPv4 válido (ex: 192.168.1.1)'
        }
    }

    form_widget_args = {
        'ip_address': {
            'placeholder': '192.168.1.1',
        }
    }


class BgpNeighborView(DeviceView):
    column_default_sort = 'description'
    column_searchable_list = column_filters = column_editable_list = ['description', 'neighbor']


class BgpNeighborIpv4View(BgpNeighborView):
    column_labels = dict(neighbor='Neighbor IPv4')

    form_args = {
        'neighbor': {
            'label': 'Endereço IP',
            'validators': [InputRequired(), IPAddress(ipv4=True)],
            'description': 'Digite um IPv4 válido (ex: 192.168.1.1)'
        }
    }


class BgpNeighborIpv6View(BgpNeighborView):
    column_labels = dict(neighbor='Neighbor IPv6')

    form_args = {
        'neighbor': {
            'label': 'Endereço IP',
            'validators': [InputRequired(), IPAddress(ipv6=True, ipv4=False)],
            'description': 'Digite um IPv6 válido (ex: 2001:db8::1)'
        }
    }


class LogoutLink(MenuLink):
    def get_url(self):
        return url_for('auth_bp.logout')


class UploadsFileAdmin(FileAdmin):
    can_upload = can_delete = can_delete_dirs = True
    can_mkdir = can_rename = True

    allowed_extensions = None
    editable_extensions = ()


def flask_admin():
    admin.name = 'auto.clickip.local'

    admin.add_view(UserView(Users, db.session))

    admin.add_view(DeviceView(Olts, db.session, name='OLTs', category='Ativos'))
    admin.add_view(DeviceView(Routers, db.session, category='Ativos'))
    admin.add_view(DeviceView(Switches, db.session, category='Ativos'))

    admin.add_view(BgpNeighborIpv4View(NeighborBgpIpv4, db.session, category='Neighbor'))
    admin.add_view(BgpNeighborIpv6View(NeighborBgpIpv6, db.session, category='Neighbor'))

    admin.add_view(UploadsFileAdmin(path, '/static/', name='Uploads'))

    admin.add_link(LogoutLink(name='Logout', category=''))
