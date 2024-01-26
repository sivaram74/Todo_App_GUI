from functions import read_todos,write_todos
import time
while True:
    now=time.strftime("%b %d, %Y %H:%M:%S")
    user_prompt=input("What do you want to do? add,edit,show or exit")
    user_prompt=user_prompt.strip()
    if user_prompt.startswith("add"):
        todo = user_prompt[4:]+"\n"
        todos=read_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_prompt.startswith("show"):
        todos=read_todos()
        new_todos=[item.strip("\n") for item in todos]
        for index,item in enumerate(new_todos):
            print(f"{index}.{item}")
    elif user_prompt.startswith("edit"):
        try:
            todos=read_todos()
            edited=int(user_prompt[5:])
            edit=input("Enter the new item")+"\n"
            edited=edited-1
            todos[edited]=edit
            write_todos(todos)
        except ValueError:
            print("You have entered wrong command")
            continue
    elif user_prompt.startswith("complete"):
        try:
            todos=read_todos()
            number=int(user_prompt[9:])
            todos.pop(number)
            write_todos(todos)
        except IndexError:
            print("the entered item is not in the list")
            continue
    else:
        break

