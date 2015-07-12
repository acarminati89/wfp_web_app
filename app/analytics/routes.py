from flask import render_template
from . import analytics

@analytics.route('/')
def index():
    return render_template('analytics/index.html')

@analytics.route('/user/<username>')
def user(username):
    return render_template('analytics/user.html')