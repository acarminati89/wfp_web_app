sql_grid_overview = '''
SELECT
	account
	,sum(realized)
FROM fact_daily_pl_report fact
INNER JOIN dim_calendar_ytd dim ON fact.trade_date = dim.ytd_day
WHERE dim.day = (select max(trade_date) from fact_daily_pl_report)-- AND unrealized = 0
GROUP BY account
ORDER BY account;
'''

sql_mtd_pnl = '''
SELECT
	sum(realized)::integer
FROM FACT_DAILY_PL_REPORT fct
INNER JOIN dim_calendar_mtd dim ON fct.trade_date = dim.mtd_day
WHERE dim.day = (select max(trade_date) from fact_daily_pl_report);
--	AND unrealized = 0;
'''

sql_qtd_pnl = '''
SELECT
	sum(realized)::integer
FROM FACT_DAILY_PL_REPORT fct
INNER JOIN dim_calendar_qtd dim ON fct.trade_date = dim.qtd_day
WHERE dim.day = CURRENT_DATE;
--	AND unrealized = 0;
'''

sql_ytd_pnl = '''
SELECT
	sum(realized)::integer
FROM FACT_DAILY_PL_REPORT fct
INNER JOIN dim_calendar_ytd dim ON fct.trade_date = dim.ytd_day
WHERE dim.day = (select max(trade_date) from fact_daily_pl_report);
--	AND unrealized = 0;
'''