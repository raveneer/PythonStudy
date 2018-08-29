import pytest


class TestLikePython():

    def test_divide_and_remainder(self):
        assert "1 2" == self.divide_nd_remainder_bad("5 3")

    def divide_nd_remainder_bad(self, input):
        a, b = map(int, input.strip().split(' '))
        return str(int(a / b)) + " " + str(int(a % b))
