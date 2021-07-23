import sqlite3
import datetime
from my_network import connection_data,people_know_data
# from direct import chat_page
############################################################################

def search_all_chat(user_id,text):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     select content,date,f,conversation_id from message where conversation_id IN
                     (
                     SELECT conversation_id FROM conversation WHERE user_idR=?
                     UNION
                     SELECT conversation_id FROM conversation WHERE user_idT=?
                     )
                     AND content LIKE ?
                     ''',(user_id,user_id,'%'+text+'%',)).fetchall()
    
    con.commit()
    con.close()
    return data

############################################################################

def get_all_chat_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     SELECT user_id,username FROM user WHERE user_id IN
                     (
                     SELECT user_idT FROM conversation WHERE user_idR=?
                     UNION
                     SELECT user_idR FROM conversation WHERE user_idT=?
                     )
                     ''',(user_id,user_id,)).fetchall()
    
    con.commit()
    con.close()
    return data

def get_unread_chat_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     SELECT user_id,username FROM user WHERE user_id IN
                     (
                     SELECT user_idT FROM conversation WHERE user_idR=? AND conversation_id IN
                        (
                            SELECT conversation_id FROM unread WHERE user_id=?
                        )
                     UNION
                     
                     SELECT user_idR FROM conversation WHERE user_idT=? AND conversation_id IN
                        (
                            SELECT conversation_id FROM unread WHERE user_id=?
                        )
                    )''',(user_id,user_id,user_id,user_id,)).fetchall()
    
    con.commit()
    con.close()
    return data 

def get_archive_chat_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     SELECT user_id,username FROM user WHERE user_id IN
                     (
                     SELECT user_idT FROM conversation WHERE user_idR=? AND conversation_id IN
                        (
                            SELECT conversation_id FROM archive WHERE user_id=?
                        )
                     UNION
                     
                     SELECT user_idR FROM conversation WHERE user_idT=? AND conversation_id IN
                        (
                            SELECT conversation_id FROM archive WHERE user_id=?
                        )
                    )''',(user_id,user_id,user_id,user_id,)).fetchall()
    
    con.commit()
    con.close()
    return data    

#############################################################################

def people_in_network(user_id):
    final_data=[]
    data=connection_data(user_id)
    for item in data:
        final_data.append(item)
        
    data=people_know_data(user_id)
    for item in data:
        final_data.append(item)
    return final_data
    
#############################################################################

def insert_new_conversation(user_idT,user_idR):
    
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    
    is_con=cur.execute("""SELECT conversation_id FROM conversation WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)""",
                       (user_idT,user_idR,user_idR,user_idT,)).fetchall()
    if (len(is_con)==0):
        cur.execute("INSERT INTO conversation (user_idT,user_idR) VALUES(?,?)",(user_idT,user_idR,))
    else:
        print("you already have conversation with this user")
        
    con.commit()
    con.close()
    
def delete_conversation(user_idT, user_idR):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    conversation_id=cur.execute("""SELECT conversation_id FROM conversation WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)""",
                       (user_idT,user_idR,user_idR,user_idT,)).fetchall()
    
    is_delete=cur.execute('''SELECT unread_id FROM unread WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_idT,)).fetchall()

    if (len(is_delete)==0):
        cur.execute("INSERT INTO delete_con (conversation_id,user_id) VALUES(?,?)",(conversation_id[0][0],user_idT,))
    else:
        print("you already delete this conversation")

    con.commit()
    con.close()
    
#############################################################################

def get_messages(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''SELECT conversation_id FROM conversation WHERE
                     (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_id1,user_id2,user_id2,user_id1,)).fetchall()

    data_final=cur.execute('''select content,date,f,conversation_id from message where conversation_id=?''',(data[0][0],)).fetchall()
    
    con.commit()
    con.close()
    return data_final


#############################################################################

def get_chat_status(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    data=[]
    
    conversation_id=cur.execute('''SELECT conversation_id FROM conversation 
         WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_id1,user_id2,user_id2,user_id1,)).fetchall()
    
    is_unread=cur.execute('''SELECT unread_id FROM unread WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,)).fetchall()
    if len(is_unread)!=0:
        data.append([1])
    else:
        data.append([0])
        
    is_archive=cur.execute('''SELECT archive_id FROM archive WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,)).fetchall()
    if len(is_archive)!=0:
        data[0].append(1)
    else:
        data[0].append(0)
            
    is_delete =cur.execute('''SELECT delete_id FROM delete_con WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,)).fetchall()
    if len(is_delete)!=0:
        data[0].append(1)
    else:
        data[0].append(0)
            
    con.commit()
    con.close()
    return data
    

def change_read_status(user_id1, user_id2,status):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    conversation_id=cur.execute('''SELECT conversation_id FROM conversation 
        WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_id1,user_id2,user_id2,user_id1,)).fetchall()

    if status == 1:
        #make it read
        cur.execute('''DELETE FROM unread WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,))
        
    if status == 0:
        read_id=cur.execute('''SELECT unread_id FROM unread WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,)).fetchall()
        if len(read_id)==0:
            cur.execute("INSERT INTO unread (conversation_id,user_id) VALUES(?,?)",(conversation_id[0][0],user_id1,))
        
    con.commit()
    con.close()
    
def change_archive_status(user_id1, user_id2,status):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    conversation_id=cur.execute('''SELECT conversation_id FROM conversation 
        WHERE (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_id1,user_id2,user_id2,user_id1,)).fetchall()

    if status == 0:
        cur.execute('''DELETE FROM archive WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,))
        
    if status == 1:
        #make it archive
        read_id=cur.execute('''SELECT archive_id FROM archive WHERE conversation_id=? AND user_id=?''',(conversation_id[0][0],user_id1,)).fetchall()
        if len(read_id)==0:
            cur.execute("INSERT INTO archive (conversation_id,user_id) VALUES(?,?)",(conversation_id[0][0],user_id1,))
        
    con.commit()
    con.close()

###################################################################################

def send_message(user_idT,user_idR,content):
    
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()

    data=cur.execute('''SELECT conversation_id FROM conversation WHERE
                    (user_idT=? AND user_idR=?) OR (user_idT=? AND user_idR=?)''',(user_idT,user_idR,user_idR,user_idT,)).fetchall()

    user_name_transfer=cur.execute('''SELECT username FROM user WHERE user_id=?''',(user_idT,)).fetchall()
    
    cur.execute("INSERT INTO message (content,f,conversation_id,date) VALUES(?,?,?,?)",(content.get(),user_name_transfer[0][0],data[0][0],datetime.datetime.now(),))
    
    con.commit()
    con.close()

###################################################################################