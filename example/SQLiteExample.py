import sqlite3


class DBController():

    def connect(self):
        self.con = sqlite3.connect("db.sqlite")
        self.cur = self.con.cursor()
