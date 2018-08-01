import pytest

# 배워보고 싶다~!
class TestSet():

    def test_MakeSet(self):
        sets = {1, 2, 3, 4, 5}
        sets2 = {4, 5, 6, 7, 8}


    def test_count(self):
        sets = {1, 2, 3}
        sets2 = set("Hello")
        assert 3 == len(sets)
        assert 4 == len(sets2)


    def test_Incert(self):
        sets = {'h', 'e', 'l', 'o'}
        assert 4 == len(sets)
        sets.add('d')
        assert {'h', 'e', 'l', 'o', 'd'} == sets
        assert 5 == len(sets)

    def test_Interset_Union_Diff(self):
        sets1 = {1, 2, 3, 4, 5}
        sets2= {4, 5, 6, 7, 8}

        interseted = sets1 & sets2
        assert {4,5} == interseted

        union = sets1 | sets2
        assert {1,2,3,4,5,6,7,8} == union

        difference = sets1 - sets2
        assert {1, 2, 3} == difference


    #pop은 랜덤하게 (해싱을 하기는 하지만?) 빼낸다. => 쓰지마라
    # def test_Pop(self):
    #     sets = {'h', 'e', 'l', 'o'}
    #     popped = sets.pop()
    #     assert  {'e', 'h', 'o'} == sets
    #     assert  'l' == popped

    #del 로  지울 수 없다.
    # def test_delete(self):
    #     sets = {'h', 'e', 'l', 'o'}
    #     del sets
    #     assert None == sets


    # in 으로 쉽게 존재 여부를 확인 가능.
    def test_GetValues(self):
        sets = {'h', 'e', 'l', 'o'}
        # 있는지 확인 가능. in 을 사용한다.
        assert 'h' in sets
        assert 'e' in sets
        assert 'l' in sets

        assert False == ('d' in sets)


    def test_AddMultiple(self):
        sets = {'h', 'e', 'l', 'o'}
        sets.update(['m', 't'])
        assert {'h', 'e', 'l', 'o', 'm', 't'} == sets


    #[문제1] 집합 만들기1
    #['a', 'b', 'c'] 라는 리스트를 집합 자료형으로 만드시오.
    def test_quiz1(self):
        list = ['a','b', 'c']
        result =  set(list)
        assert {'a', 'b', 'c'} == result

    # [문제2] 집합의 중복
    # 중복을 허용하지 않는 집합 자료형의 특징을 이용하여 다음 a 리스트에서 중복된 숫자들을 제거해 보자.
    # >>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    def test_quiz2(self):
        a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
        result = set(a)
        assert {1, 2, 3,4,5} == result

    # [문제3] 차집합
    # 다음과 같은 2개의 집합 자료형이 있다.
    # >>> s1 = set(['a', 'b', 'c', 'd', 'e'])
    # >>> s2 = set(['c', 'd', 'e', 'f', 'g'])
    # s1 집합의 항목 중 s2 집합에 포함된 항목을 제거 해 보자.
    def test_quiz3(self):
        s1 = {'a', 'b', 'c', 'd', 'e'}
        s2 = {'c', 'd', 'e', 'f', 'g'}
        s1 = s1-s2
        assert {'a', 'b'} == s1



    # [문제4] 집합 만들기2
    # 집합 자료형은 다음과 같이 만들 수 있다.
    # >>> a = {'a', 'b', 'c'}
    # >>> a
    # {'a', 'b', 'c'}
    # >>> type(a)
    # <class 'set'>
    # 값이 하나도 없는 비어있는 set을 만들기 위해 다음과 같이 시도 해 보자.
    # >>> a = {}
    # >>> type(a)
    # <class 'dict'>
    # 위와 같이 값이 있을 경우에는 집합 자료형으로 인식했지만 값이 없을경우에는 딕셔너리로 인식하게 된다. 그렇다면 값이 비어있는 집합 자료형은 어떻게 만들 수 있을까?
    def test_quiz4(self):
        a = set()

    # [문제5] 집합 추가
    # 다음과 같은 집합 자료형 a가 있다.
    # >>> a = {'a', 'b', 'c'}
    # a 에 {'d', 'e', 'f'} 를 추가하시오.
    def test_quiz5(self):
        a = {'a', 'b', 'c'}
        a.update('d', 'e', 'f')
        assert {'a', 'b', 'c', 'd', 'e', 'f'} == a