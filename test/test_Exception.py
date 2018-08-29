import pytest

# 배워보고 싶다~!
class TestException():

    def test_useRisesForThrowExceptionType(self):
        with pytest.raises(IndexError):
            a = [1,2,3]
            b = a[4]

    def test_raises2(self):
        with pytest.raises(ZeroDivisionError):
             b = 1/0

    def test_MyExcept(self):
        with pytest.raises(IOError):
            reader = MyIO()
            reader.throwIOError('blah')

    def test_MyExcept2(self):
        with pytest.raises(ZeroDivisionError):
            reader = MyIO()
            reader.throwDivideError(1,0)

    def test_MyExcept3(self):
        reader = MyIO()
        assert 2 == reader.notThrowDivideError(2, 1)
        assert "you fool!" == reader.notThrowDivideError(1,0)

    def test_quiz4(self):
        sumFunc = lambda a, b : a+b

        io =MyIO()
        assert  9 == io.quiz4Method(sumFunc(1,2))

    def test_quiz5(self):
        io = MyIO()
        indexErrorFunc = lambda a: a[10]
        with pytest.raises(IndexError):
            io.quiz4Method(indexErrorFunc([1,2,3]))



class MyIO():

    def throwIOError(self, filename: str):
        open(filename)

    def throwDivideError(self, number:int, div : int):
        return number/div

    def notThrowDivideError(self, number:int, div : int):
        try:
            return number/div
        except ZeroDivisionError:
            return "you fool!"


    def quiz4Method(self, func):
        result = 0
        try:
            func
        except TypeError:
            result += 1
        except ZeroDivisionError:
            result += 2
        except IndexError:
            result += 3
        else:
            result += 4
        finally:
            result += 5

        return result

