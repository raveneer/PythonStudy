import pytest
from ast import literal_eval


# 배워보고 싶다~!
class TestFor():

    # range를 쓰면 쉽게 c#의 for와 비슷한 형태로 사용할 수 있다.
    def test_forWithRange(self):
        result = 0

        for number in range(1, 11):
            result += number

        assert 55 == result

        # range는 마지막이 잘리는 것에 주의.
        assert 1 in range(1, 10)
        assert 10 not in range(1, 10)

    # 리스트 내포를 이용해서 람다 비스무리하게 만들수도 있다.
    # 그러나... 가독성이? 리스트 안에서 이터레이션 해버리는 것이 과연 잘하는 짓인지는?  (프로그래밍의 차수를 확인하기 어려워)
    def test_ListInFor(self):
        a = [1, 2, 3]
        result = [number * 3 for number in a]
        assert [3, 6, 9] == result

        # 안 쓴다면 이렇게 될 것이다... 위에 것 보다 장황하긴 하지만 뭐 하는지 알아보기는 쉽지. 흠... 익숙해지는 것의 문제일지?
        result2 = []
        for number in a:
            result2.append(number * 4)
        assert [4, 8, 12] == result2

    # [문제1] 1부터 100까지 출력
    # 1부터 100까지의 숫자를 for문을 이용하여 출력하시오.
    def test_quiz1(self):
        result = 0
        for number in range(1, 101):
            result += number
        assert 5050 == result

    # [문제2] 5의 배수의 총합
    # for문을 이용하여 1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하시오.
    def test_quiz2(self):
        assert 0 == self.SumOf5Multiple(0, 1);
        assert 5 == self.SumOf5Multiple(0, 5);
        assert 15 == self.SumOf5Multiple(0, 10);
        assert 100500 == self.SumOf5Multiple(0, 1000);

    def SumOf5Multiple(self, start, endInclude) -> int:
        result = 0

        for number in range(start, endInclude + 1):
            if (number % 5 == 0):
                result += number

        return result

    # [문제3] 학급의 평균 점수
    # for문을 이용하여 A 학급의 평균 점수를 구해 보자.
    # A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    def test_quiz3(self):
        assert 0 == self.GetAverage([0, 0, 0])
        assert 1 == self.GetAverage([0, 0, 3])
        assert 3 == self.GetAverage([3, 3, 3])
        assert 79 == self.GetAverage([70, 60, 55, 75, 95, 90, 80, 80, 85, 100])

    def GetAverage(self, collection: list) -> int:
        result = 0
        for point in collection:
            result += point
        result /= len(collection)
        return result

    # [문제4] 혈액형
    # 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다.
    # ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
    # for 문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.
    def test_quiz4(self):
        bloods = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'A', 'B', 'B', 'B']
        assert 4 == self.GetBloodsCount(bloods, 'A')
        assert 6 == self.GetBloodsCount(bloods, 'B')
        assert 3 == self.GetBloodsCount(bloods, 'O')
        assert 2 == self.GetBloodsCount(bloods, 'AB')

    def GetBloodsCount(self, bloods, checkingBloodType):
        result = 0
        for bloodType in bloods:
            if (bloodType == checkingBloodType):
                result += 1

        return result

    # [문제5] 리스트 내포1
    # 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.
    # numbers = [1, 2, 3, 4, 5]
    # result = []
    # for n in numbers:
    #     if n % 2 == 1:
    #         result.append(n*2)
    # 위 코드를 리스트 내포(list comprehension)를 이용하여 표현하시오.
    def test_quiz5(self):
        numbers = [1, 2, 3, 4, 5]
        result = []
        for n in numbers:
            if n % 2 == 1:
                result.append(n * 2)
        assert [2, 6, 10] == result

        # 가능하긴 한데... 음청 지저분하구마
        result2 = [(number * 2) for number in numbers if (number % 2 == 1)]
        assert [2, 6, 10] == result2

    # [문제6] 리스트 내포2
    # 리스트 내포를 이용하여 다음 문장에서 모음('aeiou')을 제거하시오.
    # Life is too short, you need python
    def test_quiz6(self):
        text = 'Life is too short, you need python'
        result = ''.join([char for char in text if (not 'aeiou'.__contains__(char))])
        assert result == 'Lf s t shrt, y nd pythn'
