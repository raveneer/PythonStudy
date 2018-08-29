import pytest


# List를 배워보고 싶다~!
class TestList():

    def test_count(self):
        codes = ['a', 'b', 'c']
        assert 3 == len(codes)

    def test_add(self):
        codes = ['a', 'b', 'c']

        codes.append('d')

        assert 4 == len(codes)
        assert ['a', 'b', 'c', 'd'] == codes

        codes.append(['e', 'f'])
        assert ['a', 'b', 'c', 'd', ['e', 'f']] == codes
        assert 5 == len(codes)

    def test_plus(self):
        codes = ['a', 'b', 'c']
        codes += 'd'
        assert ['a', 'b', 'c', 'd'] == codes

    # remove는 첫번째로 만난 해당 요소를 지운다. 한번 더 실행하면 다음 해당 요소를 지운다.
    def test_remove(self):
        codes = ['a', 'b', 'c', 'a']
        codes.remove('a')
        assert ['b', 'c', 'a'] == codes
        codes.remove('a')
        assert ['b', 'c'] == codes

    def test_delete(self):
        codes = ['a', 'b', 'c']
        del codes[0]
        assert ['b', 'c'] == codes

    # []를 이용해서 지울 수 있긴 한데, 용법이 상당히 애매하다. 직관적인 del을 쓰자...
    def test_delete2(self):
        codes = ['a', 'b', 'c']
        codes[1:2] = []
        assert ['a', 'c'] == codes

    def test_Get(self):
        codes = ['a', 'b', 'c']
        assert 'a' == codes[0]
        assert 'c' == codes[-1]
        assert 'b' == codes[-2]

    def test_Slice(self):
        codes = ['a', 'b', 'c']
        # 양수 슬라이싱은 앞에서 센 만큼만 '가진다'
        assert ['a', 'b'] == codes[:2]
        assert ['c'] == codes[2:]

        # 음수 슬라이싱은 뒤에서부터 센 만큼 '버린다'
        assert ['a', 'b'] == codes[:-1]
        assert ['a'] == codes[:-2]

    def test_Multiple(self):
        codes = ['a', 'b', 'c']

        # 양수 곱하면 반복
        assert ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'] == codes * 3

        # 음수 곱하면 비워버림
        assert [] == codes * -3

    def test_Pop(self):
        codes = ['a', 'b', 'c']
        popped = codes.pop(1)
        assert ['a', 'c'] == codes
        assert 'b' == popped

    def test_Extend(self):
        codes = ['a', 'b', 'c']
        numbers = [1, 2, 3]
        codes.extend(numbers)
        # 복사해서 이어붙인다
        assert ['a', 'b', 'c', 1, 2, 3] == codes
        assert [1, 2, 3] == numbers

    # [문제1] 리스트 인덱싱
    # 다음과 같은 리스트 a가 있다.
    # >>> a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
    # a 리스트를 이용하여 다음과 같은 문자열을 출력하시오.
    # you too
    def test_Quiz1(self):
        a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
        result = []
        result.insert(0, a[4])
        result.insert(1, a[2])
        assert ['you', 'too'] == result

    # [문제2] 리스트 조인
    # ['Life', 'is', 'too', 'short'] 라는 리스트를 Life is too short라는 문자열로 만들어 출력해 보자.
    def test_Quiz2(self):
        a = ['Life', 'is', 'too', 'short']
        result = ""
        result += a[0] + " "
        result += a[1] + " "
        result += a[2] + " "
        result += a[3]
        assert 'Life is too short' == result

    # [문제3] 리스트의 갯수
    # >>> a = [1, 2, 3]
    # 이 리스트의 갯수(사이즈)를 구하시오.
    def test_Quiz3(self):
        a = [1, 2, 3]
        assert 3 == len(a)

    # [문제4] 리스트의 append와 extend
    # 다음과 같은 리스트 a가 있다.
    # >>> a = [1, 2, 3]
    # 리스트 a에 [4, 5]를 append 했을 때와 extend했을 때의 차이점은 무엇인가?
    def test_Quiz4_1(self):
        a = [1, 2, 3]
        b = [4, 5]
        a.append(b)
        assert [1, 2, 3, [4, 5]] == a

    # extend 는 c#의 addRange와 같다. (그리고 잘 안 쓰이지 -_-)
    def test_Quiz4_2(self):
        a = [1, 2, 3]
        b = [4, 5]
        a.extend(b)
        assert [1, 2, 3, 4, 5] == a

    # [문제5] 리스트 정렬
    # [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자. (힌트. 리스트의 내장함수인 sort와 reverse를 활용해 보자.)
    def test_Quiz5(self):
        a = [1, 3, 5, 4, 2]
        a.sort()
        a.reverse()
        assert [5, 4, 3, 2, 1] == a

    # 문제6] 리스트 삭제
    # [1, 2, 3, 4, 5]라는 리스트를 [1, 3, 5]로 만들어 보자.
    def test_Quiz6(self):
        a = [1, 2, 3, 4, 5]
        a.remove(2)
        a.remove(4)
        assert [1, 3, 5] == a

    # append는 리스트에 해당 원소를 그냥 집어넣는다.
    def test_append(self):
        a = [1, 2, 3]
        a.append([4, 5])
        assert [1, 2, 3, [4, 5]] == a

    # extend는 리스트를 연결하여 늘린다.
    def test_extned(self):
        a = [1, 2, 3]
        a.extend([4, 5])
        assert [1, 2, 3, 4, 5] == a

    # __add__ 와 += 는 같으며, 리스트만 더할 수 있다. 그냥 원소를 넣을 수는 없다.
    def test_addByPlus(self):
        a = [1, 2, 3]
        a += [4]
        assert [1, 2, 3, 4] == a

        b = [1, 2, 3]
        b = b.__add__([4])
        assert [1, 2, 3, 4] == b

    # insert는 인덱스를 넘겨줘야 해서 불편하다...
    def test_insert(self):
        a = [1, 2, 3]
        a.insert(3, 4)
        assert [1, 2, 3, 4] == a

    # insert는 인덱스를 넘겨줘야 해서 불편하다...
    def test_len2(self):
        a = [1, 2, 3]
        assert 3 == len(a)

    def test_get_len_list_in_list(self):
        input = [[1], [1, 2]]
        result = list()
        result.append(len(input[0]))
        result.append(len(input[1]))
        assert [1, 2] == result
