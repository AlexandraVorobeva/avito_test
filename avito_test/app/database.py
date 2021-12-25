import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as orm


DATABASE_URL = "postgresql://hello_fastapi:hello_fastapi@db/hello_fastapi_dev"

engine = sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
