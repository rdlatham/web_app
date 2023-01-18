FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
    """Read a text file and return a list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
# print(help(get_todos))


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items in a list to a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")