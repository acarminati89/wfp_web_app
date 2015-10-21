from flask import render_template
from . import analytics
from global_vars import g

@analytics.route('/')
def index():
 return render_template('analytics/index.html')

@analytics.route('/dashboard')
def dashboard():
 return render_template('analytics/dashboard_pure_html.html')

@analytics.route('/db_test')
def db_test():
    conn = ps.connect(host=g['POSTGRES_HOST'],
                  port='5432',
                  user=g['POSTGRES_USER'],
                  password=g['POSTGRES_PWD'],
                  database=g['POSTGRES_DB'])
    cur = conn.cursor()
    sql_cmd = """SELECT account ,symbol ,realized ,unrealized FROM fact_daily_pl_report WHERE file_date = (SELECT max(file_date) FROM fact_daily_pl_report) ORDER BY account ,symbol;"""
    y = cur.execute(sql_cmd)
    #y = [1, 2, 3, 4, 5, 6, 7, 8]
    return render_template('analytics/db_test.html', y=y)