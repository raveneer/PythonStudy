from PythonStudy import Hello


# https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test

class TestHello():
    def test_Simple(self):
        assert  1==1

    def test_Summer(self):
        assert Hello.Summer(1, 2) == 3

    def test_MixedCalc(self):
        assert Hello.MixedCalc(1, 2, 3) == 9
