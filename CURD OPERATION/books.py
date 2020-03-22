from tkinter import Tk,Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk,PhotoImage,Canvas
from tkinter import messagebox
import mysql.connector
#from sqlserver_Config import dbConfig
#import pypyodbc as pyo
#con=pyo.connect(**dbConfig)
import turtle
import cx_Oracle
#con=pyo.connect(**dbconfig)
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shivam")
cursor=con.cursor()
#cursor.execute("create table booktime(id int,Title varchar(25),Author varchar(25),Mobile_No double(10) ,Email varchar(25))");
class Bansh:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shivam")
        self.cursor=con.cursor()
        print("Data base ready to connection you can do Something")
        print(con)
    def __del__(self):
        self.con.close()
    def view(self):
        self.cursor.execute("SELECT * FROM book_time")
        rows=self.cursor.fetchall()
        return rows
    def insert(self,title,author,mobile,email):
        sql=("Insert into book_time(Title,Author,Mobile_No,Email)Values(?,?,?,?)");
        values=[title,author,mobile,email]
        self.cursor.execute(sql,values)
        self.con.commit()
        massagebox.showinfo(Title="Book DATA BASE",massage="new book are add in data base")

    def update(self,title,author,mobile,email):
        tsql='UPDATE books Set title=?,author=?,mobile=?,email=?'
        self.cursor.execute(tsql,[title,author,mobile,email])
        self.con.commit()
        massagebox.showinfo(title="Book dATA BASE",massage="new book update in databse")

    def delete(self,title):
        delquery='Delete from book_time where title=?'
        self.cursor.execute(delquery,[title])
        self.con.commit()
        massagebox.showinfo(title="Book DATA BASE",massage="a book delet in database")
    def clear_all(self):
        Csql='truncate from book_time'
        self.cursor.execute(Csql)
        self.con.commit()
        massagebox.showinfo(massage="All Clear Data in data base")
jp=Bansh()
def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)
    title_entry.delete(0,'end')
    title_entry.insert('end',selected_tuple[0])
    author_entry.delete(0,'end')
    author_entry.insert('end',selected_tuple[1])
    mobile_entry.delete(0,'end')
    mobile_entry.insert("end",selected_tuple[2])
    email_entry.delete(0,'end')
    email_entry.insert('end',selected_tuple[3])
def viewRecord():
    list_box.delete(0,'end')
    for row in jp.view():
        list_box.insert('end',row)
def Click():
    #jp.insert('end',title_text.get(),author_text.get(),mobile_text.get(),email_text.get())
    list_box.delete(0,'end')
    list_box.insert('end',title_text.get(),author_text.get(),mobile_text.get(),email_text.get())
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    mobile_entry.delete(0,'end')
    email_entry.delete(0,'end')
    con.cmmit()
def delete():
    global selected_tuple
    jp.delete(selected_tuple[0])
    con.commit()
def clear_All():
    list_box.delete(0,'end')
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    mobile_entry.delete(0,'end')
    email_entry.delete(0,'end')
    con.commit()
def update():
    global selected_tuple
    list_box=(selected_tuple[0],title.get(),author.get(),mobile.get(),emial.get())
    title_entry.delete(0,'end')
    aurhor_entry.delete(0,'end')
    mobile_entry.delete(0,'end')
    email_entry.delete(0,'end')
    con.commit()
def Exit():
    dd=jp
    if messagebox.askokcancel("Quit","Do you wnat to quit"):
       root.destroy()
       del dd
root=Tk()
root.title("this is my library Concept")
root.configure(background="pink")
p=root.geometry("400x400")

#root.resizable(width=False,height=False)
#photo=PhotoImage(file="leah3.gif")
#window=turtle.Screen()
#window.bgpic("leah3.gif")
#canvas=Canvas(height=600,width=800,bg="pink")
#canvas.pack()
photo=PhotoImage(file="dish1.gif")
#p.create_image(0,0,image=photo)
title_label=ttk.Label(root,text="Title",background="light green",font=("TkDefaultFont",30))
title_label.grid(row=0,column=0,sticky=W)
title_text=StringVar()
title_entry=ttk.Entry(root,width=20,textvariable=title_text)
title_entry.grid(row=0,column=1,sticky=W)
author_label=ttk.Label(root,text="Author",background="light green",font=("TkDefaultFont",30))
author_label.grid(row=0,column=2,sticky=W)
author_text=StringVar()
author_entry=ttk.Entry(root,width=20,textvariable=author_text)
author_entry.grid(row=0,column=3,sticky=W)
mobile_label=ttk.Label(root,text="Mobile No",background="light green",font=("TkDefaultFont",30))
mobile_label.grid(row=0,column=4,sticky=W)
mobile_text=StringVar()
mobile_entry=ttk.Entry(root,width=20,textvariable=mobile_text)
mobile_entry.grid(row=0,column=5,sticky=W)
email_label=ttk.Label(root,text="Email",background="light green",font=("TkDefaultFont",30))
email_label.grid(row=0,column=6,sticky=W)
email_text=StringVar()
email_entry=ttk.Entry(root,width=20,textvariable=email_text)
email_entry.grid(row=0,column=7,sticky=W)
btn=Button(root,text="Click",background="red",font=("TkDefaultFont",20),command=Click)
btn.grid(row=0,column=8,sticky=W,padx=10)
list_box=Listbox(root,height=16,width=40,background="pink",font=("TkDefaultFont",10))
list_box.grid(row=3,column=1,columnspan=8,sticky=W+E,pady=40,padx=15)
list_box.bind('<<ListboxSelect>>',get_selected_row)
scrollbar = Scrollbar(root)
scrollbar.grid(row=1,column=10,rowspan=8,sticky=W)
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)
btn1=Button(root,text="viewRecord",background="pink",font=("TkDefaultFont",20),command=viewRecord)
btn1.grid(row=4,column=4,sticky=W,padx=10)
btn2=Button(root,text="update",background="pink",font=("TkDefaultFont",20),command=update)
btn2.grid(row=4,column=5,sticky=W,padx=5)
btn3=Button(root,text="Delete",background="light green",font=("TkDefaultFont",20),command=delete)
btn3.grid(row=4,column=6,sticky=W,padx=5)
btn4=Button(root,text="Clear_All",background="white",font=("TkDefaultFont",20),command=clear_All)
btn4.grid(row=4,column=7,sticky=W,padx=5)
btn5=Button(root,text="Exit",background="red",font=("TkDefaultFont",20),command=Exit)
btn5.grid(row=4,column=8,sticky=W,padx=5)
root.mainloop()
