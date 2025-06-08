from app import create_app, db
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_migrate import Migrate

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

# adiciona comando 'db' para gerenciar migrações
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()