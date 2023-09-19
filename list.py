import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("To-Do List")

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create an entry widget for adding tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
task_listbox = tk.Listbox(app, width=40, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Create a button to delete selected tasks
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

# Start the Tkinter main loop
app.mainloop()
