import os
from app import db
from dotenv import load_dotenv
from app.models import Routers
from cryptography.fernet import Fernet
from flask import Blueprint, render_template, flash
from app.controllers.forms.get_interface_ae0_config import GetIntConfForm
from flask_login import current_user, login_required, fresh_login_required
from app.controllers.netmiko.junos.get_interface_ae0_config import get_interface_ae0_config

load_dotenv()

# Inicializa o Blueprint
int_conf_bp = Blueprint('int_conf_bp', __name__)

fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))


# Rota: get_interface_ae0_config
@int_conf_bp.route('/get_interface_ae0_config', methods=['GET', 'POST'])
@login_required
@fresh_login_required
def interface_configuration():
    form = GetIntConfForm()
    hosts = db.session.execute(db.select(Routers).order_by(Routers.hostname)).scalars().all()
    form.hostname.choices = [(h.ip_address, h.hostname) for h in hosts]
    current_user_decrypted_password = fernet_key.decrypt(current_user.password).decode('utf-8')

    output = None

    if form.validate_on_submit():

        output = get_interface_ae0_config(
            hostname=form.hostname.data,
            username=current_user.username,
            password=current_user_decrypted_password,
            unit=form.unit.data
        )

        flash('Command sent successfully!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", category='danger')

    return render_template(
        'vendors/junos/get_interface_ae0_config.html',
        form=form,
        output=output,
    )
