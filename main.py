
import sqlite3
from login import login
from profile import profile_mainPage
import login as lg

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()
userId=""

login(False)
print("******")
print(1)
profile_mainPage(1)
















login(False)


