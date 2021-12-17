from avito_test import app as database


def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)