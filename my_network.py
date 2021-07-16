import tkinter as tk
import sqlite3
from functools import partial


def invitation_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('SELECT user_id,username FROM user WHERE user_id IN (SELECT user_idT FROM invitation WHERE user_idR=?)',(user_id,)).fetchall()

    con.commit()
    con.close()
    return data

def connection_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     SELECT user_id,username FROM user WHERE user_id IN
                     (
                     SELECT user_id1 FROM connection WHERE user_id2=?
                     UNION
                     SELECT user_id2 FROM connection WHERE user_id1=?
                     )
                     ''',(user_id,user_id,)).fetchall()

    con.commit()
    con.close()
    return data    
    
def people_know_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
SELECT user_id,username FROM user WHERE
 user_id IN(
SELECT user_id1 as user_id FROM connection WHERE user_id2 IN (

SELECT user_id FROM user
     WHERE user_id IN (
               SELECT user_id1 AS user_id
                 FROM connection
                WHERE user_id2 = ?
               UNION
               SELECT user_id2 AS user_id
                 FROM connection
                WHERE user_id1 = ?
           )

)
UNION 
SELECT user_id2 as user_id FROM connection WHERE user_id1 IN (

    SELECT user_id
      FROM user
     WHERE user_id IN (
               SELECT user_id1 AS user_id
                 FROM connection
                WHERE user_id2 = ?
               UNION
               SELECT user_id2 AS user_id
                 FROM connection
                WHERE user_id1 =?
           )

)
)
AND

user_id NOT IN (

    SELECT user_id
      FROM user
     WHERE user_id IN (
               SELECT user_id1 AS user_id
                 FROM connection
                WHERE user_id2 = ?
               UNION
               SELECT user_id2 AS user_id
                 FROM connection
                WHERE user_id1 = ?
           )

)
AND 
user_id NOT IN (SELECT user_id FROM user WHERE user_id=?)

''',(user_id,user_id,user_id,user_id,user_id,user_id,user_id,)).fetchall()

    con.commit()
    con.close()
    return data   


def invitation_request(user_idT,user_idR):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("INSERT INTO invitation (user_idT,user_idR) VALUES(?,?)",(user_idT,user_idR,))

    con.commit()
    con.close()    

def accept_invitation(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("INSERT INTO connection (user_id1,user_id2) VALUES(?,?)",(user_id1,user_id2,))
    cur.execute("DELETE FROM invitation WHERE  user_idT=? AND user_idR=?",(user_id2,user_id1,))

    con.commit()
    con.close()

def reject_invitation(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("DELETE FROM invitation WHERE user_idT=? AND user_idR=?",(user_id2,user_id1,))

    con.commit()
    con.close()

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
        tk.Button(window, text="invitation", command=partial(invitation_request,user_id, item[0])).pack()
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
    
# def main():
#     my_network_page(1);

# main()