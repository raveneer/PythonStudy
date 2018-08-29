import pytest
from ast import literal_eval

# 배워보고 싶다~!
class TestWile():

    #[문제1] 1부터 100까지 더하기
    #1부터 100까지의 자연수를 모두 더하고 그 결과를 출력하시오.
    def test_quiz1(self):
        assert 3 == self.GetTotalSum(1, 2)
        assert 5050 == self.GetTotalSum(1, 100)
        assert 2 == self.GetTotalSum(-1, 2)


    #[문제2] 3의 배수의 합
    #1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오.
    def test_quiz2(self):
        assert 0 == self.GetSumOf3Multiple(0,1)
        assert 3 == self.GetSumOf3Multiple(0, 3)
        assert 9 == self.GetSumOf3Multiple(0, 6)
        assert 9 == self.GetSumOf3Multiple(3, 6)
        assert 3 == self.GetSumOf3Multiple(3, 5)
        assert 166833 == self.GetSumOf3Multiple(1, 1000)


    #[문제3] 50점 이상의 총합
    #다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.
    #A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
    def test_quiz3(self):
        assert 0 == self.GetSumOfGoodPoint([0], 0)
        assert 1 == self.GetSumOfGoodPoint([0,1], 1)
        assert 2 == self.GetSumOfGoodPoint([0, 1, 2], 2)
        assert 3 == self.GetSumOfGoodPoint([0, 1, 2], 1)
        assert 426 == self.GetSumOfGoodPoint([5, 67, 82, 45, 33, 90, 87, 100, 25], 50)

    #[문제4] 별 표시하기1
    #
    #while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
    #*
    #**
    #***
    #****
    def test_quiz_drawStars1(self):
        starts = self.GetStarList(5)
        assert starts[0] == '*'
        assert starts[1] == '**'
        assert starts[2] == '***'
        assert starts[3] == '****'
        assert starts[4] == '*****'

    def GetStarList(self, length):
        result = list()
        i = 0
        while True:
            i += 1  # while문 수행 시 1씩 증가
            if i > 5: break  # i 값이 5보다 크면 while문을 벗어난다.
            result.append('*' * i)  # i 값 개수만큼 *를 출력한다.

        return result


    def GetTotalSum(self, start, end) -> int :
        startNumber = start
        result = 0
        while(startNumber <= end):
            result += startNumber
            startNumber += 1

        return result



    def GetSumOf3Multiple(self, start:int, end:int) -> int :
        result = 0
        index = start

        while(index <= end):
            if(index %3 == 0):
                result += index

            index += 1

        return result

    def GetSumOfGoodPoint(self, points : list, goodPointThrethHold):
        result = 0

        for point in points:
            if(point >= goodPointThrethHold):
                result += point

        return result






