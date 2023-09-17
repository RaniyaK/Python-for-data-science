import tkinter as tk
import datetime
import time
root = tk.Tk()
root.title("Python Alarm Clock")

time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack()

entry_label = tk.Label(root, text="Enter time (HH:MM):", font=("Helvetica", 16))
entry_label.pack()

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

set_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 16), command="set_alarm")
set_button.pack()

root.mainloop()
def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        while True:
            now = datetime.datetime.now()
            if now.hour == alarm_hour and now.minute == alarm_minute:
                time_label.config(text="Time to Wake Up!")
                break
            else:
                current_time = now.strftime("%H:%M:%S")
                time_label.config(text=current_time)
                root.update()
                time.sleep(1)
    except ValueError:
        time_label.config(text="Invalid time format (HH:MM)")
if __name__ == "__main__":
    root.mainloop()
