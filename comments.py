from os import name
import tkinter as tk
import sqlite3
import datetime
from notif_query import addNotif_likeOrReplyComment


def show_comments(userLoginId,postId):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()


    window = tk.Tk()
    window.title="Comments"

    tk.Label(window, text="comments of this post:").pack()
    tk.Label(window, text="*********************************************************************").pack()

    res = cur.execute(f'select * from comment where post_id="{postId}"').fetchall()
    # print(re)
    printedComments=[]
    
    for i in range(0 , len(res)):
        #if this comment was reply to a comment
        res2 = cur.execute(f'select * from reply_comment where comment_id2="{res[i][0]}"').fetchall() #it means a comment that is in reply comment too as a comment that a comment reply to it
        
        for j in range(0 , len(res2)):
            res3 = cur.execute(f'select * from comment where comment_id="{res2[j][1]}"').fetchall() # find the comment that has reply in comment table
            
            tk.Label(window, text=res3[j][1]).pack() #date comment

            nameUser = find_name_by_id(res3[j][4])

            tk.Label(window, text=nameUser).pack()
            tk.Label(window, text=res3[j][2]).pack() #content of comment
            tk.Button(window, text="like",command=lambda: like_comment(userLoginId,res3[j][0])).pack()
            tk.Button(window, text="reply", command=lambda: reply_comment(userLoginId,res3[j][0],postId)).pack()
            tk.Label(window, text="**********************************************").pack()
            tk.Label(window, text="replies to this comment are:").pack()
            printedComments.append(res3[j][0])
            print(printedComments[j])
    

            print("part")
            #res5 = cur.execute(f'select * from reply_comment where comment_id2="{res2[j][2]}"').fetchall()

            res4 = cur.execute(f'select * from comment where comment_id="{res2[j][2]}"').fetchall() #accsess to comments of comment in comment 
            
                
            for t in range(0, len(res4)):

                tk.Label(window, text=res4[t][1]).pack() #date comment
                print("part2")

                nameUser2 = find_name_by_id(res4[t][4])

                tk.Label(window, text=nameUser2).pack()
                tk.Label(window, text=res4[t][2]).pack() #content of comment
                tk.Button(window, text="like",command=lambda: like_comment(userLoginId,res4[t][0])).pack()
                tk.Button(window, text="reply", command=lambda: reply_comment(userLoginId,res4[t][0],postId)).pack()
                tk.Label(window, text="**********************************************").pack()
                printedComments.append(res4[t][0])
                print("done")
       
        #comments that dont have comment and are not comments of a comment
    for k in range(0, len(res)):
        if res[k][0] not in printedComments:

            tk.Label(window, text=res[k][1]).pack() #date comment

            nameUser3 = find_name_by_id(res[k][4])

            tk.Label(window, text=nameUser3).pack()
            tk.Label(window, text=res[k][2]).pack() #content of comment
            tk.Button(window, text="like",command=lambda: like_comment(userLoginId,res[k][0])).pack()
            tk.Button(window, text="reply", command=lambda: reply_comment(userLoginId,res[k][0],postId)).pack()
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
    user_id2=cur.execute(f'select user_id from comment where comment_id="{commentId}"').fetchall()[0][0]
    con.commit()
    con.close()
    addNotif_likeOrReplyComment(userLoginId,user_id2)


def reply_comment(userLoginId, commentId, postId):
    window2 = tk.Tk()
    window2.title="reply"
    input = tk.Entry(window2).pack()
   


    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()

    res =cur.execute("SELECT comment_id FROM comment WHERE comment_id = (SELECT MAX(comment_id) FROM comment)").fetchall()
    #print(res[0][0]+1)

    res2 = cur.execute(f'insert into comment(date, content, post_id, user_id ) values ("{datetime.date.today()}","{input.get()}","{postId}" ,"{userLoginId}")')
    res3 = cur.execute(f'insert into reply_comment(comment_id1, comment_id2) values ("{commentId}", "{res[0][0]+1}")')
    # primarykey of user2= res[0][0] +1 

    window2.geometry('200x200')
    window2.mainloop()
    con.commit()
    con.close()


def main():
    show_comments(0,2)
    print("hi") 
if __name__ == "__main__":
    main()  
    

