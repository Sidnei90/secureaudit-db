# Security-DB

Projeto Flask com PostgreSQL para gerenciamento básico de usuários e logs, utilizando Flask-Migrate para controle de migrações.

---

## Tecnologias usadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL
- python-dotenv

---

## Configuração do ambiente

1. Clone o repositório:
   ```bash
   git clone <url-do-seu-repositorio>
   cd Security-DB

## Crie e ative o ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows PowerShell

## Instale as dependências

pip install -r requirements.txt

## Configure as variáveis de ambiente criando um arquivo .env na raiz do projeto com a variável do banco:

DATABASE_URL=postgresql://postgres:<sua_senha>@localhost:5432/security_db

## Estrutura do projeto

Security-DB/
│
├── app/
│   ├── __init__.py           # Configuração do Flask e banco
│   ├── models.py             # Modelos User e Log
│   ├── routes.py             # Rotas da aplicação (a criar)
│   └── ...
│
├── migrations/               # Migrações do banco geradas pelo Flask-Migrate
│
├── test_insert.py            # Script para testar inserção de dados
├── test_db.py                # Script para testar conexão com DB
├── config.py                 # Configurações do Flask (ex: URI do banco)
├── requirements.txt          # Dependências do projeto
└── README.md

## Modelos criados

- User: Usuário com campos id, username, email, password_hash e created_at.

- Log: Registro de ações do usuário, com user_id como chave estrangeira para o usuário que realizou a ação.

## Migrações

flask db migrate -m "Mensagem da migração"
flask db upgrade

## Testando inserções

python test_insert.py

## Próximos passos

