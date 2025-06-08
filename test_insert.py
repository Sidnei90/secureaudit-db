from app import create_app, db
from app.models import User, Log

app = create_app()
app.app_context().push()

# Criar um usuário novo
user = User(username='joao', email='joao@email.com', password_hash='hashseguro123')

# Adicionar e commitar no banco
db.session.add(user)
db.session.commit()

# Criar um log para esse usuário
log = Log(user_id=user.id, action='login')

db.session.add(log)
db.session.commit()

# Consultar e mostrar os dados salvos
users = User.query.all()
logs = Log.query.all()

print("Usuários cadastrados:")
for u in users:
    print(u)

print("\nLogs cadastrados:")
for l in logs:
    print(l)