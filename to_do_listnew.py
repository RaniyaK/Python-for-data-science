import tkinter as tk
from tkinter import messagebox
import pickle

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as file:
            tasks = pickle.load(file)
            listbox.delete(0, tk.END)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
load_button = tk.Button(root, text="Load Tasks", command=load_tasks)

add_button.pack(pady=5)
delete_button.pack(pady=5)
save_button.pack(pady=5)
load_button.pack(pady=5)

root.mainloop()
