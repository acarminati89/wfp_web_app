from flask import render_template
from . import analytics
from flask.ext.login import login_required, fresh_login_required
from app import db
from queries import *
import locale
import pandas as pd
import bokeh
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
import datetime

locale.setlocale(locale.LC_ALL, 'en_US')


@analytics.route('/')
@login_required
@fresh_login_required
def dashboard():
    # #######################
    # Generate high-level metrics
    # #######################
    ytd_pnl = db.engine.execute(sql_ytd_pnl)
    qtd_pnl = db.engine.execute(sql_qtd_pnl)
    mtd_pnl = db.engine.execute(sql_mtd_pnl)

    for row in ytd_pnl:
        ytd_pnl = locale.currency(row[0], '$', grouping=True)

    for row in qtd_pnl:
        qtd_pnl = locale.currency(row[0], '$', grouping=True)

    for row in mtd_pnl:
        mtd_pnl = locale.currency(row[0], '$', grouping=True)

    # #######################
    # Generate Cumulative P&L plot
    # #######################
    cum_pnl = db.engine.execute(sql_cum_pnl)

    output = list()
    for i in cum_pnl:
        output.append(i)

    df = pd.DataFrame(output, columns=['Date', 'Cumulative P&L'])
    # df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    # df.plot(x='Date', legend=False, title='Cumulative P&L', ylim = 0)

    tools = "box_zoom,reset,pan"

    p = figure(tools=tools,
               x_axis_type="datetime",
               width=1000,
               height=500)

    p.line(df['Date'], df['Cumulative P&L'])

    p.title = "Cumulative P&L YTD"
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'P&L'
    p.grid.grid_line_alpha = 0.3
    p.responsive = True

    p.left[0].formatter.use_scientific = False
    p.left[0].formatter = bokeh.models.formatters.NumeralTickFormatter(format='$ 0,0[.]00')

    p.xaxis.bounds = (datetime.datetime(2015, 01, 01), datetime.datetime(2016, 1, 1))
    p.yaxis.bounds = (0, 5000000)
    p.xaxis[0].ticker.desired_num_ticks = 12

    js_files = CDN.js_files[0]
    css_files = CDN.css_files[0]

    script, div = components(p, CDN)

    return render_template('analytics/dashboard.html',
                           ytd_pnl=ytd_pnl,
                           qtd_pnl=qtd_pnl,
                           mtd_pnl=mtd_pnl,
                           script=script,
                           div=div,
                           js_files=js_files,
                           css_files=css_files)


@analytics.route('/trader_performance')
@login_required
def trader_performance():
    grid_overview = db.engine.execute(sql_grid_overview)

    y = list()
    for i in grid_overview:
        y.append((i[0], locale.currency(i[1], '$', grouping=True)))

    return render_template('analytics/trader_performance.html',
                           y=y)
