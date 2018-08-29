import pytest
from ast import literal_eval

# 배워보고 싶다~!
class TestpytonIncludedFunctions():

    def test_abs(self):
        assert 1 == abs(1);
        assert 1 == abs(-1);
        assert 1.2 == abs(-1.2);
        assert 1.2 == abs(1.2);

    def test_all(self):
        collection = (2,2,3)
        assert True == all( x >1 for x in collection )
        assert False == all (x <1 for x in collection)

    def test_any(self):
        collection = (2, 2, 3)
        assert True == any(x >= 3 for x in collection)
        assert False == any(x < 2 for x in collection)
        assert True == any(x >2 for x in collection)

    def test_cha(self):
        assert 'a' == chr(97)
        assert '' == chr(1)

    # dir은 내부 함수 리스트를 보여주지만... 별로 쓸 일이 있나?
    # def test_dir(self):
    #     cow = Animal()
    #     assert  ['eat', 'sleep'] == dir(cow)

    #divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴하는 함수이다.
    def test_divMod(self):
        assert (2,1) == divmod(7, 3)
        assert (1,3) == divmod(13,10)

    # enumerate는 내부의 인덱서를 움직여 순회한다.
    # http: // brownbears.tistory.com / 118
    # range 보다 enumratef를 사용하라!
    def test_enumerate(self):
        for i, char in enumerate(('a','b','c')):
            if(i == 0):
                assert 'a' == char
            if (i == 1):
                assert 'b' == char
            if (i == 2):
                assert 'c' == char

    # enumerate는 인자로 콜렉션, 시작인덱스를 가진다.
    # 또한 enumerate는 결과로 (인덱스, 값)의 튜플을 반환한다.
    # 따라서 for 인덱스, 값 in enumerate(콜렉션, 시작인덱스):
    # 의 구문이 되는 것이다.
    def test_enumerate2(self):
        sum = 0
        for i , number in enumerate((1,2,3), 1):
            sum += number
        assert 6 == sum

    def test_enumerate3(self):
        sum =0
        for i, x in enumerate((1,2,3)):
            sum += i
            sum += x
        assert 9 == sum

    #이건 아주 대단한 구문인데, 문자열 구문을 받아서 실행하여 그 결과를 돌려준다.
    #즉, 동적으로 코드를 실행할 수가 있는 것이다...! 대단해
    def test_eval(self):
        assert 1 == eval("2-1")
        assert True == eval ("'a' in ['a', 1, 2]")
        assert True == eval ("1 == 1")


    #핕터는 강력하지만 결과를 필터 객체로 내보낸다. (iterator) 그러므로 list 등으로 재가공 해줄 필요가 있음.
    #람다를 써도 좋을 것이다.
    def test_filter(self):
        assert [1,2,3] == list(filter(lambda x : x>0, [0,0,1,2,3]))
        assert ['a'] == list(filter(lambda x : type(x) == str, [1,2,3,'a']))


    #hex는 웃긴게 16진수라고 해도, str로 반환한다.
    def test_hex(self):
        assert '0x1' == hex(1)
        assert '0x2' == hex(2)
        assert '0xf' == hex(15)
        assert '0x10' == hex(16)
        assert '0x11' == hex(17)
        assert '0xa0' == hex(160)
        assert '0xff' == hex(255) # 유명하니까외워둬자
        assert '0x100' == hex(256)
        assert '0xfff' == hex(4095)
        assert  255 == int('0xff', 16) # int 로 파싱하면 됨.


    #id는 메모리의 주소?를 알려주는 것은 아니지만 파이썬 내의 고유주소값을 반환한다.
    def test_id(self):
        a = 3
        b = 3
        assert id(a) == id(b)

        #파이썬의 고유주소값은 일종의 포인터 같은 느낌. 참조를 따면 주소값이 같다.
        c = a
        assert id(c) == id(a)

        #같은 값을 가진다 해도, 콜렉션은 id 값이 다를 것이다.
        col = [1,2,3]
        bar = [1,2,3]
        assert id(col) != id(bar)

        #그러나 콜렉션이 객체가 아닌 값을 가지고 있으므로, 값의 주소값은 같을 것이다. 왜냐면 1과 1은 같은 주소니까.
        assert id(col[0]) == id(bar[0])
        assert id(1) == id(col[0])


    #클래스 체크. 그냥 타입으로 비교해도 되지만.
    def test_isInstance(self):
        cat = Animal()
        assert True == isinstance(cat, Animal)
        assert type(cat) == Animal


    #드디어 강력한 것이 나왔군...
    #맵은 함수, 콜렉션으로 들어가며, 콜렉션의 각 원소를 함수에 차례대로 넣고 그 결과를 묶어서(어떻게 묶어서?) 반환한다.
    #필터와 비슷하다. 그러나 필터는 입력값을 걸러내지만, 맵은 입력값을 함수에 투영한 결과를 반환한다.
    #필터와 마찬가지로 결과는 map 객체이다. 그래서 list 등으로 평탄화 해줘야 할 필요가...흠...
    def test_map(self):
        assert [2,4,8] == list(map(lambda x:x*2, [1,2,4]))

        #그냥 for를 써도 비슷하게 구현할 수 있다. 함수를 넘길 수 없는 것도 아니고.
        #맵을 왜 써야 하는지 잘 모르겠군.
        result = list()
        col = [1,2,4]
        for number in col:
            result.append(number*2)
        assert [2,4,8] == result


class Animal():
    def eat(self):
        return 'mmm...'