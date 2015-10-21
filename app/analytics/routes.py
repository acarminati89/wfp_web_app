from flask import render_template
from . import analytics

@analytics.route('/')
def index():
 return render_template('analytics/index.html')

@analytics.route('/dashboard')
def dashboard():
 return render_template('analytics/dashboard_pure_html.html')

@analytics.route('/db_test')
def db_test():
 y = [1, 2, 3, 4, 5, 6, 7, 8]
 return render_template('analytics/db_test.html', y=y)