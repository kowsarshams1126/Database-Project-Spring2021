import tkinter as tk
from functools import partial
from network_query import invitation_data,connection_data,people_know_data,insert_invitation,accept_invitation,reject_invitation

def view_a_user(user_id1,user_id2):
    pass

#####################################################################################################
def invitation_page(user_id):
    #get data 
    inv_data=invitation_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("INVITATION")
    counter=0
    #item[0]=user_id, item[1]=username
    for item in inv_data:
        counter=counter+1
        tk.Label(window, text=str(counter)+"- "+item[1]).pack()
        tk.Label(window, text=item[1]).pack()
        tk.Button(window, text="view",command=lambda: view_a_user(user_id, item[0])).pack()
        tk.Button(window, text="accept",command=partial(accept_invitation,user_id, item[0])).pack()
        tk.Button(window, text="reject", command=partial(reject_invitation,user_id, item[0])).pack()
        tk.Label(window, text="------------------").pack()
    window.geometry('400x400')
    window.mainloop()

#####################################################################################################
def people_know_page(user_id):
    #get data
    know_data=people_know_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("PEOPLE YOU MAY KNOW")
    counter=0
    #item[0]=user_id, item[1]=username
    for item in know_data:
        counter=counter+1
        tk.Label(window, text=str(counter)+"- "+item[1]).pack()
        tk.Button(window, text="view",command=lambda: view_a_user(user_id, item[0])).pack()
        tk.Button(window, text="invitation", command=partial(insert_invitation,user_id, item[0])).pack()
        tk.Label(window, text="------------------").pack()
    window.geometry('400x400')
    window.mainloop()
    
#####################################################################################################
def connection_page(user_id):
    #get data 
    conn_data=connection_data(user_id)
    #tk-view
    window = tk.Tk()
    window.title("CONNECTIOIN")
    counter=0
    #item[0]=user_id, item[1]=username
    for item in conn_data: 
        counter=counter+1
        tk.Label(window, text=str(counter)+"- "+item[1]).pack()
        tk.Button(window, text="view",command=lambda: view_a_user(user_id, item[0])).pack()
        tk.Label(window, text="------------------").pack()
    window.geometry('400x400')
    window.mainloop()
    
#####################################################################################################
def my_network_page(user_id):

    window = tk.Tk()
    window.title("MY NETWORK")
    tk.Button(window, text="connection",command=lambda: connection_page(user_id)).pack()
    tk.Button(window, text="invitation",command=lambda: invitation_page(user_id)).pack()
    tk.Button(window, text="people you may khow", command=lambda: people_know_page(user_id)).pack()
    window.geometry('400x400')
    window.mainloop()

#####################################################################################################    
def main():
    my_network_page(1);

main()