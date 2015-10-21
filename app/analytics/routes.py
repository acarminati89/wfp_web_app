from flask import render_template
from . import analytics

@analytics.route('/')
def index():
 return render_template('analytics/dashboard_pure_html.html')