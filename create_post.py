import datetime
import sqlite3
from tkinter import *

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()


def send_post(string_val, user_id,create_post):
    print(datetime.date.today())
    cur.execute(f'insert into post(content,date,user_id) values("{string_val.get()}","{datetime.date.today()}","{user_id}")')
    con.commit()
    create_post.destroy()


def create_post(user_id):
    create_post=Tk()
    create_post.geometry("500x500")
    lf=LabelFrame(create_post,text="text")
    string_val=StringVar(lf)
    content=Entry(lf,textvariable=string_val)
    lf.grid(row=1,column=1)
    content.grid(row=1,column=1)
    submit_button=Button(create_post,text="Send Post!",command=lambda :send_post(string_val,user_id,create_post))
    submit_button.grid(row=2,column=1)
    create_post.mainloop()
