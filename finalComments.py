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
       
        ##comments that dont have commeny and are not comments of a comment
        #if res[i][0] not in printedComments:

            #tk.Label(window, text=res[i][1]).pack() #date comment

            #nameUser3 = find_name_by_id(res[i][4])

            #tk.Label(window, text=nameUser3).pack()
            #tk.Label(window, text=res[i][2]).pack() #content of comment
            #tk.Button(window, text="like",command=lambda: like_comment(userLoginId,res[i][0])).pack()
            #tk.Button(window, text="reply", command=lambda: reply_comment(userLoginId,res[i][0],postId)).pack()
            #tk.Label(window, text="**********************************************").pack()
    
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

    res2 = cur.execute(f'insert into comment(date, content, post_id, user_id ) values ("{datetime.date.today()}","{"its a comment from user2 for the comment that user1 has been sent to post 0"}","{postId}" ,"{userLoginId}")')
    res3 = cur.execute(f'insert into reply_comment(comment_id1, comment_id2) values ("{commentId}", "{res[0][0]+1}")')
    # primarykey of user2= res[0][0] +1 

    con.commit()
    con.close()


#def main():
    #show_comments(0,2)
    #print("hi") 
#if __name__ == "__main__":
    #main()  
    

