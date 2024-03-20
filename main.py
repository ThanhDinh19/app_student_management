from tkinter import *
from database import *

def add():
    line = id.get()+" - "+name.get()+" - "+year.get()
    save(line)
    show()

def show():
    sv = read() 
    lbox.delete(0, END)
    for item in sv:
        lbox.insert(END, f"{item[0]+"   "+item[1]+"   "+item[2]}")
 
def arrange_decrease():
    sv = read()
    sv.sort(key = lambda x: x[2], reverse = True)
    # for i in range(len(sv)):
    #     for j in range(len(sv)):
    #         x, y  = sv[i], sv[j]
    #         if(x[2] > y[2]):
    #             sv[i], sv[j] = y, x
    lbox.delete(0, END)
    for item in sv:
        lbox.insert(END, f"{item[0]+"   "+item[1]+"   "+item[2]}")
             


root = Tk()
root.geometry("500x630")
root.title("Student management")
root.iconbitmap('logo_student.ico')

id = StringVar()
name = StringVar()
year = StringVar()

lb = Label(root, text = "STUDENT MANAGEMENT", font = ("Arial", 30), fg = "Red", bg = "#FFFFFF")
lb.grid(row = 0)


lbox = Listbox(root, width = 80, height = 20)
lbox.grid(row=1)
show()

lb1 = Label(root, text = "Student id: ", font = ("Arial", 13))
lb1.place(x=10, y = 390)
lb2 = Label(root, text = "Name: ", font = ("Arial", 13))
lb2.place(x=10, y = 420)
lb3 = Label(root, text = "Year of birth: ", font = ("Arial", 13))
lb3.place(x=10, y = 450)


et1 = Entry(root, width = 30, textvariable=id)
et1.place(x = 160, y = 392)
et2= Entry(root, width = 30, textvariable=name)
et2.place(x = 160, y = 422)
et3= Entry(root, width = 30, textvariable=year)
et3.place(x = 160, y = 452)


button = Frame(root)
Button(button, text="Add", command=add).pack(side=LEFT)
Button(button, text="Watch", command=show).pack(side=LEFT)
Button(button, text="Arrange", command=arrange_decrease).pack(side=LEFT)
Button(button, text="Exit", command=root.quit).pack(side=LEFT)
button.place(x=100, y = 520)

root.mainloop()