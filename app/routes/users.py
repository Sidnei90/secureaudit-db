from flask import Blueprint, request, jsonify, abort
from ..models import User, db

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_users():
    users_list = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'created_at': u.created_at.isoformat()
    } for u in users_list])

@users.route('/', methods=['POST'])
def create_user():
    data = request.json
    if not data or not all(k in data for k in ('username', 'email', 'password_hash')):
        abort(400, "Campos obrigatórios: username, email, password_hash")
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        abort(400, "Usuário ou email já cadastrado")

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado', 'id': new_user.id}), 201