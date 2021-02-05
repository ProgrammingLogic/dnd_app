from flask import Flask
from flask_login import LoginManager

from routes import init_routes
from db_models import init_databases

app = Flask(__name__)
db = init_databases(app)
init_routes(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
