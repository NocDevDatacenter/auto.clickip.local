import os
from app import db
from dotenv import load_dotenv
from app.models import Routers
from cryptography.fernet import Fernet
from app.controllers.forms import AddressAssignmentForm
from flask import Blueprint, request, render_template, flash
from flask_login import current_user, login_required, fresh_login_required

load_dotenv()

# Inicializa o Blueprint
int_dhcp_bp = Blueprint('int_dhcp_bp', __name__)

fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))


@int_dhcp_bp.route('/set_access_address_assignment_page', methods=['GET', 'POST'])
@login_required
@fresh_login_required
def set_access_address_assignment_page():
    form = AddressAssignmentForm()

    devices = db.session.execute(db.select(Routers)).scalars().all()

    user_decrypted_password = fernet_key.decrypt(current_user.password).decode('utf-8')

    output = None

    if form.validate_on_submit():
        hostname = request.form.get('hostname')
        username = current_user.username
        password = user_decrypted_password

        output = set_access_address_assignment_page(
            hostname, username, password,
        )

        flash('Command sent successfully!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", category='danger')

    return render_template(
        'junos/set_access_address_assignment.html',
        form=form,
        output=output,
        devices=devices,
    )
