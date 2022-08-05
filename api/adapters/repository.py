from abc import ABC, abstractmethod
from api.domain import model


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: model.User):
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: int):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user: model.User):
        self.session.add(user)

    def get(self, user_id: int):
        return self.session.query(model.User).filter_by(
            id=user_id
        ).first()
