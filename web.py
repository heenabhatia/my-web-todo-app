import streamlit as st
import functions

todos = functions.get_todos_from_file()

def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos_to_file(todos)
    st.session_state['new_todo'] = ''


st.title("Routine tasks")
st.write("This is app where you can add todo list.")

for todo in todos:
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos_to_file(todos)
        del st.session_state[todo]
        st.rerun()

input_box = st.text_input(label='', placeholder="Add new task..",
              on_change=add_todo, key='new_todo')