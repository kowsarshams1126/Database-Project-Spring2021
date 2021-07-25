import sqlite3
import datetime

from itertools import chain

import notif_query
from direct_query import people_in_network


#########################################################################################

def insert_like_post(user_id,post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    notif_query.addNotif_likePost(user_id,post_id)
    cur.execute(f'insert into like_post(date,post_id,user_id) values ("{datetime.datetime.now()}","{post_id}","{user_id}")')
    con.commit()
#########################################################################################
def get_number_of_like(post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT like_post_id FROM like_post WHERE post_id=?
                     ''',(post_id,)).fetchall()

    con.commit()
    con.close()
    return len(data)

def get_number_of_comment(post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT comment_id FROM comment WHERE post_id=?
                     ''',(post_id,)).fetchall()

    con.commit()
    con.close()
    return len(data)


#########################################################################################

def get_username(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT username FROM user WHERE user_id=?
                     ''',(user_id,)).fetchall()

    con.commit()
    con.close()
    return data

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

#############################################################################################
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

def network_shared_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    people=people_in_network(user_id)
    people_data=[]
    for item in people:
        people_data.append(item[0])
        
    sql='''SELECT post.post_id,post.user_id,post.content,post.date,
                        share_post.user_id,share_post.comment,share_post.date
                        FROM post,share_post 
                        WHERE post.post_id=share_post.post_id AND share_post.user_id IN ({seq})'''.format(seq=','.join(['?']*len(people_data)))

    data=cur.execute(sql, people_data).fetchall()
    
    con.commit()
    con.close()
    return data


def network_like_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    people=people_in_network(user_id)
    people_data=[]
    for item in people:
        people_data.append(item[0])
        
    sql='''SELECT post.post_id,post.user_id,post.content,post.date
                        FROM post,like_post 
                        WHERE post.post_id=like_post.post_id AND like_post.user_id IN
                      ({seq})''' .format(seq=','.join(['?']*len(people_data)))

    data=cur.execute(sql, people_data).fetchall()
    
    con.commit()
    con.close()
    return data


def network_comment_post_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    people=people_in_network(user_id)
    people_data=[]
    for item in people:
        people_data.append(item[0])
        
    sql='''SELECT post.post_id,post.user_id,post.content,post.date
                        FROM post,comment 
                        WHERE post.post_id=comment.post_id AND comment.user_id IN
                        ({seq})''' .format(seq=','.join(['?']*len(people_data)))

    data=cur.execute(sql, people_data).fetchall()
    
    con.commit()
    con.close()
    return data


#########################################################################################
