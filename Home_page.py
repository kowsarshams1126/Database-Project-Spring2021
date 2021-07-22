from tkinter import *
import sqlite3
con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()
#tedad like va tedad likecomment ro too datABASE nadashtim  age lazem darim felan ye global gereftam
#button ha kamel nist hanooz
numOfLikes = 0
numOfreplike = 0
    
def like_post():
    global numOfLikes
    numOfLikes+=1
    likeLabel.config(text="Likes: {}".format(numOfLikes))
    postLike.config(text=" ")
    cur.execute("""CREATE TABLE IF NOT EXISTS like_pst(
    like_post_id integer PRIMARY KEY,
    date DATE,
    post_id INT,
    user_id INT
    );
    """)
    con.commit()
    
    cr.execute("""INSERT INTO comment(content, date) 
    VALUES('GETDATE()');""")
    con.commit()
##vaghti like mishe bayad tedad likehay ghabli ro update kone pas:


##notification
##posti ke like karde bere too home page networkihash
    
    
    
def comment():
    
    cur.execute("""CREATE TABLE IF NOT EXISTS comment(
    comment_id integer PRIMARY KEY,
    content TEXT,
    date DATE,
    post_id INT
    );
    """)
    con.commit()

    cur.execute("""INSERT INTO comment(content, date) 
    VALUES('{textcomment.get()}', 'GETDATE()');""")
    con.commit()
    
##notification
##posti ke comment barash gozashte shode bere to safhe Home networks


def like_reply():
    global numOfreplike
    numOfreplike=+1
    likeLabel2.config(text="Likes: {}".format(numOfLikes))
    commentLike.config(text=" ")
    cur.execute("""CREATE TABLE IF NOT EXISTS like_comment(
    like_comment_id integer PRIMARY KEY,
    comment_id INT,
    date DATE
    user_id INT
    );
    """)
    con.commit()
    
    cur.execute("""INSERT INTO like_comment(date) 
    VALUES('GETDATE()');""")
    con.commit()
##just notification
    
    
    



def reply_comment():
    cur.execute("""CREATE TABLE IF NOT EXISTS reply_comment(
    reply_comment_id integer PRIMARY KEY,
    comment_id1 INT,
    comment_id INT
    );
    """)
    con.commit()
    
#age notification lazem dare


Home = Tk()
Home.title("Home")


likeLabel = Label(Home, text="Likes: ")
likeLabel.pack()
likeLabel2 = Label(Home, text="Likes: ")
likeLabel2.pack()

textComment = Entry(Home)

postLike = Button(Home, text="Like", command=like_reply)
postLike.pack()
commentLike = Button(Home, text="Like", command=like_reply)
commentLike.pack()

Home.geometry("600x480")
Home.mainloop()

