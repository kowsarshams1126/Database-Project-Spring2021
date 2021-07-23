import datetime
import sqlite3
import notif_query


from network_query import connection_data

# this func return num of likes of a post
def numOfLikes(post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    num=cur.execute(f'select count(like_post_id) as cnt from like_post group by post_id having post_id="{post_id}"').fetchall()[0][0]
    return num

#this func all contents of comments
def comments(post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    comments=cur.execute(f'select * from comment group by post_id having post_id="{post_id}"').fetchall()[0]
    return comments

#this func all contents of comments
def numOfComments(post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    num=cur.execute(f'select count(comment_id) as cnt from comment group by post_id having post_id="{post_id}"').fetchall()[0][0]
    return num

# this func return all of posts datas
def my_post(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    my_posts=cur.execute(f'select * from post group by user_id having user_id="{user_id}"').fetchall()[0]
    return my_posts

# this func return sll of contents whose id is in connection_data
def others_posts(user_id):
    posts=[]
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    for user in connection_data(user_id):
        posts.append(cur.execute(f'select * from post group by user_id having user_id="{user[0]}"').fetchall()[0])
        posts.append(cur.execute(f'select * from share_post group by user_id having user_id="{user[0]}"').fetchall()[0])

    return posts

def like_post(user_id,post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    notif_query.addNotif_likePost(user_id,post_id)
    cur.execute(f'insert into like_post(date,post_id,user_id) values ("{datetime.date.today()}","{post_id}","{user_id}")')
    con.commit()

def share_post(text_val,user_id,post_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(f'insert into share_post(date,comment,post_id,user_id) values ("{datetime.date.today()}","{text_val.get()}","{post_id}","{user_id}")')
    con.commit()

