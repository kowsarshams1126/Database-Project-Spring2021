from tkinter import *
from tkinter import *
from datetime import datetime
import sqlite3
con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()

def after_pst():
    #p1 would remove
    like.pack()
    l2.pack()
    reply.pack()
   
def post_creation():
    #postButton would remove

    l1.pack()
    textPost.pack()
    p1.pack()
    after_pst()



    cur.execute("""CREATE TABLE IF NOT EXISTS post(
    post_id integer PRIMARY KEY,
    content TEXT,
    date DATE
    user_id INT
    );
    """)
    con.commit()

    cur.execute("""INSERT INTO post(content, date) 
    VALUES('{textpost.get()}', 'GETDATE()');""")
    con.commit()
    
##post would add to homepage of those who are in network
post = Tk()
post.title("post")




postButton = Button(post, text=" Click to add a post", command=post_creation)
postButton.pack()
l1 = Label(post, text="write your text")
textPost = Entry(post)
p1 = Button(post, text="post")
like = Button (post, text="Like")
l2 = Label(post, text="reply")
reply = Entry(post)

l2 = Label(post, text="reply")
post.geometry("600x480")
post.mainloop()
