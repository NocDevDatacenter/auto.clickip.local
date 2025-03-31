import os
from app import db
from dotenv import load_dotenv
from app.models import Users, Olts
from cryptography.fernet import Fernet
from flask import Blueprint, render_template, flash
from app.controllers.forms.downstream_fec import Downstream_fec_form
from flask_login import current_user, login_required, fresh_login_required
from app.controllers.netmiko.dmos.downstream_fec import no_downstream_fec

load_dotenv()

downstream_fec_bp = Blueprint('downstream_fec_bp', __name__)
fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))


@downstream_fec_bp.route('/downstream_fec', methods=['GET', 'POST'])
@login_required
@fresh_login_required
def downstream_fec():
    form = Downstream_fec_form()
    hosts = db.session.execute(db.select(Olts).order_by(Olts.id)).scalars()
    form.hostname.choices = [(host.ip_address, host.hostname) for host in hosts]

    output = None

    current_user_record = db.session.execute(db.select(Users).filter_by(username=current_user.username)).scalar_one_or_none()
    current_user_decrypted_password = fernet_key.decrypt(current_user_record.password).decode('utf-8')

    if form.validate_on_submit():
        output = no_downstream_fec(
            hostname=form.hostname.data,
            username=current_user.username,
            password=current_user_decrypted_password,
            chassis=form.chassis.data,
            slot=form.slot.data,
            port_id=form.port_id.data,
            dmos_command=form.dmos_command.data
        )

        flash('Command sent successfully!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", category='danger')

    return render_template(
        'vendors/dmos/downstream_fec.html',
        form=form,
        output=output,
    )
