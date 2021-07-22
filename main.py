
import sqlite3
from login import login
from profile import profile_mainPage
import login as lg
import search

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()
login(False)
# search.search(1,"","","","",0)
#

