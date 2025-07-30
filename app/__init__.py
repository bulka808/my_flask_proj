from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    # Регистрируем Blueprint
    from app.views.main import main_bp
    app.register_blueprint(main_bp)

    # Создаём таблицы
    with app.app_context():
        db.create_all()

    return app