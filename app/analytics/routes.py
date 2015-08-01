from flask import render_template
from . import analytics

@analytics.route('/')#, subdomain='wfp-admin')
def index():
    # return "Placeholder for the WFP Management administration page."
    return render_template('analytics/index.html')

@analytics.route('/user/<username>')#, subdomain='wfp-admin')
def user(username):
    return render_template('analytics/user.html')