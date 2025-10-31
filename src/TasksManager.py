from typing import List, Dict
from src.Task import Task
import json
import os


class TasksManager:
    """
    Класс менеджера задач, содержащий список задач
    """

    def __init__(self):
        try:
            # Пробуем открыть файл и загрузить задачи
            with open(file='tasks.json', mode='r', encoding='utf-8') as file:
                raw_data = json.load(file)
                # Восстанавливаем задачи из сырых данных
                self.tasks = [Task(**data) for data in raw_data]
        except FileNotFoundError:
            # Если файл не найден, инициализируем пустой список задач
            self.tasks = []
        except json.JSONDecodeError:
            # Если файл есть, но содержит некорректные данные, используем пустой список
            self.tasks = []

    def add(self, description: str) -> List:
        task = Task(description=description)
        self.tasks.append(task)
        self.__save_to_file()
        print(f"Добавлена задача {task}")
        return self.tasks

    def delete(self, task_id: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.__save_to_file()
                return True
        return False

    def update(self, task_id: str, new_description: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.set_description(new_description)
                self.__save_to_file()
                print(f"Изменана задача {task}")
                return True
        return False

    def list_tasks(self, filter_by_status=None) -> List[Dict]:
        """Получить список всех задач или выбрать определённый статус."""
        filtered_tasks = [
            task.to_dict() for task in self.tasks
            if not filter_by_status or task.status == filter_by_status
        ]
        return filtered_tasks

    def mark_in_progress(self, task_id: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.set_status('in-progress')
                self.__save_to_file()
                print(f"Задача отмечена как 'в процессе': {task}")
                return True
        return False
        

    def mark_done(self, task_id: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.set_status('done')
                self.__save_to_file()
                print(f"Задача отмечена как 'выполнена': {task}")
                return True
        return False

    def __save_to_file(self):
        # Перед сохранением превращаем каждую задачу в словарь
        serialized_tasks = [task.to_dict() for task in self.tasks]
        print(serialized_tasks)
        with open(file='tasks.json', mode='w', encoding='utf-8') as file:
            json.dump(serialized_tasks, file, ensure_ascii=False, indent=4)
