import os
from app import db
from dotenv import load_dotenv
from app.models import Users, Routers
from cryptography.fernet import Fernet
from app.controllers.forms import NetworkForm
from flask import Blueprint, request, render_template, flash
from app.controllers.netmiko import get_interface_ae0_config
from flask_login import current_user, login_required, fresh_login_required

load_dotenv()

# Inicializa o Blueprint
int_conf_bp = Blueprint('int_conf_bp', __name__)

fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))


# Rota: get_interface_ae0_config
@int_conf_bp.route('/get_interface_ae0_config', methods=['GET', 'POST'])
@login_required
@fresh_login_required
def interface_configuration():
    form = NetworkForm()

    devices = db.session.execute(db.select(Routers)).scalars().all()

    output = None

    current_user_record = db.session.execute(
        db.select(Users).filter_by(username=current_user.username)
    ).scalar_one_or_none()

    user_decrypted_password = fernet_key.decrypt(current_user_record.password).decode('utf-8')

    if request.method == 'POST':
        hostname = form.hostname.data
        username = current_user.username
        password = user_decrypted_password
        unit = request.form.get('unit')

        output = get_interface_ae0_config(
            hostname, username, password, unit
        )

        flash('Command sent successfully!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", category='danger')

    return render_template(
        'network/junos/get_interface_ae0_config.html',
        form=form,
        output=output,
        devices=devices,
    )
