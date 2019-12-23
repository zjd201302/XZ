##Python work with SQLite: https://www.youtube.com/watch?v=pd-0G0MigUA

import sqlite3

conn = sqlite3.connect('Test_DB.db')

c = conn.cursor()

c.execute("select * from INV_sum ")

##def read_from_db():
##    c.execute("select * from INV ")
####    data = c.fetchall()
####    print(data)
##
##    for row in c.fetchall():
##        print(row)

##print(c.fetchall())
##print(c.fetchone())

for row in c.fetchall():
    print(row)

conn.commit()

conn.close()
