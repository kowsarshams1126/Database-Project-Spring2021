import sqlite3
from tkinter import *
# global UID
import profile

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()
def checkInDB2(username, password):
    res=cur.execute(f'select user_id from user where name="{username}" and password="{password}"')
    return False if len(res)==0 else True

def Authentication(loginpage, username1, password):
    global UID
    loginpage.destroy()
    if not checkInDB2(username1, password):
        UID=username1.get()
    else:
        login(True)

def checkInDB(username, email):
    res = cur.execute(f'select user_id from user where name="{username}" or email="{email}"').fetchall()
    return True if len(res) == 0 else False
def sendData2DB_NEWACCOUNT(newAccount, username, password, email):
    global UID
    newAccount.destroy()
    if ( checkInDB(username, password)):
        print("WHY")
        print(cur.execute(f'insert into user(name,password,email) values ("{username}","{password}","{email}") '))
        con.commit()
        UID = username
        profile.profile_mainPage(UID)
        return True
    else:
        Create(True)
        return False

def Create(flag):
    newAccount = Tk()
    usernameLabel = Label(newAccount, text='username')
    passwordLabel = Label(newAccount, text='password')
    usernameInput = Entry(newAccount)
    passwordInput = Entry(newAccount, show="*")
    emailLabel = Label(newAccount, text="e-mail")
    emailInput = Entry(newAccount)
    lab = Label(newAccount,
                text="There is a user with this username or email! Please Retry." if flag else "                                               ")
    lab.grid(row=0, column=2)
    usernameLabel.grid(row=1, column=1)
    passwordLabel.grid(row=2, column=1)
    emailLabel.grid(row=3, column=1)
    usernameInput.grid(row=1, column=2)
    passwordInput.grid(row=2, column=2)
    emailInput.grid(row=3, column=2)
    submit = Button(newAccount, text='Submit',
                    command=lambda: sendData2DB_NEWACCOUNT(newAccount, usernameInput.get(), passwordInput.get(),
                                                           emailInput.get()))
    submit.grid(row=4, column=1)
    newAccount.mainloop()



def login(flag):
    global username
    loginPage=Tk("500x5000")
    usernameLabel=Label(loginPage, text='username')
    passwordLabel=Label(loginPage, text='password')
    username=StringVar()
    password=StringVar()
    usernameInput=Entry(loginPage, textvariable=username)
    passwordInput=Entry(loginPage,show="*",textvariable=password)
    lab=Label(loginPage,text= "Wrong username or password! Please Retry." if flag else "                                               ")
    lab.grid(row=0,column=2)
    usernameLabel.grid(row=1, column=1)
    passwordLabel.grid(row=2, column=1)
    usernameInput.grid(row=1,column=2)
    passwordInput.grid(row=2,column=2)
    loginButton=Button(loginPage,text='Sign in',command=lambda :Authentication(loginPage,username,password))
    signUpButton=Button(loginPage,text='Sign up',command=lambda :Create(False))
    loginButton.grid(row=3,column=1)
    signUpButton.grid(row=3,column=2)
    # username=username.get()
    # password=password.get()
    print(username)
    print(password)
    loginPage.mainloop()

