from flask import Blueprint, request, jsonify, abort, render_template
from ..models import Log, User, db
from ..utils import registrar_log

logs = Blueprint('logs', __name__)

# Página HTML com logs (render_template)
@logs.route('/pagina', methods=['GET'])
def pagina_logs():
    return render_template('logs.html')

# API - Retorna todos os logs em JSON
@logs.route('/api', methods=['GET'])
def api_logs():
    logs_list = Log.query.all()
    return jsonify([
        {
            'id': log.id,
            'username': log.user.username if log.user else 'Anônimo',
            'action': log.action,
            'timestamp': log.timestamp.isoformat()
        }
        for log in logs_list
    ])

# API - Criar log manualmente (via JSON)
@logs.route('/', methods=['POST'])
def create_log():
    data = request.json
    if not data or not all(k in data for k in ('user_id', 'action')):
        abort(400, "Campos obrigatórios: user_id, action")

    user = User.query.get(data['user_id'])
    if not user:
        abort(404, "Usuário não encontrado")

    new_log = Log(user_id=data['user_id'], action=data['action'])
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Log criado', 'id': new_log.id}), 201

# API - Listar todos os logs simples
@logs.route('/', methods=['GET'])
def get_logs():
    logs_list = Log.query.all()
    return jsonify([{
        'id': l.id,
        'user_id': l.user_id,
        'action': l.action,
        'timestamp': l.timestamp.isoformat()
    } for l in logs_list])

# API - Ver log individual
@logs.route('/<int:log_id>', methods=['GET'])
def get_log(log_id):
    log = Log.query.get_or_404(log_id)
    return jsonify({
        'id': log.id,
        'user_id': log.user_id,
        'action': log.action,
        'timestamp': log.timestamp.isoformat()
    })

# API - Deletar log
@logs.route('/<int:log_id>', methods=['DELETE'])
def delete_log(log_id):
    log = Log.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return jsonify({'message': 'Log deletado'})

# LOGIN
@logs.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        abort(400, "Dados ausentes")

    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.verify_password(data.get('password')):
        registrar_log(user.id, "login_sucesso")
        return jsonify({"msg": "Login realizado com sucesso"}), 200
    else:
        registrar_log(user.id if user else 0, "login_falha")
        return jsonify({"msg": "Credenciais inválidas"}), 401
