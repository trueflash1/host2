import sqlite3 as sq
 
con = sq.connect("db.sqlite3")
cur = con.cursor()

# cur.execute("""CREATE TABLE SPRAV_NAME (
#     name TEXT,
#     descriptionm TEXT
# )""")
cur.execute("""DELETE FROM SPRAV_NAME WHERE name = 'oneee'""")
con.commit()
con.close()