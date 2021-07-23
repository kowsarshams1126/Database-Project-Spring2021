from os import name
import tkinter as tk
import sqlite3
import datetime

#correct without UI

def show_comments(postId,userLoginId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()


    window = tk.Tk()
    window.title="Comments"

    tk.Label(window, text="comments of this post:").pack()
    tk.Label(window, text="*********************************************************************").pack()

    res = cur.execute(f'select * from comment where post_id="{postId}"').fetchall()
    
    
    
    for i in range(0 , len(res)):

       
        tk.Label(window, text=res[i][1]).pack() #date comment

        nameUser = find_name_by_id(res[i][4])

        tk.Label(window, text=nameUser).pack()
        tk.Label(window, text=res[i][2]).pack() #content of comment
        tk.Button(window, text="like",command=like_comment(userLoginId,res[i][0])).pack()
        tk.Button(window, text="reply", command=reply_comment(userLoginId,res[i][0],postId)).pack()
        tk.Label(window, text="**********************************************").pack()
    
    con.commit()
    con.close()




    window.geometry('600x600')
    window.mainloop()

def find_name_by_id(id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    res = cur.execute(f'select name from user where user_id="{id}"').fetchall() #find name of user who sent the comment
    nameUser = res[0][0]
    con.commit()
    con.close()
    return nameUser

def like_comment(userLoginId, commentId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    res = cur.execute(f'insert into like_comment(user_id, date, comment_id) values ("{userLoginId}","{datetime.date.today()}","{commentId}")')

    con.commit()
    con.close()

def reply_comment(userLoginId, commentId, postId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()

    res =cur.execute("SELECT comment_id FROM comment WHERE comment_id = (SELECT MAX(comment_id) FROM comment)").fetchall()
    #print(res[0][0]+1)

    res2 = cur.execute(f'insert into comment(date, content, post_id, user_id ) values ("{datetime.date.today()}","{"its comment for comment"}","{postId}" ,"{userLoginId}")')
    res3 = cur.execute(f'insert into reply_comment(comment_id1, comment_id2) values ("{commentId}", "{res[0][0]+1}")')
    #compute primarykey of user2

    con.commit()
    con.close()


def main():
    show_comments(0,1)
    print("hi") 
if __name__ == "__main__":
    main()  
    

