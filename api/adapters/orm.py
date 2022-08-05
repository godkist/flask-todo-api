from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import mapper, relationship
from api.domain import model

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(32), nullable=False)
)

todo = Table(
    'todo',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('task', String(255), nullable=False),
)


def start_mappers():
    mapper(
        model.User,
        user,
        properties={
            'todos': relationship(model.Todo, backref='user')
        }
    )

    mapper(
        model.Todo,
        todo
    )
