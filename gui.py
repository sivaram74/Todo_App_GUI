import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("DarkPurple4")
clock=sg.Text("",key="clock")
text=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values= functions.read_todos(), key="todos",
                    enable_events=True, size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")
window=sg.Window("My To Do App",
                 layout=[[clock],[text],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                 font=("Calibri",20))
print(functions.read_todos())
while True:
    event,values= window.read(timeout=10)
    window["clock"].update(value=time.strftime("%d %d %Y %H:%M:%S"))
    print(event)
    print(values)
    if event=="Add":
        current_todos= functions.read_todos()
        new_todo=values["todo"]+"\n"
        print(new_todo)
        current_todos.append(new_todo)
        functions.write_todos(current_todos)
        window["todos"].update(values=current_todos)
    elif event=="Edit":
        try:
            new_todo= values["todo"]
            current_todos= functions.read_todos()
            m=values["todos"]
            current_todos[current_todos.index(m[0])]=values["todo"]+"\n"
            functions.write_todos(current_todos)
            window["todos"].update(values=current_todos)
        except IndexError:
            sg.popup("Please select an item first",font=("Calibri",20))
    elif event=="Complete":
        try:
            removed_item=values["todos"][0]
            current_todos= functions.read_todos()
            current_todos.remove(removed_item)
            functions.write_todos(current_todos)
            window["todos"].update(values=current_todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Calibri", 20))
    elif event=="Exit":
        break
    elif event=="todos":
        window["todo"].update(value=values["todos"][0])


    elif sg.WIN_CLOSED:
        break

window.close()
