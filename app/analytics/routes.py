from flask import render_template
from . import analytics
from flask.ext.login import login_required

@analytics.route('/')
@login_required
def dashboard():
    return render_template('analytics/dashboard.html')


@analytics.route('/db_test')
@login_required
def db_test():
    y = 'no variable linked - this is static'
    return render_template('analytics/db_test.html', y=y)


@analytics.route('/base')
@login_required
def base():
    return render_template('base.html')
