import sqlite3

conn=sqlite3.connect('test.db')

c=conn.cursor()

c.execute("""CREATE TABLE testt(
            name text,
            phone integer
            )""")

conn.commit()
conn.close()