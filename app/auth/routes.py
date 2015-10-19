from flask import render_template
from . import auth
import random
# imports for Bokeh plotting
#import bokeh.plotting
#from bokeh.plotting import figure
#from bokeh.resources import CDN
#from bokeh.embed import file_html, components
# imports for matplotlib plotting
#import tempfile
#import matplotlib
#matplotlib.use('Agg') # this allows PNG plotting
#import matplotlib.pyplot as plt

@auth.route('/login')
def login():
 import sys
 sys.version
 # generate some random integers, sorted
 exponent = .7+random.random()*.6
 dta = []
 for i in range(50):
  rnum = int((random.random()*10)**exponent)
  dta.append(rnum)
 y = sorted(dta)
 x = range(len(y))
 # generate Bokeh HTML elements
 # create a `figure` object
 p = figure(title='A Bokeh plot', plot_width=500,plot_height=400)
 # add the line
 p.line(x,y)
 # add axis labels
 p.xaxis.axis_label = "time"
 p.yaxis.axis_label = "size"
 # create the HTML elements to pass to template
 figJS,figDiv = components(p,CDN)
 # generate matplotlib plot
 fig = plt.figure(figsize=(5,4),dpi=100)
 axes = fig.add_subplot(1,1,1)
 # plot the data
 axes.plot(x,y,'-')
 # labels
 axes.set_xlabel('time')
 axes.set_ylabel('size')
 axes.set_title("A matplotlib plot")
 # make the temporary file
 f = tempfile.NamedTemporaryFile(
 dir='static/temp',
 suffix='.png',delete=False)
 # save the figure to the temporary file
 plt.savefig(f)
 f.close() # close the file
 # get the file's name (rather than the whole path)
 # (the template will need that)
 plotPng = f.name.split('/')[-1]
 return(render_template('figures.html', y=y, figJS=figJS,figDiv=figDiv, plotPng=plotPng))
 #return render_template('auth/login.html')
