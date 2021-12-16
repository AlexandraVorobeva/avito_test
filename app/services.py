import app.database as database
import app.schemas as _models


def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)