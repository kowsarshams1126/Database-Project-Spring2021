from os import name
import tkinter as tk
import sqlite3
import datetime
from functools import partial
#from notif_query import addNotif_likeOrReplyComment
from notif_query import addNotif_likeOrReplyComment,addNotif_comment


def comment_page(userLoginId,postId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    window = tk.Tk()
    window.title="Comments"
    input_comment = tk.Entry(window)
    input_comment.pack()
    tk.Button(window, text="creat new comment",
              command=partial(creat_comment, userLoginId, postId, input_comment)).pack()
    tk.Label(window, text="*********************************************************************").pack()
    tk.Label(window, text="comments of this post are:").pack()
    tk.Label(window, text="---------------------------------------------------------------------").pack()
    

   
    res = cur.execute(f'select * from comment where comment_id not in(select comment_id2 from reply_comment) and post_id="{postId}"').fetchall()
    print(res)
    for i in range(0 , len(res)):


        tk.Label(window, text=res[i][1]).pack() #date comment
        print(res[i][4])
        nameUser = find_name_by_id(res[i][4])

        tk.Label(window, text=nameUser).pack()
        tk.Label(window, text=res[i][2]).pack() #content of comment
        tk.Button(window, text="like",command=lambda: like_comment(userLoginId,res[i][0])).pack()
        tk.Button(window, text="view replies and creat a reply for this comment", command=lambda: reply_page(userLoginId,res[i][0], postId)).pack()
        tk.Label(window, text="**********************************************").pack()



    window.geometry('600x600')
    window.mainloop()
    con.commit()
    con.close()

def find_name_by_id(id):
    print(id)
    print("LLLLLLLLLLLLLLLLLLLLL")
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    res = cur.execute(f'select name from user where user_id="{id}"').fetchall() #find name of user who sent the comment
    nameUser = res[0][0]
    con.commit()
    con.close()
    return nameUser

def creat_comment(userLoginId, postId, input_comment):
    con = sqlite3.connect('linkedin_db.db')

    cur = con.cursor()

    cur.execute("INSERT INTO comment (date, content, post_id, user_id ) VALUES(?,?,?,?)",
                (datetime.date.today(), input_comment.get(), postId, userLoginId), )
    user_id2 = cur.execute(f'select user_id from post where post_id="{postId}"').fetchall()[0][0]

    con.commit()
    con.close()
    addNotif_comment(userLoginId,user_id2)


def like_comment(userLoginId, commentId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    a=cur.execute(f'select * from like_comment where user_id="{userLoginId}" and comment_id="{commentId}"').fetchall()
    if len(a)==0:
        res = cur.execute(f'insert into like_comment(user_id, date, comment_id) values ("{userLoginId}","{datetime.date.today()}","{commentId}")')
        user_id2=cur.execute(f'select user_id from comment where comment_id="{commentId}"').fetchall()[0][0]
        con.commit()
        con.close()
        addNotif_likeOrReplyComment(userLoginId,user_id2)

def reply_page(userLoginId, commentId, postId):

    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    window2 = tk.Tk()
    window2.title="replies"
    input_reply = tk.Entry(window2)
    input_reply.pack()
    tk.Button(window2, text="creat new reply",
              command=partial(create_reply, userLoginId, commentId, postId, input_reply)).pack()
    tk.Label(window2, text="*********************************************************************").pack()
    tk.Label(window2, text="replies of this comment are:").pack()
    tk.Label(window2, text="---------------------------------------------------------------------").pack()
    res2 = cur.execute(f'select * from comment where comment_id in (select comment_id2 from reply_comment where comment_id1="{commentId}")' ).fetchall()


    for j in range(0, len(res2)):
    
        tk.Label(window2, text=res2[j][1]).pack() #date comment

        nameUser = find_name_by_id(res2[j][4])

        tk.Label(window2, text=nameUser).pack()
        tk.Label(window2, text=res2[j][2]).pack() #content of comment
        tk.Button(window2, text="like",command=lambda: like_comment(userLoginId,res2[j][0])).pack()
        tk.Button(window2, text="view replies and creat a reply for this comment", command=lambda: reply_page(userLoginId,res2[j][0], postId)).pack()
        tk.Label(window2, text="**********************************************").pack()




    window2.geometry('600x600')
    window2.mainloop()

def create_reply(userLoginId, commentId, postId, input_reply):

    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()

    res =cur.execute("SELECT comment_id FROM comment WHERE comment_id = (SELECT MAX(comment_id) FROM comment)").fetchall()
    res = cur.execute(
        "SELECT comment_id FROM comment WHERE comment_id = (SELECT MAX(comment_id) FROM comment)").fetchall()
    # print(res[0][0]+1)
    res2 = cur.execute("INSERT INTO comment (date, content, post_id, user_id ) VALUES(?,?,?,?)",
                       (datetime.date.today(), input_reply.get(), postId, userLoginId), )
    # res2 = cur.execute(f'insert into comment(date, content, post_id, user_id ) values ("{datetime.date.today()}","{"its comment for comment"}","{postId}" ,"{userLoginId}")')
    res3 = cur.execute(f'insert into reply_comment(comment_id1, comment_id2) values ("{commentId}", "{res[0][0] + 1}")')
    # compute primarykey of user2


    user_id2 = cur.execute(f'select user_id from comment where comment_id="{commentId}"').fetchall()[0][0]
    con.commit()
    con.close()
    print("meow")
    addNotif_likeOrReplyComment(userLoginId,user_id2)


#
# def main():
#     comment_page(1,1)
#     print("hi")
# if __name__ == "__main__":
#     main()
    

