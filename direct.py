import tkinter as tk
from functools import partial
from direct_query import *

################################################################################

def all_chat_page(user_id):
    #get_data
    people=get_all_chat_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("ALL CHAT")
    for item in people:
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="open",command=partial(chat_page, user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()
    
    window.geometry('400x400')
    window.mainloop()
    

def unread_chat_page(user_id):
    people=get_unread_chat_data(user_id)
    
    window = tk.Tk()
    window.title("ALL UNREAD CHAT")
    
    for item in people:
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="open",command=partial(chat_page, user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()
    
    window.geometry('400x400')
    window.mainloop()
    

def archive_chat_page(user_id):
    people=get_archive_chat_data(user_id)
    
    window = tk.Tk()
    window.title("ALL ARCHIVE CHAT")
    
    for item in people:
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="open",command=partial(chat_page, user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()
    
    window.geometry('400x400')
    window.mainloop()
    
################################################################################

def chat_page(user_idT,user_idR):
    #make_chat_status_read
    change_read_status(user_idT,user_idR,1)
    #get data
    messages=get_messages(user_idT,user_idR)
    chat_status =get_chat_status(user_idT,user_idR)
    #tk view
    window = tk.Tk()

    if chat_status[0][0]==1:
        tk.Button(window, text="unread",command=partial(change_read_status,user_idT,user_idR,0)).pack()
    if chat_status[0][0]==0:
        tk.Button(window, text="read",command=partial(change_read_status,user_idT,user_idR,1)).pack()
    if chat_status[0][1]==1:
        tk.Button(window, text="unarchive",command=partial(change_archive_status,user_idT,user_idR,0)).pack()
    if chat_status[0][1]==0:
        tk.Button(window, text="archive",command=partial(change_archive_status,user_idT,user_idR,1)).pack()

    tk.Button(window, text="delete",command=partial(delete_conversation,user_idT,user_idR)).pack()
    tk.Label(window, text="--------------------------------------").pack()

    for item in messages:
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[0]).pack()
        tk.Label(window, text=item[1]).pack()
        tk.Label(window, text="--------------------------------------").pack()

    text=tk.Entry(window)    
    text.pack()
    tk.Button(window, text="send",command=partial(send_message,user_idT,user_idR,text)).pack()

    window.geometry('400x400')
    window.mainloop()

#############################################################################
def select_new_chat_page(user_id):
    #get_data
    people = people_in_network(user_id)
    #tk view 
    window = tk.Tk()
    window.title("PEOPLE IN YOUR NETWORK")
    
    for item in people:
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="select",command=partial(add_new_chat, user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()
    
    window.geometry('400x400')
    window.mainloop()
    
def add_new_chat(user_idT,user_idR):
    insert_new_conversation(user_idT,user_idR)
    chat_page(user_idT, user_idR)

#############################################################################
def direct_page(user_id):
    
    window = tk.Tk()
    window.title("DIRECT")
    tk.Button(window, text="all chat",command=partial(all_chat_page,user_id)).pack()
    tk.Button(window, text="unread chat",command=partial(unread_chat_page,user_id)).pack()
    tk.Button(window, text="archive chat",command=partial(archive_chat_page,user_id)).pack()
    tk.Button(window, text="new chat",command=partial(select_new_chat_page,user_id)).pack()
    window.geometry('400x400')
    window.mainloop()

#############################################################################
def main():

    direct_page(1)

main()