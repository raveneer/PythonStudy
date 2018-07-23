from unittest import TestCase
import Hello

class TestHello(TestCase):
    def test_Summer(self):
        self.assertEqual(3, Hello.Summer(1, 2))

    def test_MixedCalc(self):
        self.assertEqual(9, Hello.MixedCalc(1,2,3))
