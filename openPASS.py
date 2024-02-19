from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
root = Tk()     
root.title("OpenPASS")
def add_password():
    name = nameentry.get()
    account = accountentry.get()
    password = passwordentry.get()
    db = "Account: "+ account + " User: "+ name + " Password: " + password
    f = open(account + ".dat", "w")
    f.write(db + "\n")

def get_password():
    account = accountentry.get()
    f = add_password()
    f = open(account + ".dat", "r")
    print(f.read())
nameentry = ttk.Entry()
namelabel = ttk.Label(text="User ")
accountlabel = ttk.Label(text="Account ")
passwordlabel = ttk.Label(text="Password ")
passwordentry = ttk.Entry()
addbtn = ttk.Button(text="Add...", command=add_password)
getbtn = ttk.Button(text="Get...", command=get_password)
accountentry = ttk.Entry()

addbtn.grid(row=1, column=0, sticky='e')
getbtn.grid(row=2, column=0)
accountlabel.grid(row=1, column=1)
accountentry.grid(row=1, column=2)
nameentry.grid(row=2, column = 2)
namelabel.grid(row=2,column=1)
passwordlabel.grid(row=3,column=1)
passwordentry.grid(row=3, column=2)


root.mainloop()