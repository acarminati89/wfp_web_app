from flask import render_template
from . import analytics
from flask.ext.login import login_required
from app import db
from queries import *
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

@analytics.route('/')
@login_required
def dashboard():
    ytd_pnl = db.engine.execute(sql_ytd_pnl)
    qtd_pnl = db.engine.execute(sql_qtd_pnl)
    mtd_pnl = db.engine.execute(sql_mtd_pnl)
    grid_overview = db.engine.execute(sql_grid_overview)

    for row in ytd_pnl:
        ytd_pnl = locale.currency(row[0], '$', grouping=True)

    for row in qtd_pnl:
        qtd_pnl = locale.currency(row[0], '$', grouping=True)

    for row in mtd_pnl:
        mtd_pnl = locale.currency(row[0], '$', grouping=True)

    y = list()
    for i in grid_overview:
        y.append((i[0], locale.currency(i[1], '$', grouping=True)))

    return render_template('analytics/dashboard.html'
                           , ytd_pnl=ytd_pnl
                           , qtd_pnl=qtd_pnl
                           , mtd_pnl=mtd_pnl
                           , y=y)
