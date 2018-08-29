import pytest
from ast import literal_eval

# 배워보고 싶다~!
class TestWile():

    #파이썬은 인자의 앞에 *를 붙이는 걸로 여러개의 인자를 넘길 수 있다.
    #인자은 튜플로 전달된다.
    def test_UseMultipleArgs(self):
        assert 1 == self.Summer(1)
        assert 3 == self.Summer(1,2)

    def Summer(self, *args) -> int:
        result = 0
        for arg in args:
            result += arg
        return  result


    #파이썬은 결과를 여러개 보낼 수 있다. 정말? 실은 튜플로 보내는 것이다.
    #잘 쓰면 코드가 간결해질 수도. 아니면 혼돈만 낳는가?
    def test_ReturnTuple(self):
        assert ("a",1) == self.ReturnTuple()

        name, number = self.ReturnTuple()
        assert "a" == name
        assert  1 == number

    def ReturnTuple(self):
        return "a", 1


    #인자 초기값 설정은 편하고 좋다. c#과 같음.
    def test_SetDefaultArgValue(self):
        assert 1 == self.GetNumber()
        assert 2 == self.GetNumber(2)
        assert 3 == self.GetNumber(3)

    def GetNumber(self, number = 1) -> int:
        return number


    #람다를 써보자. 람다의 용법은 초 심플. 인자 : 식이면 땡.
    #굳이 함수를 만드록 싶지 않을 때 사용할 수 있다. 그러나 남용하면...!
    def test_Rambda(self):
        summer = lambda a, b : a+b
        assert 1 == summer(0,1)
        assert 2 == summer(1, 1)

        #리스트에 함수넣기. 이 경우에는 그냥 함수들이 든 리스트가 되므로, 인덱스 선언해서 써야 함. 별거아님.
        lister = [lambda a, b: a + b, lambda a, b: a * b]
        assert 3 ==  lister[0](1,2)
        assert 2 == lister[1](1,2)



    # [문제1] 홀수 짝수 판별
    # 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.
    def test_quiz1(self):
        is_odd = lambda a : a%2 == 0
        assert True == is_odd(0)
        assert True == is_odd(2)
        assert True == is_odd(4)
        assert False == is_odd(1)
        assert False == is_odd(3)
        assert False == is_odd(9)

    # [문제2] 평균값 계산
    # 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)
    def test_quiz2(self):
        assert 10 == self.GetAvg(10, 10, 10)
        assert 10 == self.GetAvg(10, 10)
        assert 10 == self.GetAvg(10, 10, 10, 10)
        assert pytest.approx(3.3, 0.1) == self.GetAvg(10, 0, 0, 2)

    def GetAvg(self, *args):
        sum = 0
        for number in args:
            sum += number
        return sum / len(args)

    # [문제3] 구구단 출력
    # 입력을 자연수 n(2부터 9까지의 자연수)으로 받았을 때, n에 해당되는 구구단을 출력하는 함수를 작성해 보자.
    def test_quiz3(self):
        assert [2,4,6,8,10,12,14,16,18] == self.GetMultiplication(2)
        assert [9, 18, 27, 36, 45, 54, 63, 72, 81] == self.GetMultiplication(9)

    def GetMultiplication(self, param):
        result = list()
        for number in range(1,10):
            result.append(number*param)

        return result

    # [문제4] 피보나치
    # 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
    # 피보나치 수열은 다음과 같은 순서로 결과값을 리턴한다.
    # fib(0) → 0 리턴
    # fib(1) → 1 리턴
    # fib(2) → fib(0) + fib(1) → 0 + 1 → 1 리턴
    # fib(3) → fib(1) + fib(2) → 1 + 1 → 2 리턴
    # fib(4) → fib(2) + fib(3) → 1 + 2 → 3 리턴
    def test_quiz4(self):
        assert 0 == self.Fibonachi(0)
        assert 1 == self.Fibonachi(1)
        assert 1 == self.Fibonachi(2)
        assert 2 == self.Fibonachi(3)
        assert 3 == self.Fibonachi(4)

    def Fibonachi(self, param):
        if(param == 0):
            return 0
        if(param == 1):
            return 1
        return self.Fibonachi(param -1) + self.Fibonachi(param -2)


    # [문제5] 5보다 큰 수만
    # 다음은 숫자들로 이루어진 리스트를 입력으로 받아 5보다 큰 수만 필터링하여 리턴해 주는 함수이다.
    # >>> def myfunc(numbers):
    # ...     result = []
    # ...     for number in numbers:
    # ...         if number > 5:
    # ...             result.append(number)
    # ...     return result
    # ...
    # >>> myfunc([2,3,4,5,6,7,8])
    # [6, 7, 8]
    # 위 함수를 lambda 함수로 변경해 보시오.
    def test_quiz5(self):
        myfilterLambda = lambda numbers : [number for number in numbers if number > 5]
        assert [6,7,8] == myfilterLambda([2,3,4,5,6,7,8])

