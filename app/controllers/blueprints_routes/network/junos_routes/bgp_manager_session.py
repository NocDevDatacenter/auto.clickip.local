import os
from app import db
from dotenv import load_dotenv
from app.models import Routers, BgpNeighbor
from cryptography.fernet import Fernet
from app.controllers.forms import BgpManagerSessionForm
from flask import Blueprint, render_template, flash
from flask_login import current_user, login_required, fresh_login_required

load_dotenv()

# Inicializa o Blueprint
bgp_manager_session_bp = Blueprint('bgp_manager_session_bp', __name__)

fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))


# Rota: bgp_manager_session_bp
@bgp_manager_session_bp.route('/bgp_manager_session', methods=['GET', 'POST'])
@login_required
@fresh_login_required
def bgp_manager_session():
    form = BgpManagerSessionForm()
    hosts = db.session.execute(db.select(Routers).order_by(Routers.id)).scalars()
    form.hostname.choices = [(host.ip_address, host.hostname) for host in hosts]

    neighbors = db.session.execute(db.select(BgpNeighbor).order_by(BgpNeighbor.id)).scalars()
    form.neighbor.choices = [(neighbor.neighbor, neighbor.description) for neighbor in neighbors]

    output = None

    current_user_decrypted_password = fernet_key.decrypt(current_user.password).decode('utf-8')

    if form.validate_on_submit():
        hostname = form.hostname.data
        username = current_user.username
        password = current_user_decrypted_password
        action = form.action.data
        group = form.group.data
        neighbor = form.neighbor.data

        output = bgp_manager_session(
            hostname, username, password,
            action, group, neighbor
        )

        flash('Command sent successfully!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", category='danger')

    return render_template(
        'junos/bgp_manager_session.html',
        form=form,
        output=output,
    )
