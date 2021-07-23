import tkinter as tk
from direct import direct_page
from my_network import my_network_page
from functools import partial
from profile import profile_mainPage,show_notifs
from search_page import search_page
from post import post_page


def home(user_id):
    print(user_id)
    window = tk.Tk()
    window.title("HOME")
    tk.Button(window, text="direct",command=partial(direct_page,user_id)).pack()
    tk.Button(window, text="network",command=partial(my_network_page,user_id)).pack()
    tk.Button(window, text="my profile",command=partial(profile_mainPage,user_id)).pack()
    tk.Button(window, text="search people",command=partial(search_page,user_id)).pack()
    tk.Button(window, text="post",command=partial(post_page,user_id)).pack()
    tk.Button(window, text="notification",command=partial(show_notifs,user_id)).pack()
    window.geometry('400x400')
    window.mainloop()

