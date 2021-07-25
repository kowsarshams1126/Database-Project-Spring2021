import sqlite3
import datetime
from functools import partial
import tkinter as tk
from tkinter import *
import tkinter.font
from network_query import connection_data
import notif_query
from post_query import insert_like_post

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()


def share_it(user_id, post_id, sv):
    cur.execute(f'insert into share_post(user_id,post_id,comment,date) values("{user_id}","{post_id}","{sv.get()}","{datetime.datetime.now()}")')
    con.commit()


def share_post(post_id,user_id):
    page=Tk()
    post=cur.execute(f'select * from post where post_id="{post_id}"').fetchall()[0]
    sv=StringVar(page)
    comment=Entry(page,textvariable=sv)
    button=Button(page,text="Share Post!",command=lambda :share_it(user_id,post_id,sv))
    lf2=LabelFrame(page,text= "comment on:")
    lf1=LabelFrame(lf2)
    tk.Label(lf1, text=post[1]).pack()
    tk.Label(lf1, text=post[2]).pack()
    tk.Label(lf1, text=post[3]).pack()
    comment.grid(row=1,column=1)
    button.grid(row=1,column=2)
    lf2.grid(row=2,column=1)
    lf1.grid(row=1,column=1)
    page.mainloop()