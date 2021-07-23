import sqlite3
import datetime
from tkinter import *

import search


def search_page(user_id):
    page=Tk()
    sv=StringVar(page)
    entry=Entry(page,textvariable=sv)
    entry.grid(row=1,column=1)
    button=Button(page,text="Search",command=lambda :search.search(user_id,sv.get(),"","","",0))
    button.grid(row=1,column=2)


    page.mainloop()