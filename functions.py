def read_todos():
    with open(r"C:\Users\2058028\OneDrive - Cognizant\Desktop\app1\todos.txt", "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local):
    with open(r"C:\Users\2058028\OneDrive - Cognizant\Desktop\app1\todos.txt", "w") as file:
        file.writelines(todos_local)


'''import time
print(time.strftime("%b %d, %Y %H:%M:%S"))../files/todos.txt'''
'''todos=read_todos()
print(todos)'''
