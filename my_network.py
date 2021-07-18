import tkinter as tk
from functools import partial
from network_query import invitation_data,connection_data,people_know_data,insert_invitation,accept_invitation,reject_invitation

def invitation_page(user_id):
    
    inv_data=invitation_data(user_id)
    window = tk.Tk()
    window.title("INVITATION")
    for item in inv_data:
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="accept",command=partial(accept_invitation,user_id, item[0])).pack()
        tk.Button(window, text="reject", command=partial(reject_invitation,user_id, item[0])).pack()
        tk.Label(window, text="------------------").pack()

    window.geometry('400x400')
    window.mainloop()

def people_know_page(user_id):
    
    know_data=people_know_data(user_id)
    window = tk.Tk()
    window.title("PEOPLE YOU MAY KNOW")
    for item in know_data:
        tk.Label(window, text=item[1]).pack()
        # tk.Button(window, text="view",command=lambda: view_a_user(user_id, item[0])).pack()
        tk.Button(window, text="invitation", command=partial(insert_invitation,user_id, item[0])).pack()
        tk.Label(window, text="------------------").pack()

    window.geometry('400x400')
    window.mainloop()
    
def connection_page(user_id):
    conn_data=connection_data(user_id)
    window = tk.Tk()
    window.title("CONNECTIOIN")
    for item in conn_data:
        tk.Label(window, text=item[1]).pack()
        # tk.Button(window, text="view",command=partial(view,user_id,item[0])).pack()
        tk.Label(window, text="------------------").pack()

    window.geometry('400x400')
    window.mainloop()
    
def my_network_page(user_id):

    window = tk.Tk()
    window.title("MY NETWORK")
    tk.Button(window, text="connection",command=lambda: connection_page(user_id)).pack()
    tk.Button(window, text="invitation",command=lambda: invitation_page(user_id)).pack()
    tk.Button(window, text="people you may khow", command=lambda: people_know_page(user_id)).pack()
    window.geometry('400x400')
    window.mainloop()
    
def main():
    my_network_page(3);

main()