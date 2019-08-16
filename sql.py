import sqlite3
con = sqlite3.connect("database.db")
con.execute("""CREATE TABLE customer_comp(
                    Firstname text,
                    Lastname text,
                    invoice text,
                    date integer,
                    product text) """)
print("table success")
con.close()