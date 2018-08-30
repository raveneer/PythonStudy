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

    def add_data(self):
        self.cur.execute("insert into hanbit_books values (?, ?, ?, ?, ?)",
                         ("책이름", "저자이름", "번역자이름", "2016-08-22", "12345678"))
        self.con.commit()

    def select_fetch_one(self):
        # 왜 끝에 , 를 넣고, ()로 묶어주는 것인지?
        self.cur.execute("select * from hanbit_books where author = ?", ('톨킨',))
        print(self.cur.fetchone())
        return (list(self.cur.fetchone()))

    def select_fetch_all(self):
        self.cur.execute("select * from hanbit_books where author = ?", ('톨킨',))
        result = self.cur.fetchall()
        for row in result:
            print(row)
        return (list(self.cur.fetchall()))
