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

sql_cum_pnl = '''
select
    distinct trade_date
    ,CAST(sum(realized) OVER (ORDER BY trade_date) AS INTEGER) AS cum_amt
from fact_daily_pl_report
order by trade_date;
'''

sql_top_daily_trades = '''
SELECT max.trade_date
	,account
	,symbol
	,max.max_realized
FROM (
	SELECT trade_date
		,max(realized) AS max_realized
	FROM fact_daily_pl_report
	GROUP BY trade_date
	) max
INNER JOIN fact_daily_pl_report fct
	ON max.trade_date = fct.trade_date
		AND max.max_realized = fct.realized
WHERE max_realized <> 0
ORDER BY max.trade_date;
'''
