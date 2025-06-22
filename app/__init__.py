from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .routes import main
from .calculations_routes import calculations  
import os

main.register_blueprint(main)
main.register_blueprint(calculations)  

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__,
                template_folder='app/templates',
                static_folder='static')
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import register_blueprints
    register_blueprints(app)

    return app