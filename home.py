import tkinter as tk
from direct import direct_page
from my_network import my_network_page
from functools import partial


def home(user_id):
    
    window = tk.Tk()
    window.title("DIRECT")
    tk.Button(window, text="direct",command=partial(direct_page,user_id)).pack()
    tk.Button(window, text="network",command=partial(my_network_page,user_id)).pack()
    
    tk.Button(window, text="my profile",command=partial(all_chat_page,user_id)).pack()
    tk.Button(window, text="search",command=partial(archive_chat_page,user_id)).pack()
    tk.Button(window, text="post",command=partial(select_new_chat_page,user_id)).pack()
    tk.Button(window, text="notification",command=partial(select_new_chat_page,user_id)).pack()
    window.geometry('400x400')
    window.mainloop()
