from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import *
from sqlalchemy.engine.url import URL
import config

def db_connect():
    return create_engine(URL(**config.database))

class User(db.Model):
    __tablename__ = 'lu_user'

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


class PLReport(db.Model):
    __tablename__ = 'fact_daily_pl_report'

    account = db.Column(db.String(50), primary_key=True)
    symbol = db.Column(db.String(10), primary_key=True)
    realized = db.Column(db.DECIMAL)
    unrealized = db.Column(db.DECIMAL)
    trades = db.Column(db.DECIMAL)
    volume = db.Column(db.DECIMAL)
    date = db.Column(db.String(10), primary_key=True)
    ecn_fee = db.Column(db.DECIMAL)
    sec_Fee = db.Column(db.DECIMAL)
    commission = db.Column(db.DECIMAL)
    nasdaq_fee = db.Column(db.DECIMAL)
    nscc_Fee = db.Column(db.DECIMAL)
    clearing_fee = db.Column(db.DECIMAL)
    orders_yielding_exec = db.Column(db.DECIMAL)
    position = db.Column(db.DECIMAL)
    closing_price = db.Column(db.DECIMAL)
    nyse_fee = db.Column(db.DECIMAL)
    amex_fee = db.Column(db.DECIMAL)
    nasdaq_etf = db.Column(db.DECIMAL)
    file_name = db.Column(db.String(50))
    file_date = db.Column(db.String(50))

