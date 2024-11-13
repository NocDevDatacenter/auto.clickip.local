from flask import Blueprint, flash, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
from app import db
from app.controllers.forms import Form_Register
from app.models.model import Table_Register

user_bp = Blueprint('user', __name__)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@user_bp.route('/register', methods=['GET', 'POST'])
def page_register():
    form = Form_Register()
    table = db.session.execute(db.select(Table_Register)).scalars().all()
    
    if form.validate_on_submit():
        user = Table_Register(
            username=form.username.data,
            password=generate_password_hash(form.password.data, method='pbkdf2:sha256')
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', category='success')
        return redirect(url_for('user.page_register'))

    if form.errors:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar usuário: {err}', category='danger')
    
    return render_template('page_register_user.html', form=form, table=table)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@user_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def page_edit_user(id):
    user = db.session.execute(db.select(Table_Register).filter_by(id=id)).scalar_one_or_none()
    form = Form_Register(obj=user)
    
    if user is None:
        flash(f'Usuário com ID {id} não encontrado.', category='danger')
        return redirect(url_for('user.page_register'))
    
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        db.session.commit()
        flash('Usuário atualizado com sucesso!', category='success')
        return redirect(url_for('user.page_register'))
    
    return render_template('page_edit_user.html', user=user, form=form)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@user_bp.route('/<int:id>/remove')
def remove_user(id):
    user = db.session.execute(db.select(Table_Register).filter_by(id=id)).scalar_one_or_none()
    
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Usuário excluído com sucesso.', category='success')
    else:
        flash('Usuário não encontrado.', category='danger')

    return redirect(url_for('user.page_register'))
