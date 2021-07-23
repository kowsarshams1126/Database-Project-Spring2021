import sqlite3
import datetime

from itertools import chain

from direct_query import people_in_network


#########################################################################################
def get_my_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT post_id,user_id,content,date FROM post WHERE user_id=?
                     ''',(user_id,)).fetchall()

    con.commit()
    con.close()
    return data  

def get_my_shared_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT post.post_id,post.user_id,post.content,post.date,
                        share_post.user_id,share_post.comment,share_post.date
                        FROM post,share_post 
                        WHERE post.post_id=share_post.post_id AND share_post.user_id=?
                     ''',(user_id,)).fetchall()

    con.commit()
    con.close()
    return data 

def network_create_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    people=people_in_network(user_id)
    print(people)
    people_data=[]
    for item in people:
        people_data.append(item[0])
        
    sql="SELECT post_id,user_id,content,date FROM post WHERE user_id IN  ({seq})".format(
    seq=','.join(['?']*len(people_data)))

    data=cur.execute(sql, people_data).fetchall()
    print(people_data)
    
    con.commit()
    con.close()
    return data
#########################################################################################
def insert_like_post(user_id,post_id):
    pass