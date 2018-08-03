import pytest
from ast import literal_eval

# 배워보고 싶다~!
class TestIf():

    #[문제1] 조건문1
    # 홍길동씨는 5,000원의 돈을 가지고 있고 카드는 없다고 한다. 이러한 홍길동씨의 상태는 아래와 같이 표현할 수 있을 것이다.
    # >>> money = 5000
    # >>> card = False
    # 홍길동씨는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하고 있거나 4,000원 이상의 현금을 가지고 있어야 한다고 한다.
    # 홍길동씨는 택시를 탈 수 있는지를 판별할 수 있는 조건식을 작성하고 그 결과를 출력하시오.

    def test_quiz1(self):
        money = 5000
        card = False
        result = self.CanUseTaxi(money, card)
        assert True == result

        money = 100
        card = True
        assert  True == self.CanUseTaxi(money, card)

        money = 0
        card = False
        assert  False == self.CanUseTaxi(money, card)

    def CanUseTaxi(self, cash: int, card: bool) -> bool:
        return (cash >= 4000 or card == True)




    # [문제2] 조건문2
    # 홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다.
    # >>> lucky_list = [1, 9, 23, 46]
    # 홍길동씨가 당첨되었다면 “야호”라는 문자열을 출력하는 프로그램을 작성하시오.

    def test_quiz2(self):

        myLotto = [1,9, 23,46]
        Result = self.CheckLotto(myLotto)
        assert True == Result;

        yourLotto = [1,2,3,4,5]
        assert False == self.CheckLotto(yourLotto)

    def CheckLotto(self, myLotto) -> bool:
        return 23 in myLotto

    # [문제3] 홀수 짝수 판별
    # 주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.
    def test_quiz3(self):
        assert False == self.IsEven(1)
        assert True == self.IsEven(2)
        assert True == self.IsEven(0)
        assert type(1) is int
        assert False == self.IsEven("Two")


    def IsEven(self, param):
        if(type(param) is not int):
            return False
        return param%2 == 0



    # [문제4] 문자열 분석
    # 다음 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.
    # 나이:30,키:180
    def test_quiz4(self):
        assert "No" == self.IsYoungAndSexy('age:30,height:180')
        assert "Yes" == self.IsYoungAndSexy('age:29,height:180')
        assert "Yes" == self.IsYoungAndSexy('age:29,height:179')

    def IsYoungAndSexy(self, param : str) -> str:
        temp = param.split(",")
        age = temp[0].split(":")[-1]
        height = temp[1].split(":")[-1]
        if int(age) < 30 and int(height) >= 175:  # 문자열을 숫자로 바꾸어 비교해야 한다.
            return "Yes"
        else:
            return "No"


    # [문제5] 조건문3
    # 다음 코드의 결과값은 무엇일까?
    # >>> a = "Life is too short, you need python"
    # >>> if 'wife' in a:
    # ...     print('wife')
    # ... elif 'python' in a and 'you' not in a:
    # ...     print('python')
    # ... elif 'shirt' not in a:
    # ...     print('shirt')
    # ... elif 'need' in a:
    # ...     print('need')
    # ... else:
    # ...     print('none')
    def test_quiz5(self):
        assert 'shirt' == self.YouNeed("Life is too short, you need python")


    def YouNeed(self, param : str) -> str:
        if 'wife' in param:
            return 'wife'
        elif 'python' in param and 'you' not in param:
            return 'python'
        elif 'shirt' not in param:
            return 'shirt'
        elif 'need' in param:
            return 'need'
        else:
            return 'none'

