import argparse
from src.TasksManager import TasksManager

def main():
    parser = argparse.ArgumentParser(description='Простое приложение для управления задачами.')
    
    subparsers = parser.add_subparsers(dest='command')

    # Добавляем команду "add"
    add_parser = subparsers.add_parser('add', help='Создание новой задачи')
    add_parser.add_argument('description', type=str, help='Описание задачи')

    # Команда "update"
    update_parser = subparsers.add_parser('update', help='Обновление существующей задачи')
    update_parser.add_argument('task_id', type=str, help='Номер задачи')
    update_parser.add_argument('new_description', type=str, help='Новое описание задачи')

    # Команда "delete"
    delete_parser = subparsers.add_parser('delete', help='Удаление задачи')
    delete_parser.add_argument('task_id', type=str, help='Номер задачи')

    # Команда "mark-in-progress"
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Отмечаем задачу как выполняющуюся')
    mark_in_progress_parser.add_argument('task_id', type=str, help='Номер задачи')

    # Команда "mark-done"
    mark_done_parser = subparsers.add_parser('mark-done', help='Отмечаем задачу как завершённую')
    mark_done_parser.add_argument('task_id', type=str, help='Номер задачи')

    # Команда "list"
    list_parser = subparsers.add_parser('list', help='Список задач')
    list_parser.add_argument('--status', choices=['todo', 'in-progress', 'done'], default=None, help='Фильтрация по статусу')

    args = parser.parse_args()

    manager = TasksManager()

    if args.command == 'add':
        manager.add(args.description)
    elif args.command == 'update':
        manager.update(args.task_id, args.new_description)
    elif args.command == 'delete':
        manager.delete(args.task_id)
    elif args.command == 'mark-in-progress':
        manager.mark_in_progress(args.task_id)
    elif args.command == 'mark-done':
        manager.mark_done(args.task_id)
    elif args.command == 'list':
        result = manager.list_tasks(filter_by_status=args.status)
        for task in result:
            print(f" id: {task['id']} \n\t status: ({task['status']}) \n\t description: {task['description']} \n\t created: {task['createdAt']} \n\t updated: {task['updatedAt']}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()