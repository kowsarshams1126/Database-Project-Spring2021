import sqlite3
import numpy as np

###########################################################################
def connection_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                     SELECT user_id,username FROM user WHERE user_id IN
                     (
                     SELECT user_id1 FROM connection WHERE user_id2=?
                     UNION
                     SELECT user_id2 FROM connection WHERE user_id1=?
                     )
                     ''',(user_id,user_id,)).fetchall()

    con.commit()
    con.close()
    return data    

def find_mutual_connection(user_id1,user_id2):
    data1=connection_data(user_id1)
    data2=connection_data(user_id2)
    data1_con=[]
    data2_con=[]
    
    for i in data1:
        data1_con.append(i[0])
        
    for i in data2:
        data2_con.append(i[0])
    
    data1_conn=np.array(data1_con)
    data2_conn=np.array(data2_con)

    intersect=np.intersect1d(data1_conn,data2_conn)
    print(len(intersect))
    return len(intersect)
    
###########################################################################

def people_know_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('''
                        SELECT user_id,username FROM user WHERE
                        user_id IN(
                        SELECT user_id1 as user_id FROM connection WHERE user_id2 IN (

                        SELECT user_id FROM user
                            WHERE user_id IN (
                                    SELECT user_id1 AS user_id
                                        FROM connection
                                        WHERE user_id2 = ?
                                    UNION
                                    SELECT user_id2 AS user_id
                                        FROM connection
                                        WHERE user_id1 = ?
                                )

                        )
                        UNION 
                        SELECT user_id2 as user_id FROM connection WHERE user_id1 IN (

                            SELECT user_id
                            FROM user
                            WHERE user_id IN (
                                    SELECT user_id1 AS user_id
                                        FROM connection
                                        WHERE user_id2 = ?
                                    UNION
                                    SELECT user_id2 AS user_id
                                        FROM connection
                                        WHERE user_id1 =?
                                )

                        )
                        )
                        AND

                        user_id NOT IN (

                            SELECT user_id
                            FROM user
                            WHERE user_id IN (
                                    SELECT user_id1 AS user_id
                                        FROM connection
                                        WHERE user_id2 = ?
                                    UNION
                                    SELECT user_id2 AS user_id
                                        FROM connection
                                        WHERE user_id1 = ?
                                )

                        )
                        AND 
                        user_id NOT IN (SELECT user_id FROM user WHERE user_id=?)

                        ''',(user_id,user_id,user_id,user_id,user_id,user_id,user_id,)).fetchall()

    con.commit()
    con.close()
    return data   


def insert_invitation(user_idT,user_idR):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    number_inv=cur.execute('SELECT count(user_idT) FROM invitation WHERE user_idR=? AND user_idT=?',(user_idR,user_idT)).fetchall()
    numbe_conr=cur.execute("SELECT count(user_id1) FROM connection WHERE (user_id1=? AND user_id2=?) OR (user_id1=? AND user_id2=?)"
                ,(user_idR,user_idT,user_idT,user_idR,)).fetchall()
    
    if number_inv[0][0]==0 and numbe_conr[0][0]==0:
        cur.execute("INSERT INTO invitation (user_idT,user_idR) VALUES(?,?)",(user_idT,user_idR,))
    else:
        print("you already send invitation to this user")
        
    con.commit()
    con.close()    

#################################################################################################################
def invitation_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('SELECT user_id,username FROM user WHERE user_id IN (SELECT user_idT FROM invitation WHERE user_idR=?)'
                     ,(user_id,)).fetchall()

    con.commit()
    con.close()
    return data

def accept_invitation(user_idR,user_idT):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    number=cur.execute("SELECT count(user_id1) FROM connection WHERE (user_id1=? AND user_id2=?) OR (user_id1=? AND user_id2=?)"
                ,(user_idR,user_idT,user_idT,user_idR,)).fetchall()
    
    if number[0][0]==0:
        cur.execute("INSERT INTO connection (user_id1,user_id2) VALUES(?,?)",(user_idR,user_idT,))
        cur.execute("DELETE FROM invitation WHERE  user_idT=? AND user_idR=?",(user_idT,user_idR,))

    else:
        print("you already accept this invitation")
        
    con.commit()
    con.close()

def reject_invitation(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("DELETE FROM invitation WHERE user_idT=? AND user_idR=?",(user_id2,user_id1,))

    con.commit()
    con.close()

#################################################################################################################