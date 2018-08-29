import pytest


# 배워보고 싶다~!
class TestStringFormant():
    def test_make_instance(self):
        a = 10
        b = 20
        c = 'tome'
        assert '10, 20, tome' == f'{a}, {b}, {c}'
