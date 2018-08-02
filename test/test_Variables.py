import pytest
from copy import deepcopy

# 배워보고 싶다~!
class TestVariables():

    #[문제1] 변수와 객체1
    # 다음 예제를 실행하고 그 결과를 설명하시오.
    # >>> a = [1, 2, 3]
    # >>> b = [1, 2, 3]
    # >>> a is b
    def test_Quiz1(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        assert False == (a is b)
        #is는 레퍼런스 비교이기 때문이다.
        # http://seorenn.blogspot.com/2011/04/python-is.html


    # [문제2] 변수와 객체2
    # 다음 예제를 실행하고 그 결과를 설명하시오.
    # >>> a = [1, 2, 3]
    # >>> b = a
    # >>> a is b
    def test_Quiz2(self):
        a = [1, 2, 3]
        b = a
        assert a is b
        #레퍼런스 비교이므로 같다.

    # [문제3] 객체의 변경
    # 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 아래와 같이 a, b 변수를 선언 한 후 a의 첫 번째 요소값을 변경하면 b의 값은 어떻게 될까? 그리고 이런 결과가 나오는 이유에 대해서 설명해 보자.
    # >>> a = b = [1, 2, 3]
    # >>> a[1] = 4
    # >>> print(b)
    def test_quiz3(self):
        a = b = [1, 2, 3]
        a[1] = 4
        assert [1,4,3] == b
        assert a  is b
        #당연히 같은 참조니까..

    # [문제4] 리스트 복사1
    # 다음 예제를 실행하고 그 결과를 설명하시오.
    # >>> a = [1, 2, 3]
    # >>> b = a[:]
    # >>> a is b
    def test_quiz4(self):
        a = [1, 2, 3]
        b = a[:]
        assert  False == (a is b)
        #값 복사를 해서 새로운 리스트를 만들었기 때문에.

    # [문제5] 리스트 복사2
    # b리스트는 a리스트를 copy하여 다음과 같이 생성하였다.
    # >>> a = [1, 2, 3]
    # >>> b = a[:]
    # 그리고 다음과 같이 a리스트의 두번째 요소값을 2에서 4로 바꾸었다.
    # >>> a[1] = 4
    # >>> a
    # [1, 4, 3]
    # >>> print(b)
    # 이제 b리스트를 출력하면 어떤 값이 출력될까? 그리고 그런 결과값이 나오는 이유에 대해서 설명하시오.
    def test_quiz5(self):
        a = [1, 2, 3]
        b = a[:]
        a[1] = 4
        assert [1,2,3] == b
        #복사되면 다른 메모리니까

    # [문제6] 리스트의 더하기와 extend
    # 다음과 같은 리스트 a가 있다.
    # >>> a = [1, 2, 3]
    # 리스트 a에 [4, 5]를 + 기호를 이용하여 더한 결과는 다음과 같다.
    # >>> a = [1, 2, 3]
    # >>> a = a + [4,5]
    # >>> a
    # [1, 2, 3, 4, 5]
    # 리스트 a에 [4,5]를 extend를 이용하여 더한 결과는 다음과 같다.
    # >>> a = [1, 2, 3]
    # >>> a.extend([4, 5])
    # >>> a
    # [1, 2, 3, 4, 5]
    # + 기호를 이용하여 더한것과 extend한 것의 차이점이 있을까? 있다면 그 차이점에 대해서 얘기해 보자.
    def test_quiz6(self):
        a = [1, 2, 3]
        idOfa = id(a)
        a = a + [4, 5]
        idOfa2 = id(a)
        assert idOfa != idOfa2

        b = [1, 2, 3]
        idOfb = id(b)
        b.extend([4, 5])
        idOfb2 = id(b)
        assert idOfb == idOfb2

        #extend는 메모리 낭비가 적다는 것...


    # [문제7] 리스트 복사3
    # a리스트는 리스트내에 [2, 3]이라는 리스트를 하나 더 포함하고 있는 리스트이다. 이 a리스트를 copy하여 b리스트를 다음과 같이 만들었다.
    # >>> a = [1, [2, 3], 4]
    # >>> b = a[:]
    # 그리고 다음과 같이 a 리스트에 포함된 [2, 3]의 첫번째 값을 2에서 5로 바꾸어 주었다.
    # 이렇게 a리스트에 포함된 리스트의 요소값을 변경하면 b 리스트는 어떻게 될까? 그리고 그런 결과값이 나오는 이유에 대해서 설명하시오.
    # >>> a[1][0] = 5
    # >>> a
    # [1, [5, 3], 4]
    # >>> print(b)
    def test_quiz7(self):
        a = [1, [2, 3], 4]
        b = a[:]
        a[1][0] = 5
        assert  [1, [5,3],4] == b
        #왜냐면 [2,3]이 참조이므로.

        d = [1, [2, 3], 4]
        c = deepcopy(d)
        d[1][0] = 5
        assert [1,[2,3],4] == c
        #딥카피 하면 다른 객체니까.