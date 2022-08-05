from flask import Flask, request
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.domain import model
from api.adapters import orm
from api.service_layer import services, unit_of_work


def create_app(config_class=Config):
    # app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db
    orm.start_mappers()
    engine = create_engine(
        app.config['SQLALCHEMY_DATABASE_URI'],
        echo=app.config['SQLALCHEMY_ECHO']
    )
    session_factory = sessionmaker(
        bind=engine
    )

    @app.route('/user', methods=['POST'])
    def add_user():
        user = services.add_user(
            name=request.json['name'],
            uow=unit_of_work.SqlAlchemyUnitOfWork(session_factory)
        )

        return {
            'id': user['id'],
            'name': user['name'],
            'todos': user['todos']
        }, 200

    @app.route('/user/<user_id>', methods=['GET'])
    def get_user_by_id(user_id):
        user = services.get_user(
            user_id=user_id,
            uow=unit_of_work.SqlAlchemyUnitOfWork(session_factory)
        )

        return {
            'id': user['id'],
            'name': user['name'],
            'todos': user['todos']
        }, 200

    @app.route('/user/<user_id>/todo', methods=['POST'])
    def add_todo_to_user(user_id):
        user = services.add_post_to_user(
            user_id=user_id,
            task=request.json['task'],
            uow=unit_of_work.SqlAlchemyUnitOfWork(session_factory)
        )

        return {
            'id': user['id'],
            'name': user['name'],
            'todos': user['todos']
        }, 201

    return app
