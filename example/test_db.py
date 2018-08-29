import sqlite3
import pytest
import example.SQLiteExample


class TestDBController():
    def test_connect(self):
        db_controller = example.SQLiteExample.DBController()
        db_controller.connect()
        assert None is not db_controller.con
