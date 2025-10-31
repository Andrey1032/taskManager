from typing import Literal, Union
from datetime import datetime
from random_id import random_id

format_string = "%d %B %Y г., %H:%M"


class Task:
    '''
    Класс задачи, содержащий основную информацию о задаче

    :param description: Описание задачи
    :param id: Уникальный идентификатор задачи
    :param status: Статус задачи
    :param createdAt: Дата создания задачи
    :param updatedAt: Дата последнего изменения задачи
    '''

    def __init__(self,  description: str, id: Union[str, None] = None, status: Union[Literal['todo', 'in-progress', 'done'], None] = None, createdAt: Union[str, None] = None, updatedAt: Union[str, None] = None):
        self.id = id if id else random_id()
        self.description = description
        self.status = status if status else 'todo'
        if isinstance(createdAt, str):
            dt_created = datetime.strptime(createdAt, format_string)
            self.createdAt = dt_created
        else:
            self.createdAt = datetime.now()
        if isinstance(updatedAt, str):
            dt_updated = datetime.strptime(updatedAt, format_string)
            self.updatedAt = dt_updated
        else:
            self.updatedAt = None

    def set_status(self, status: Literal['todo', 'in-progress', 'done']) -> None:
        self.status = status
        self.updatedAt = datetime.now()

    def set_description(self, description: str) -> bool:
        self.description = description
        self.updatedAt = datetime.now()
        return True

    def __str__(self) -> str:
        return f'\nЗадача {self.id}:\n Описание: {self.description}\n Статус: {self.status}\n Создана: {self.createdAt}\n Изменна: {self.updatedAt}'

    def __repr__(self) -> str:
        return f"<Task {self.id}: {self.description}, Status: {self.status}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.strftime(format_string),
            "updatedAt": self.updatedAt.strftime(format_string) if self.updatedAt else None,
        }
