import sqlite3
class Database:
    def __init__(self, db): #__init__ -> initializer,self-> "this" feature in other Language
        self.conn =sqlite3.connect(db) #conn(kinda variable) -> property ,connect -> connects with database
        self.cur = self.conn.cursor() #cursor -> executes queries
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text ,price text)")
        self.conn.commit()

    def fetch(self):# fetch-> takes data
        self.cur.execute("SELECT * FROM parts")# * -> all
        rows = self.cur.fetchall()#fetchall -> forthis instance select all rows
        return rows

    def insert(self,part,customer,retailer,price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))# NULL,? -> protection from SQL injection
        self.conn.commit()

    def remove(self,id):
        self.cur.execute=("DELETE FROM parts WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ? , customer = ? , retailer = ? , price = ? WHERE id=?",(part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):# kinda destructor
        self.conn.close()

    