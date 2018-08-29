import sqlite3


class DBController():

    def connect(self):
        self.con = sqlite3.connect("db.sqlite")
        self.cur = self.con.cursor()
        self.con.text_factory = str

    def create_table(self):
        self.cur.execute("create table hanbit_books(title varchar(100), author varchar(100), translator varchar(100), "
                         "pub_date date, isbn varchar(100))")
        self.con.commit()
