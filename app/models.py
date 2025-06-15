from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    # Identificador único da tabela (chave primária)

    username = db.Column(db.String(80), unique=True, nullable=False)  
    # Nome do usuário, deve ser único e não pode ser vazio

    email = db.Column(db.String(120), unique=True, nullable=False)  
    # Email também único e obrigatório

    password_hash = db.Column(db.String(128), nullable=False)  
    # Senha já com hash, por segurança, obrigatória

    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    # Data e hora de criação do usuário (automático)

    def __repr__(self):  
        # Como o objeto será mostrado no console, para facilitar o debug
        return f'<User {self.username}>'


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
  
    action = db.Column(db.String(255), nullable=False)  
  
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  
    
    user = db.relationship('User', backref=db.backref('logs', lazy=True))  
   
    def __repr__(self):  
        return f'<Log {self.action} by User {self.user_id}>'
