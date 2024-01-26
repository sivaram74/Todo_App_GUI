import streamlit as st
import functions
todos = functions.read_todos()
def add_todo():
    todos.append(st.session_state["new_todo"]+"\n")
    functions.write_todos(todos)

st.title("my Todo App")
st.subheader("this is my to do app.")
st.write("this is to increase productivity")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",placeholder="Add a new todo....."
              ,on_change=add_todo,key="new_todo")
st.session_state()