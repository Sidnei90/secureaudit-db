from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate() #cria o objeto migrate

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db) #conecta o migrate ao app e db

    from . import models
    from . import routes
    app.register_blueprint(routes.main)  # Troque aqui

    return app