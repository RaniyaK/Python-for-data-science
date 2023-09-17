import tkinter
import tkinter.messagebox
import pickle
window = tkinter.Tk()
window.title("Own to do list")

def task_adding():
    todo = task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!",message="to add a task, please enter some task!!")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)

    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="To delete a task, you must select a task!!")


def task_load():
    try:
        todo_task = pickle.load(open(r"C:\Users\computer lab\Desktop\python\Python-for-data-science\tasks.dat"))
        todo_box.delete(0,tkinter.END)
        for todo in todo_task:
            todo_box.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Attention!!",message="Cannot find task.dat") 

def task_save():
    todo_list = todo_box.get(0,list_frame.size())
    pickle.dump(todo_list, open(r"C:\Users\computer lab\Desktop\python\Python-for-data-science\tasks.dat"))              

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height =20, width=50)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
# # scroller.config(command=list_frame.yview)

task_add = tkinter.Entry(window,width=70)
task_add.pack()

add_task_button = tkinter.Button(window,text="Click to add task",font=("arial",20,"bold"),background="red",width=40,command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window,text="CLICK TO DELETE TASK",font=("arial",20,"bold"),background="yellow",width=40,command=task_removing)
remove_task_button.pack()

load_task_button = tkinter.Button(window,text="CLICL TO LOAD TASK",font=("arial",20,"bold"),background="green",width=40,command=task_load)
load_task_button.pack()
save_task_button = tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",20,"bold"),background="blue",width=40,command=task_save)
save_task_button.pack()

window.mainloop()
