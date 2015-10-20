#!/home/ubuntu/miniconda/bin/python
from flask import render_template
from . import auth

@auth.route('/login')
def login():
 return(render_template('figures.html', y=y, figJS=figJS,figDiv=figDiv, plotPng=plotPng))
 return render_template('auth/login.html')
