import os

FILEPATH = 'todos.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file :
        pass

def get_todos_from_file(filepath=FILEPATH) :
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos_to_file(todos, filepath=FILEPATH) :
    with open(filepath, 'w') as file:
        file.writelines(todos)


def show_todo_list() :
    todos = get_todos_from_file()

    print("To Do List: ")
    for number, item in enumerate(todos):
        todo_title = f"{number + 1}.{item.title()}"
        print(todo_title.strip('\n'))


