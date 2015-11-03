from flask import render_template, redirect, request, url_for, flash
from . import auth
from forms import *
from ..models import User
from flask.ext.login import login_user, login_required, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('.login'))
        # login_user(user, form.remember_me.data)
        login_user(user)
        return redirect(request.args.get('next') or url_for('analytics.overview')) # redirect(request.args.get('next') or url_for('analytics.dashboard_pure_html'))
    return render_template('auth/login.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('auth/logout.html')
