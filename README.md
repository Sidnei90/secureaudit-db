git clone https://github.com/Sidnei90/secureaudit-db.git
cd secureaudit-db

## Crie e ative o ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows PowerShell

## Instale as dependências

pip install -r requirements.txt

## Configure as variáveis de ambiente criando um arquivo .env na raiz do projeto com a variável do banco:

set DATABASE_URL=postgresql://usuario:senha@localhost:5432/seubanco
# Linux / macOS
export DATABASE_URL=postgresql://usuario:senha@localhost:5432/seubanco

## Estrutura do projeto

Security-DB/


├── app/
│   ├── __init__.py           # Configuração do Flask e banco
│   ├── models.py             # Modelos User e Log
│   ├── forms.py              # Para fomulários e registros de logins
│   ├── utils.py              # Funções auxiliares (ex: registrar_log, cálculos)
│   ├── routes                # Rotas da aplicação (cálculos, usuários, etc)
│   │   ├── __init__.py  
│   │   ├── calculations.py
│   │   ├── logs.py
│   │   └── users.py
│   ├── templates/            # HTMLs organizados
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

## Funcionalidades atuais

- Cálculo de salário líquido
- Cálculo de 13º salário proporcional
- Cálculo de rescisão trabalhista
- Cálculo de férias + 1/3 constitucional
- Registro de logs por usuário
- Interface web via Flask + HTML
- Templates organizados por rota
- Separação de responsabilidades em módulos
- Testes de banco e inserção
- Migrações de banco de dados
- Pronto para deploy com variáveis de ambiente

## Funcionalidades planejadas

- Exportar os cálculos em PDF
- Melhorar responsividade da interface (Bootstrap)
- Autenticação com JWT para API
- Dashboard de ações e estatísticas

## Migrações

flask db migrate -m "Mensagem da migração"
flask db upgrade

## Testando inserções

python test_insert.py

## Execute o projeto

flask run

## Status do projeto

✅ Em andamento — funcionalidades principais implementadas.  
🔄 Em fase de melhorias e expansão de recursos.

## Como contribuir

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

## Licença

MIT license © Sidnei Moura

## Contato

Sidnei Moura – https://github.com/Sidnei90

Mais atualizações em breve... 
