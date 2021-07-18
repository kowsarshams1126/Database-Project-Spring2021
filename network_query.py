import sqlite3

def invitation_data(user_id):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    data=cur.execute('SELECT user_id,username FROM user WHERE user_id IN (SELECT user_idT FROM invitation WHERE user_idR=?)',(user_id,)).fetchall()

    con.commit()
    con.close()
    return data

def insert_invitation(user_idT,user_idR):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("INSERT INTO invitation (user_idT,user_idR) VALUES(?,?)",(user_idT,user_idR,))

    con.commit()
    con.close()    

def accept_invitation(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("INSERT INTO connection (user_id1,user_id2) VALUES(?,?)",(user_id1,user_id2,))
    cur.execute("DELETE FROM invitation WHERE  user_idT=? AND user_idR=?",(user_id2,user_id1,))

    con.commit()
    con.close()

def reject_invitation(user_id1,user_id2):
    con = sqlite3.connect('linkedin_db.db')
    cur = con.cursor()
    
    cur.execute("DELETE FROM invitation WHERE user_idT=? AND user_idR=?",(user_id2,user_id1,))

    con.commit()
    con.close()


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
