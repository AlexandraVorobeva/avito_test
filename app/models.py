import sqlalchemy as sql
import app.database as database


class Client(database.Base):
    __tablename__ = "clients"

    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    balance = sql.Column(sql.Float, index=True)


class Operation(database.Base):
    __tablename__ = 'operations'

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey('clients.id'))
    date = sql.Column(sql.Date)
    kind = sql.Column(sql.String)
    amount = sql.Column(sql.Numeric(10, 2))
    description = sql.Column(sql.String, nullable=True)