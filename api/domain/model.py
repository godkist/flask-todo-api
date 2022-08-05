from __future__ import annotations
from dataclasses import dataclass
from typing import List


class User:
    def __init__(self, name: str, todos: List[Todo] = None):
        self.name = name
        if todos is None:
            self.todos = []
        else:
            self.todos = todos

    def __repr__(self):
        return f'<User {self.name}>'

    def assign(self, todo: Todo):
        self.todos.append(todo)


@dataclass(unsafe_hash=True)
class Todo:
    task: str
