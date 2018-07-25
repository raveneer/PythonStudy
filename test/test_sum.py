from unittest import TestCase
from PythonStudy import Hello

class TestHello(TestCase):
    def test_Summer(self):
        self.assertEqual(3, Hello.Summer(1, 2))

    def test_MixedCalc(self):
        self.assertEqual(2, Hello.MixedCalc(1, 2, 3))
