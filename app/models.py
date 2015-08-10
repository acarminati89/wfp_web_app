from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class LuUser(db.Model):
    __tablename__ = 'lu_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# class StgDailyTrades(db.Model):
#     __tablename__ = 'stg_daily_trades'
#
#     trader = db.Column(db.String(255))
#     sequence_no = db.Column(db.String(255))
#     account = db.Column(db.String(255))
#     side = db.Column(db.String(255))
#     symbol = db.Column(db.String(255))
#     quantity = db.Column(db.String(255))
#     price = db.Column(db.String(255))
#     destination = db.Column(db.String(255))
#     contra = db.Column(db.String(255))
#     trade_datetime = db.Column(db.String(255))
#     bo_account = db.Column(db.String(255))
#     cusip = db.Column(db.String(255))
#     liq = db.Column(db.String(255))
#     order_id = db.Column(db.String(255))
#     exec_broker = db.Column(db.String(255))
#     ecn_fee = db.Column(db.String(255))
#     order_datetime = db.Column(db.String(255))
#     specialist = db.Column(db.String(255))
#     commission = db.Column(db.String(255))
#     bb_trade = db.Column(db.String(255))
#     sec_fee = db.Column(db.String(255))
#     batch_id = db.Column(db.String(255))
#     client_order_id = db.Column(db.String(255))
#     prime = db.Column(db.String(255))
#     cover_quantity = db.Column(db.String(255))
#     userr = db.Column(db.String(255))
#     settle_date = db.Column(db.String(255))
#     principal = db.Column(db.String(255))
#     net_amount = db.Column(db.String(255))
#     allocation_id = db.Column(db.String(255))
#     allocation_role = db.Column(db.String(255))
#     is_clearable = db.Column(db.String(255))
#     nscc_fee = db.Column(db.String(255))
#     nasdaq_fee = db.Column(db.String(255))
#     clearing_fee = db.Column(db.String(255))
#     nyse_etf_fee = db.Column(db.String(255))
#     amex_etf_fee = db.Column(db.String(255))
#     listing_exchange = db.Column(db.String(255))
#     native_liq = db.Column(db.String(255))
#     order_received_id = db.Column(db.String(255))
#     bo_group_id = db.Column(db.String(255))
#     side_desc = db.Column(db.String(255))
#     calculated_quantity = db.Column(db.String(255))
#     calculated_principal = db.Column(db.String(255))
#     ticket_fee = db.Column(db.String(255))
#     total_fee = db.Column(db.String(255))
#     away_ticket = db.Column(db.String(255))
#     total_cost = db.Column(db.String(255))
#     calculated_net = db.Column(db.String(255))
#     file_name = db.Column(db.String(255))
#     file_date = db.Column(db.String(255))
#
# class StgDailyPlReport(db.Model):
#     __tablename__ = 'stg_daily_pl_report'
#
#     account = db.Column(db.String(255))
#     symbol = db.Column(db.String(255))
#     realized = db.Column(db.String(255))
#     unrealized = db.Column(db.String(255))
#     trades = db.Column(db.String(255))
#     volume = db.Column(db.String(255))
#     date = db.Column(db.String(255))
#     ecn_fee = db.Column(db.String(255))
#     sec_Fee = db.Column(db.String(255))
#     commission = db.Column(db.String(255))
#     nasdaq_fee = db.Column(db.String(255))
#     nscc_Fee = db.Column(db.String(255))
#     clearing_fee = db.Column(db.String(255))
#     orders_yielding_exec = db.Column(db.String(255))
#     position = db.Column(db.String(255))
#     closing_price = db.Column(db.String(255))
#     nyse_fee = db.Column(db.String(255))
#     amex_fee = db.Column(db.String(255))
#     nasdaq_etf = db.Column(db.String(255))
#     file_name = db.Column(db.String(255))
#     file_date = db.Column(db.String(255))
#
# class FactDailyPlReport(db.Model):
#     __tablename__ = 'stg_daily_pl_report'
#
#     account = db.Column(db.String(50))
#     symbol = db.Column(db.String(10))
#     realized = db.Column(db.Numeric)
#     unrealized = db.Column(db.Numeric)
#     trades = db.Column(db.Numeric)
#     volume = db.Column(db.Numeric)
#     date = db.Column(db.Numeric)
#     ecn_fee = db.Column(db.Numeric)
#     sec_Fee = db.Column(db.Numeric)
#     commission = db.Column(db.Numeric)
#     nasdaq_fee = db.Column(db.Numeric)
#     nscc_Fee = db.Column(db.Numeric)
#     clearing_fee = db.Column(db.Numeric)
#     orders_yielding_exec = db.Column(db.Numeric)
#     position = db.Column(db.Numeric)
#     closing_price = db.Column(db.Numeric)
#     nyse_fee = db.Column(db.Numeric)
#     amex_fee = db.Column(db.Numeric)
#     nasdaq_etf = db.Column(db.Numeric)
#     file_name = db.Column(db.String(50))
#     file_date = db.Column(db.String(8))