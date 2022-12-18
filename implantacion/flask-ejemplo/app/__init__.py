from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import routes
    app.register_blueprint(routes.bp)

    return app
