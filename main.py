from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyodbc
from Save import *
from Getallrecords import *
from Update import *

#ConnectingDatabase#

from tkinter import messagebox
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUTHUCOMPUTER;'
                      'Database=Class4c v4;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#print(

# defining the canvas

root= tk.Tk()
root.title("Class4c")
canvas1 = tk.Canvas(root, width = 900, height = 300)
canvas1.pack()



# Defining the fields and labels and validating

Name = tk.Entry (root)
canvas1.create_window(300, 10, window=Name)
label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)


Age = tk.Entry (root)
canvas1.create_window(300, 40, window=Age)
label2 = tk.Label(root, text='Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 40, window=label2)



label3 = tk.Label(root, text='Gender:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 70, window=label3)


M = IntVar()
G1 = Checkbutton(
    root, text="M", variable=M,
    onvalue=1, offvalue=0)

F = IntVar()
G2 = Checkbutton(
    root, text="F", variable=F,
    onvalue=1, offvalue=0)

canvas1.create_window(350, 70, window=G1)
canvas1.create_window(250, 70, window=G2)


Height = tk.Entry (root)
canvas1.create_window(300, 100, window=Height)
label4 = tk.Label(root, text='height in cm:')
label4.config(font=('helvetica', 10))
canvas1.create_window(195, 100, window=label4)

Weight = tk.Entry (root)
canvas1.create_window(300, 130, window=Weight)
label5 = tk.Label(root, text='weight in kg:')
label5.config(font=('helvetica', 10))
canvas1.create_window(195, 130, window=label5)

StudentId = tk.Entry (root)
canvas1.create_window(300, 160, window=StudentId)
label6 = tk.Label(root, text='StudentId:')
label6.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label6)

Activitytype = tk.Entry (root)
canvas1.create_window(300, 190, window=Activitytype)
label7 = tk.Label(root, text='Activitytype:')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 190, window=label7)


Activity = tk.Entry (root)
canvas1.create_window(500, 10, window=Activity)
label8 = tk.Label(root, text='Activity:')
label8.config(font=('helvetica', 10))
canvas1.create_window(400, 10, window=label8)

Extra = tk.Entry (root)
canvas1.create_window(500, 40, window=Extra)
label9 = tk.Label(root, text='Extra:')
label9.config(font=('helvetica', 10))
canvas1.create_window(400, 40, window=label9)

 



# Defining the buttons

Save_Button = tk.Button(text='Save',command = Save)
canvas1.create_window(500, 250, window=Save_Button)

Search_Button = tk.Button(text='Search',command=Search)
canvas1.create_window(400, 250, window=Search_Button)

Delete_Button = tk.Button(text='Delete',command=Delete)
canvas1.create_window(450, 250, window=Delete_Button)

Show_All_Records = tk.Button(text='Get all records',command=getallrecords)
canvas1.create_window(330, 250, window=Show_All_Records)

Update_Button = tk.Button(text='Update',command=create_new_window)
canvas1.create_window(260, 250, window=Update_Button)

# Defining the tree

tree=ttk.Treeview(root)
tree["columns"]=("one","two","three","four","five","six")
tree.column("#0", width=130, minwidth=270, stretch=tk.NO)
tree.column("one", width=100, minwidth=150, stretch=tk.NO)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Age",anchor=tk.W)
tree.heading("two", text="Gender",anchor=tk.W)
tree.heading("three", text="Height",anchor=tk.W)
tree.heading("four", text="Weight",anchor=tk.W)
tree.heading("five", text="StudentId",anchor=tk.W)
tree.heading("six", text="Activity",anchor=tk.W)
tree.pack()



root.mainloop()
