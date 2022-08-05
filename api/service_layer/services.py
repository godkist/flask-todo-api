from __future__ import annotations

from api.domain import model
from api.service_layer import unit_of_work


class InvalidUserId(Exception):
    pass


def add_user(
    name: str,
    uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        user = model.User(name=name)
        uow.user.add(user)
        uow.commit()

        return {
            'id': user.id,
            'name': user.name,
            'todos': [todo.task for todo in user.todos]
        }


def get_user(
    user_id: int,
    uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        user = uow.user.get(user_id)
        if user is None:
            raise InvalidUserId(f'Invalid user_id : {user_id}')

        return {
            'id': user.id,
            'name': user.name,
            'todos': [todo.task for todo in user.todos]
        }


def add_post_to_user(
    user_id: int,
    task: str,
    uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        user = uow.user.get(user_id)
        if user is None:
            raise InvalidUserId(f'Invalid user_id : {user_id}')
        user.todos.append(model.Todo(task))
        uow.commit()

        return {
            'id': user.id,
            'name': user.name,
            'todos': [todo.task for todo in user.todos]
        }
