from flask import render_template
from . import analytics

@analytics.route('/login')
def login():
 return render_template('analytics/login.html')