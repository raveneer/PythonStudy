import pytest


# 배워보고 싶다~!
class TestDictionary():

    def test_count(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        assert 3 == len(codes)

    def test_incert(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        codes[4] = 'd'
        assert 4 == len(codes)
        assert {1: 'a', 2: 'b', 3: 'c', 4: 'd'} == codes

    # pop으로 딕셔너리를 줄일 수 있다.
    def test_pop(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        codes.pop(3)
        assert {1: 'a', 2: 'b'} == codes
        codes.pop(1)
        assert {2: 'b'} == codes

        # pop으로 '꺼낼 수 있다' 이 경우 키는 사용되고 값이 반환
        popped = codes.pop(2)
        assert {} == codes
        assert 'b' == popped

    # del 로 쉽게 지울 수 있다!
    def test_delete(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        del codes[3]
        assert {1: 'a', 2: 'b'} == codes

    def test_get(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        assert 'a' == codes[1]
        assert 'b' == codes[2]
        assert 'c' == codes[3]

    # zip 과 comprehension 을 이용해서 리스트 2개로 간단히 딕셔너리를 만들 수가 있다.
    def test_comprehension(self):
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        my_dic = {key: value for key, value in zip(keys, values)}
        assert my_dic == {'a': 1, 'b': 2, 'c': 3}

    # 딕셔너리는 곱할 수가 없따
    # def test_Multiple(self):
    #
    #     codes = {1:'a', 2:'b', 3:'c'}
    #     #양수 곱하면 반복
    #     assert {1:'a', 2:'b', 3:'c'} == codes * 2
    #
    #     #음수 곱하면 비워버림
    #     #assert {} == codes * -3

    # 키는 리스트가 아니라 순회 가능한 타입으로 반환된다.
    # 순회만 가능할 뿐이란것에 주의...
    def test_get_keys(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        keys = codes.keys()

        # 순회가능
        result = 0
        for key in keys:
            result += key

        assert 6 == result

        # 있는지 확인 가능.
        assert keys.__contains__(1)
        assert keys.__contains__(2)
        assert keys.__contains__(3)

        assert False == keys.__contains__(4)
        assert False == ('4' in codes.keys())

    def test_get_alues(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        values = codes.values()

        # 있는지 확인 가능. in 을 사용한다.
        assert 'a' in codes.values()
        assert 'b' in codes.values()
        assert 'c' in codes.values()

        assert False == ('d' in codes.values())

    def test_get_key_value_pair(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        items = codes.items()

        # 있는지 확인 가능. items는 튜플반환임에 주의.
        assert (1, 'a') in codes.items()
        assert (2, 'b') in codes.items()
        assert (3, 'c') in codes.items()

    # 키가 없을 때 None 반환.
    def test_try_get_values(self):
        codes = {1: 'a', 2: 'b', 3: 'c'}
        assert codes.get(10) is None

    # quiz1
    # [문제1]    딕셔너리    만들기    다음    표를    딕셔너리로    만드시오.
    # 항목    값
    # name    홍길동
    # birth    1128
    # age    30
    def test_make_dic_with_honggildong(self):
        newDic = {'name': '홍길동', 'birth': 1128, 'age': 30}
        assert '홍길동' == newDic["name"]
        assert 1128 == newDic["birth"]
        assert 30 == newDic["age"]

    # quiz2
    # 딕셔너리 키는 얄딱꾸리한데, = 이 오른쪽에 있으면 입력이고 = 이 왼쪽에 있으면 출력이다 -_-
    # 다음 중 에러나는 것은..?
    def test_dic_what_makes_error(self):
        a = dict()
        a['name'] = 'python'
        a[('a',)] = 'python'
        # a[[1]] = 'python' #에러가 난다. 리스트를 키로 쓸 수 없기 때문에.
        a[250] = 'python'

        assert 'python' == a['name']
        assert 'python' == a[('a',)]  # 대체 무슨 짓을 한 거냥...
        assert 'python' == a[250]

    # quiz3
    # 딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해 보자.
    # >>> a = {'A':90, 'B':80, 'C':70}
    def test_Extract_B(self):
        a = {'A': 90, 'B': 80, 'C': 70}
        result = a.pop('B')
        assert 80 == result
        assert {'A': 90, 'C': 70} == a

    # quiz4
    # 해당되는 키값이 없을 경우 오류 대신 70을 얻을수 있도록 수정해 보자.
    def test_Extract_Return_SomeValueWhenNoKey(self):
        a = {'A': 90, 'B': 80, 'C': 70}

        assert 90 == a['A']
        assert 90 == self.TryGetValue(a, 'A')
        assert 80 == self.TryGetValue(a, 'B')
        assert 70 == self.TryGetValue(a, 'C')
        assert 70 == self.TryGetValue(a, 'a')

    def TryGetValue(self, a: dict, key: str) -> int:
        if (key in a.keys()):
            return a[key]
        else:
            return 70

    # [문제5] 딕셔너리 최소값 다음과 같은 딕셔너리 a가 있다.
    # >>> a = {'A':90, 'B':80, 'C':70}
    # 딕셔너리 a의 value중에서 최소 값을 출력하시오.
    def test_FindLowestValue(self):
        a = {'A': 90, 'B': 80, 'C': 70}

        valueList = list(a.values())
        valueList.sort()
        assert 70 == valueList[0]

    # 문제6] 딕셔너리 리스트 변환
    # 다음과 같은 딕셔너리 a가 있다.
    # >>> a = {'A':90, 'B':80, 'C':70}
    # 위 딕셔너리 a를 다음과 같은 리스트로 만들어보자.
    # [('A', 90), ('B', 80), ('C', 70)]
    def test_DicToList(self):
        a = {'A': 90, 'B': 80, 'C': 70}
        pair = a.items()
        result = list(pair)
        assert [('A', 90), ('B', 80), ('C', 70)] == result
