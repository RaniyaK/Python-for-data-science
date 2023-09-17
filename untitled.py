# Import necessary modules
import tkinter as tk
from datetime import datetime
from sqlite3 import connect
from tkinter import simpledialog

# Connect to the database
conn = connect('todolist.db')
cur = conn.cursor()

def add_task():
    # Get the input value from the entry field
    desc = entry_field.get().strip()
    
    # Check if the input is empty
    if len(desc) == 0:
        return
    
    # Insert a new row into the database table
    cur.execute("INSERT INTO todo VALUES (NULL, ?)", (desc,))
    
    # Refresh the display
    show_tasks()

def edit_task():
    # Get the selected item index
    sel_index = listbox.curselection()[0]
    
    # Get the current task description
    old_desc = listbox.get(sel_index).split(",")[1].strip()
    
    # Prompt the user for a new description
    new_desc = simpledialog.askstring("New Description", f"Enter a new description for '{old_desc}':")
    
    # Update the database record
    cur.execute("UPDATE todo SET description=? WHERE id=?", (new_desc, sel_index+1))
    
    # Refresh the display
    show_tasks()

def delete_completed():
    # Delete all rows marked as completed
    cur.execute("DELETE FROM todo WHERE completed='True'")
    
    # Refresh the display
    show_tasks()

def clear_all():
    # Clear all records from the database
    cur.execute("DELETE FROM todo")
    
    # Refresh the display
    show_tasks()

def show_tasks():
    # Query the database for all incomplete tasks
    cur.execute("SELECT * FROM todo WHERE completed='False' ORDER BY created DESC")
    results = cur.fetchall()
    
    # Empty the listbox
    listbox.delete(0, tk.END)
    
    # Populate the listbox with the queried tasks
    for result in results:
        listbox.insert(tk.END, f"{result['id']}: {result['description']}")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Add labels and entry fields
label_date = tk.Label(text="Current Date & Time: ")
label_incomplete = tk.Label(text="Incomplete Tasks: ")
entry_field = tk.Entry(width=50)
button_add = tk.Button(text="Add Task", command=add_task)
button_edit = tk.Button(text="Edit Task", command=edit_task)
button_del = tk.Button(text="Delete Completed", command=delete_completed)
button_clear = tk.Button(text="Clear All", command=clear_all)
listbox = tk.Listbox(height=10, width=50)

# Pack the widgets onto the screen
label_date.pack()
label_incomplete.pack()
entry_field.pack()
button_add.pack()
button_edit.pack()
button_del.pack()
button_clear.pack()
listbox.pack()

# Show the initial set of tasks
show_tasks()

# Run the main loop
root.mainloop()

# Close the database connection
cur.close()
conn.commit()
conn.close()
