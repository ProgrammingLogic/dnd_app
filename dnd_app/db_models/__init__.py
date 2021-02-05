from flask_sqlalchemy import SQLAlchemy

from .User import init_user


def init_databases(app):
    db = SQLAlchemy(app)
    init_user(db)

    return db
