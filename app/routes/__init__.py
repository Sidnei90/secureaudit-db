from flask import Blueprint

from .users import users
from .logs import logs
from .calculations import calculations

# Você pode adicionar uma função para facilitar o registro
def register_blueprints(app):
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(logs, url_prefix='/logs')
    app.register_blueprint(calculations, url_prefix='/calcular')
