#sql: structured query language

import sqlite3


conn=sqlite3.connect("oyos.db")

conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT,ADDRESS TEXT,PRICE INT,AMENITIES TEXT,RATING TEXT)")

print("Table created successfully")

conn.execute("INSERT INTO OYO_HOTELS (NAME,ADDRESS,PRICE,AMENITIES,RATING) VALUES ('Oyo1','Oyo1_street',450,'bath,kitchen','Good')")

cur=conn.cursor()

cur.execute("SELECT * FROM OYO_HOTELS")

table_data=cur.fetchall()

for record in table_data:
    print(record)