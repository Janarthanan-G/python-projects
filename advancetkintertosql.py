from tkinter import *
import mysql.connector
from tkinter import ttk


db=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Janarthanan@1812',
    database='Registration'
  
)

mydata = db.cursor()


def next_action():
    first=e1.get()
    mid=e2.get()
    last=e3.get()
    phone=ph.get()
    alter=Al.get()
    gender=var.get()
    age=w.get()
    course=CB.get()

    sql = ("INSERT INTO person (f_name ,m_name ,l_name,phone ,alter_ph,gender,age ,course)values(%s,%s,%s,%s,%s,%s,%s,%s)")
    val=(first,mid,last,phone,alter,gender,age,course)
    print(val)
    mydata.execute(sql,val)
    db.commit()

    


master=Tk()
master.title('Registration From')
master.config(bg="#cccccc")
frame=Frame(master)
frame.pack()
     
Label(frame, text='First Name :').grid(row=3, column=1, sticky=W)
Label(frame, text='Mid Name :').grid(row=3, column=3, sticky=E)
Label(frame, text='Last Name :').grid(row=3, column=5, sticky=E)
e1 = Entry(frame)
e2 = Entry(frame)
e3 = Entry(frame)
e1.grid(row=3, column=2, padx=10, pady=10)
e2.grid(row=3, column=4, padx=10, pady=10)
e3.grid(row=3, column=6, padx=10, pady=10)
Label(frame,text='Phone No :').grid(row=4,column=1)
ph =Entry(frame)
ph.grid(row=4,column=2,padx=10,pady=10)
Label(frame,text='Alternate No :').grid(row=5,column=1)
Al =Entry(frame)
Al.grid(row=5,column=2,padx=10,pady=10)
Label(frame, text="Gender :").grid(row=6, column=1, padx=10, pady=10)
var = StringVar()
Radiobutton(frame, text='Male', variable=var, value='Male').grid(row=6, column=2)
Radiobutton(frame, text='Female', variable=var, value='Female').grid(row=6, column=3)
Label(frame,text="Age :").grid(row=6, column=5, padx=10, pady=10)
w = Spinbox(frame, from_=0, to=35)
w.grid(row=6,column=6,padx=10,pady=10)
    
Label(frame,text='Course Name :').grid(row=8,column=1)
CB=ttk.Combobox(frame, values=["","python","java","C++","Data science","Cloud","AI&ML","Any other"])

CB.grid(row=8, column=2, padx=10, pady=10)
Label(frame,text="Course :").grid(row=9,column=1)
Checkbutton(frame, text='PYTHON').grid(row=9, column=2, sticky=W)
Checkbutton(frame, text='SQL').grid(row=10, column=2, sticky=W)
Checkbutton(frame, text='JAVA').grid(row=11, column=2, sticky=W)
Checkbutton(frame, text='PHP').grid(row=12, column=2, sticky=W)
Checkbutton(frame, text='UI/UX').grid(row=13, column=2, sticky=W)
  
    

Button(frame, text='SUBMIT', width=10, command=next_action).grid(row=16, column=3, padx=10, pady=10)
 
mainloop()