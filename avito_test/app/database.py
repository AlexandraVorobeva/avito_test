import sqlalchemy
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:54320/my_dbdata"

engine = sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()