import pytest

# 배워보고 싶다~!
class TestBool():

    def test_TrueFalse(self):
        assert 0 == False;
        assert 1 == True;

    def test_EmptyCollection_Is_False(self):
        #Set
        result  = 0
        if(False == {}):
            result = 1
        else :
            result = 2
        assert 2 == result

        #list
        if (False == []):
            result = 3
        else:
            result = 4
        assert 4 == result

        #Tuple/Dic
        if (False == {}):
            result = 5
        else:
            result = 6
        assert 6 == result



    #[문제1] 불 자료형과 조건문
    #다음은 불 자료형을 리턴하는 조건문들이다. 각 각의 예제의 결과가 어떻게 나오는지 예상해 보자.
    # >>> 1 != 1
    # >>> 3 > 1
    # >>> 'a' in 'abc'
    # >>> 'a' not in [1, 2, 3]
    def test_Quiz1(self):
        assert False == (1 != 1)
        assert True == (3 > 1)
        assert True == ('a' in 'abc')
        assert True == ('a' not in [1,2,3])
