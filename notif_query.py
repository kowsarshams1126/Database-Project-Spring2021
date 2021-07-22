import sqlite3
from datetime import datetime

from network_query import find_mutual_connection, connection_data

def addNotif_birthday(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    res = cur.execute(
        f'select notification_id from notification where type=1 and user_idT="{user_id}" and user_idR="{param}" and date="{datetime.date.today()}"').fetchall()
    if len(res) == 0:
        cur.execute(
            f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{1}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()

def addNotif_viewProfile(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    res = cur.execute(
        f'select notification_id from notification where type=2 and user_idT="{user_id}" and user_idR="{param}"').fetchall()
    if len(res) == 0:
        cur.execute(
            f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{2}","{user_id}","{param}","{datetime.date.today()}")')
    
    else:
        cur.execute(
            f'update notification set read="{0}",date="{datetime.date.today()}" where notification_id="{res[0][0]}"')
        con.commit()
    con.close()


def addNotif_likePost(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(
        f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{3}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()


def addNotif_comment(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(
        f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{4}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()


def addNotif_likeOrReplyComment(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(
        f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{5}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()

def addNotif_endorse(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(
        f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{6}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()

def addNotif_changePosition(user_id, param):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    cur.execute(
        f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{6}","{user_id}","{param}","{datetime.date.today()}")')
    con.commit()
    con.close()


