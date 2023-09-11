import tkinter as tk

# Function to update the entry field with button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter main loop
window.mainloop()
