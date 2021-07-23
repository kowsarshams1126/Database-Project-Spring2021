import tkinter as tk
from direct import direct_page
from my_network import my_network_page
from functools import partial
from profile import profile


def home(user_id):
    
    window = tk.Tk()
    window.title("DIRECT")
    tk.Button(window, text="direct",command=partial(direct_page,user_id)).pack()
    tk.Button(window, text="network",command=partial(my_network_page,user_id)).pack()
    
    tk.Button(window, text="my profile",command=partial(profile,user_id)).pack()
    tk.Button(window, text="search people",command=partial(direct_page,user_id)).pack()
    tk.Button(window, text="post",command=partial(direct_page,user_id)).pack()
    tk.Button(window, text="notification",command=partial(direct_page,user_id)).pack()
    window.geometry('400x400')
    window.mainloop()

home(1)
