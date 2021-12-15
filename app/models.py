import sqlalchemy as sql
import app.database as database


class Client(database.Base):
    __tablename__ = "clients"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    balance = sql.Column(sql.Float, index=True)
