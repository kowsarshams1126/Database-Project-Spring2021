import tkinter as tk
from tkinter import *

import sqlite3
import datetime


from functools import partial
from my_network import connection_data,people_know_data



def people_in_network(user_id):
    final_data=[]
    data=connection_data(user_id)
    for item in data:
        final_data.append(item)
        
    data=people_know_data(user_id)
    for item in data:
        final_data.append(item)
    return final_data
    

def get_messages(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT conversation_id FROM conversation WHERE
                     (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_id1,user_id2,user_id2,user_id1,)).fetchall()

    data_final=cur.execute('''select content,date,f,conversation_id from message where conversation_id=?''',(data[0][0],)).fetchall()
    
    con.commit()
    con.close()
    return data_final
    

def all_chat_page(user_id):
    pass


def unread_chat_page(user_id):
    pass


def archive_chat_page(user_id):
    pass

def send_message(user_idT,user_idR,content):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    print(user_idT,content.get())
    data=cur.execute('''SELECT conversation_id FROM conversation WHERE
                     (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_idT,user_idR,user_idR,user_idT,)).fetchall()
 
    user_name_transfer=cur.execute('''SELECT username FROM user WHERE user_id=?''',(user_idT,)).fetchall()
    
    cur.execute("INSERT INTO message (content,f,conversation_id,date) VALUES(?,?,?,?)",(content.get(),user_name_transfer[0][0],data[0][0],datetime.datetime.now(),))
    
    con.commit()
    con.close()

def chat_page(user_idT,user_idR):
    
    messages=get_messages(user_idT,user_idR)
    
    window = tk.Tk()
    

    for item in messages:
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[0]).pack()
        tk.Label(window, text=item[1]).pack()
        tk.Label(window, text="--------------------------------------").pack()

    text=tk.Entry(window)    
    text.pack()
    tk.Button(window, text="send",command=partial(send_message,user_idT,user_idR,text)).pack()

    # window.geometry('400x400')
    window.mainloop()
    

def add_new_chat(user_idT,user_idR):
    
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    
    is_con=cur.execute("""SELECT conversation_id FROM conversation WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)""",(user_idT,user_idR,user_idR,user_idT,)).fetchall()
    print(len(is_con))
    cur.execute("INSERT INTO conversation (read,archive,user_idT,user_idR) VALUES(1,0,?,?)",(user_idT,user_idR,))

    con.commit()
    con.close()
    
    chat_page(user_idT, user_idR)
    
def select_new_chat_page(user_id):
    
    people = people_in_network(user_id)
    
    window = tk.Tk()
    window.title("PEOPLE IN YOUR NETWORK")
    for item in people:
        print(item)
        tk.Label(window, text=item[1]).pack()
        
        tk.Button(window, text="select",command=partial(add_new_chat, user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()
    
    window.geometry('400x400')
    window.mainloop()
    

def direct_page(user_id):
    
    window = tk.Tk()
    window.title("DIRECT")
    tk.Button(window, text="all chat",command=lambda: all_chat_page(user_id)).pack()
    tk.Button(window, text="unread chat",command=lambda: unread_chat_page(user_id)).pack()
    tk.Button(window, text="archive chat", command=lambda: archive_chat_page(user_id)).pack()
    tk.Button(window, text="new chat", command=lambda: select_new_chat_page(user_id)).pack()
    window.geometry('400x400')
    window.mainloop()

def main():

    direct_page(1)

main()