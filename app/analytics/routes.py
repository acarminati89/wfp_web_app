from flask import render_template
from . import analytics

@analytics.route('/')
def login():
 return render_template('analytics/index.html')