from flask import Blueprint, request, jsonify, abort, render_template
from . import db
from .models import User, Log
from .utils import registrar_log

main = Blueprint('main', __name__)

# ROTAS PARA USUÁRIOS

@main.route('/logs')
def pagina_logs():
    return render_template('logs.html')

@main.route('/api/logs')
def api_logs():
    logs = Log.query.all()
    logs_serializados = [
        {
            'id': log.id,
            'username': log.user.username if log.user else 'Anônimo',
            'action': log.action,
            'timestamp': log.timestamp.isoformat()
        }
        for log in logs
    ]
    return jsonify(logs_serializados)

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'created_at': u.created_at.isoformat()
    } for u in users])

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    })

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or not all(k in data for k in ('username', 'email', 'password_hash')):
        return abort(400, "Campos obrigatórios: username, email, password_hash")

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return abort(400, "Usuário ou email já cadastrado")

    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=data['password_hash']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado', 'id': new_user.id}), 201

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    if not data:
        return abort(400, "Dados inválidos")

    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password_hash' in data:
        user.password_hash = data['password_hash']

    db.session.commit()
    return jsonify({'message': 'Usuário atualizado'})

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado'})


# ROTAS PARA LOGS

@main.route('/logs', methods=['GET'])
def get_logs():
    logs = Log.query.all()
    return jsonify([{
        'id': l.id,
        'user_id': l.user_id,
        'action': l.action,
        'timestamp': l.timestamp.isoformat()
    } for l in logs])

@main.route('/logs/<int:log_id>', methods=['GET'])
def get_log(log_id):
    log = Log.query.get_or_404(log_id)
    return jsonify({
        'id': log.id,
        'user_id': log.user_id,
        'action': log.action,
        'timestamp': log.timestamp.isoformat()
    })

@main.route('/logs', methods=['POST'])
def create_log():
    data = request.json
    if not data or not all(k in data for k in ('user_id', 'action')):
        return abort(400, "Campos obrigatórios: user_id, action")

    user = User.query.get(data['user_id'])
    if not user:
        return abort(404, "Usuário não encontrado")

    new_log = Log(user_id=data['user_id'], action=data['action'])
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Log criado', 'id': new_log.id}), 201

@main.route('/logs/<int:log_id>', methods=['DELETE'])
def delete_log(log_id):
    log = Log.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return jsonify({'message': 'Log deletado'})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.verify_password(data.get('password')):
        registrar_log(user.id, "login_sucesso")
        return jsonify({"msg": "Login realizado"}), 200
    else:
        user_id = user.id if user else 0
        registrar_log(user_id, "login_falha")
        return jsonify({"msg": "Credenciais inválidas"}), 401