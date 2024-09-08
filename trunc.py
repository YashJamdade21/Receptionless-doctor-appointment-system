import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("TRUNCATE TABLE appointments")
conn.commit()