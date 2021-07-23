import sqlite3
from tkinter import *
# global UID
import profile
import my_network

from home import home

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()


def checkInDB2(username1, password):
    res = cur.execute(f'select user_id from user where username="{username1}" and password="{password}"').fetchall()
    print(res)
    return False if len(res) == 0 else True


def Authentication(loginpage, username1, password):
    global UID
    loginpage.destroy()
    if checkInDB2(username1, password):
        UID = username1
        home(UID)
    else:
        login(True)


def checkInDB(username, email):
    res = cur.execute(f'select user_id from user where name="{username}" or email="{email}"').fetchall()
    print(res)
    print("LLLLLLLLLLLLLLLLLLLLLLLL")
    return False if len(res) == 0 else True


def sendData2DB_NEWACCOUNT(newAccount, username, password, email,loginPage):
    global UID
    newAccount.destroy()
    print(checkInDB(username, password))
    if (not checkInDB(username, email)):
        print("WHY")
        print(cur.execute(
            f'insert into user(name,password,email,username) values ("{username}","{password}","{email}","{username}") '))
        con.commit()
        UID = username
        loginPage.destroy()
        home(UID)
        return True
    else:
        Create(True,loginPage)
        return False


def Create(flag,loginPage):
    # loginPage.destroy()
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
                                                           emailInput.get(),loginPage))
    submit.grid(row=4, column=1)
    newAccount.mainloop()


def login(flag):
    global username
    loginPage = Tk("500x5000")
    usernameLabel = Label(loginPage, text='username')
    passwordLabel = Label(loginPage, text='password')
    username = StringVar()
    password = StringVar()
    usernameInput = Entry(loginPage, textvariable=username)
    passwordInput = Entry(loginPage, show="*", textvariable=password)
    lab = Label(loginPage,
                text="Wrong username or password! Please Retry." if flag else "                                               ")
    lab.grid(row=0, column=2)
    usernameLabel.grid(row=1, column=1)
    passwordLabel.grid(row=2, column=1)
    usernameInput.grid(row=1, column=2)
    passwordInput.grid(row=2, column=2)
    loginButton = Button(loginPage, text='Sign in',
                         command=lambda: Authentication(loginPage, username.get(), password.get()))
    signUpButton = Button(loginPage, text='Sign up', command=lambda: Create(False,loginPage))
    loginButton.grid(row=3, column=1)
    signUpButton.grid(row=3, column=2)
    # username=username.get()
    # password=password.get()
    print(username)
    print(password)
    loginPage.mainloop()
