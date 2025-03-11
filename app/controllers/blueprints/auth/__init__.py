import os
from app import db
from app.models import Users
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from app.controllers.forms import LoginForm
from flask_login import login_required, login_user, logout_user
from flask import Blueprint, render_template, redirect, url_for, flash

load_dotenv()

auth_bp = Blueprint('auth', __name__)


def check_password(stored_password, provided_password):
    fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))

    try:
        decrypted_password = fernet_key.decrypt(stored_password).decode('utf-8')
        return decrypted_password == provided_password
    except Exception as e:
        print(f'[Erro] Falha ao verificar a senha: {e}')
        return False


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        input_username = login_form.username.data
        input_password = login_form.password.data

        user_record = db.session.execute(
            db.select(Users).filter_by(username=input_username)
        ).scalar_one_or_none()

        if user_record and check_password(user_record.password, input_password):
            login_user(user_record, remember=login_form.checkbox.data)
            flash(f'Login success {input_username}', category='success')
            return redirect(url_for('int_unit_bp.interface_unit'))
        else:
            flash('Usuário ou senha incorretos', category='danger')

    if login_form.errors:
        for field_name, error_messages in login_form.errors.items():
            for error_message in error_messages:
                flash(f'Error in {field_name}: {error_message}', category='danger')
    return render_template('login.html', form=login_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Deslogado!!!', category='info')
    return redirect(url_for('auth.login'))
