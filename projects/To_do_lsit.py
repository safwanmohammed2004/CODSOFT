#TASK1----TO DO LIST PROGRAM-----
#Using tkinter module
from tkinter import *
from tkinter import messagebox     #This library  is used to display a message

#create functions
def newTask():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","PLEASE ENTER SOME TASK")

def deleteTask():
    lb.delete(ANCHOR)

# Creating the main-window
work_space=Tk()     # Initializing the library
work_space.geometry('550x500+900+200')
work_space.title('**Tasks to Tackle**')   # Title for the list
work_space.config(bg='#244444')   # Background colour
work_space.resizable(width=False,height=False)

#Creating widgets like (frame ,listbox,scrollbar,entry,button)
frame=Frame(work_space)
frame.pack(pady=10)

lb=Listbox(
    frame,
    width=25,
    height=10,
    font=('times',18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',

)
lb.pack(side=LEFT,fill=BOTH)

task_list=[
    'GYM',
    'Breakfast',
    'College',
    'Home',
    'Nap time'



]

for item in task_list:
    lb.insert(END,item)

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    work_space,
    font=('times',24)
)

my_entry.pack(pady=20)

button_frame=Frame(work_space)
button_frame.pack(pady=20)

addTask_button= Button(
    button_frame,
    text='add task',
    font=('times 14'),
    bg="#c5f776",
    padx=20,
    pady=10,
    command=newTask
)
addTask_button.pack(fill=BOTH,expand=True,side=LEFT)

DelTask_button=Button(
    button_frame,
    text="delete task",
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
DelTask_button.pack(fill=BOTH, expand=True,side=LEFT)

#creating main loop
work_space.mainloop()
