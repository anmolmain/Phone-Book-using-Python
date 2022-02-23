from tkinter import *
from tkinter import font
from tkinter import ttk
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='contacts_projects')
myCursor=mydb.cursor()

"""
------SQL-------
show databases;
create database contacts_projects;
use contacts_projects;
#or use mini_projects;

create table contactdata(
contactname varchar(50)NOT NULL,
countrycode varchar(4)NOT NULL ,
contactnum varchar(10)primary key
);

"""


root=Tk()
root.geometry('1280x720+35+5')
root.config(background='wheat')
root.title('Phonebook')
root.resizable(False,False)
titlePhonebook=Label(root,text="Phonebook",font=('times new roman',35,'bold'),width=46,bg='indianred',fg='wheat')
titlePhonebook.place(x=0,y=0)

def addContact():
    name=NameEntry.get()
    if len(name)==0:
        AddedLabel.config(text=f'Some information is Incorrect , Please Recheck')
    else:
        number=NumberEntry.get()
        country=countryCode.get()
        try:
            int(int(NumberEntry.get()))
            print(name,country,number)
            val=(name,country,number)
            global myCursor
            query='insert into contactdata (contactname,countrycode,contactnum) values(%s,%s,%s)'
            myCursor.execute(query,val)
            global mydb
            mydb.commit()
            AddedLabel.config(text='Number added successfully')
            NumberEntry.delete('0',END)
            NameEntry.delete('0',END)
            countryCode.delete('0',END)
            oldContacts()            
        except:
            AddedLabel.config(text=f'Some information is Incorrect , Please Recheck')

Name=Label(root,text="Name of Contact",font=('times new roman',35,'bold'),bg='indianred',fg='wheat')
Name.place(x=25,y=100)
NameEntry=Entry(root,font=('times new roman',25,'bold'))
NameEntry.place(x=25,y=180)

country=Label(root,text="Country Code",font=('times new roman',35,'bold'),bg='indianred',fg='wheat')
country.place(x=500,y=100)
countryCode=Entry(root,font=('times new roman',25,'bold'),width=5)
countryCode.place(x=600,y=180)

Number=Label(root,text="Contact Number",font=('times new roman',35,'bold'),bg='indianred',fg='wheat')
Number.place(x=900,y=100)
NumberEntry=Entry(root,font=('times new roman',25,'bold'))
NumberEntry.place(x=900,y=180)

btnAdd=Button(root,text="Add",font=('times new roman',23,'bold'),width=15,height=1,command=addContact)
btnAdd.place(x=935,y=250)

def oldContacts():
    myCursor.execute('select * from contactdata order by contactname')
    btnOld.config(text='Refresh')
    rows=myCursor.fetchall()
    tv=ttk.Treeview(root,columns=(1,2,3),show='headings')
    tv.pack()
    tv.heading(1,text="Name")
    tv.heading(2,text="Country Code")
    tv.heading(3,text="Number")
    for i in rows:
        tv.insert('',END,values=i)
    tv.place(x=330,y=455)
    # new.mainloop()
creditBar=Label(root,text="Made By : Anmol Main ",font=('times new roman',15,'bold'),width=110,bg='indianred',fg='wheat')
creditBar.place(x=0,y=690)
        
btnOld=Button(root,text="All Contacts",font=('times new roman',23,'bold'),width=15,height=1,command=oldContacts)
btnOld.place(x=50,y=250)

def reset():
    NumberEntry.delete('0',END)
    NameEntry.delete('0',END)
    countryCode.delete('0',END)
    NumberEntrynxt.delete('0',END)
    AddedLabel.config(text='')

Reset=Button(root,text=" Reset ",font=('times new roman',23,'bold'),width=15,height=1,command=reset)
Reset.place(x=500,y=250)

AddedLabel=Label(root,text="",font=('times new roman',35,'bold'),width=46,bg='indianred',fg='wheat')
AddedLabel.place(x=0,y=350)

def deleteFromDb():
        val=NumberEntrynxt.get()
        global myCursor
        query=f"delete from contactdata where contactnum={val}"
        # print(val)
        try:
            myCursor.execute(query)
            global mydb
            mydb.commit()
            # print('done')
            AddedLabel.config(text=f'Record Deleted successfully')
            NumberEntrynxt.delete('0',END)
            oldContacts()
        except:
                AddedLabel.config(text=f'Some information is Incorrect , Please Recheck')

delLabel=Label(root,text="Enter Contact number of Record  to delete: ",font=('times new roman',15,'bold'),width=40,bg='indianred',fg='wheat')
delLabel.place(x=0,y=420)
delLabel=Label(root,text="permanently delete record",font=('times new roman',15,'bold'),width=35,bg='indianred',fg='wheat')
delLabel.place(x=860,y=420)

NumberEntrynxt=Entry(root,font=('times new roman',17,'bold'),width=15)
NumberEntrynxt.place(x=500,y=420)
finalBtn=Button(root,text="Delete",font=('times new roman',11,'bold'),width=15,height=1,command=deleteFromDb)
finalBtn.place(x=700,y=420)

root.mainloop()