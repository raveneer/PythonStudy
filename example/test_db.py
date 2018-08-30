import sqlite3
import pytest
import example.SQLiteExample


class TestDBController():
    def test_connect(self):
        db_controller = example.SQLiteExample.DBController()
        db_controller.connect()
        assert None is not db_controller.con

    # def test_make_table(self):
    #     db_controller = example.SQLiteExample.DBController()
    #     db_controller.connect()
    #     db_controller.create_table()

    # def test_add_data(self):
    #     db_controller = example.SQLiteExample.DBController()
    #     db_controller.connect()
    #     db_controller.add_data()

    def test_fetch_one(self):
        db_controller = example.SQLiteExample.DBController()
        db_controller.connect()
        one_book = db_controller.select_fetch_one()
        assert '호빗' == one_book[0]
        assert '톨킨' == one_book[1]

    def test_fetch_all(self):
        db_controller = example.SQLiteExample.DBController()
        db_controller.connect()
        all_book = db_controller.select_fetch_all()
        assert list == type(all_book)
        assert ('반지전쟁', '톨킨', '몰라', '2017-01-01', '0000') == list[0]

