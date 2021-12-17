from .database import Base, engine


def _add_tables():
    return Base.metadata.create_all(bind=engine)