import pytest


# 배워보고 싶다~!
class TestClass():
    def test_make_instance(self):
        calculator = FourCalc('zony')
        assert 3 == calculator.add(1, 2)
        assert FourCalc == type(calculator)

    def test_constructor(self):
        sony_mx5 = FourCalc('sony')
        samsung_pad = FourCalc('samsung')

        assert 3 == sony_mx5.add(1, 2)
        assert 3 == samsung_pad.add(1, 2)

        assert 'sony' == sony_mx5.maker
        assert 'samsung' == samsung_pad.maker

    def test_inheritance(self):
        i_calc6 = SixCalc('apple')
        assert 3 == i_calc6.add(1, 2)
        assert 2 == i_calc6.multiply(1, 2)
        assert 'apple' == i_calc6.maker

    def test_override(self):
        hwawei69 = CrackCalc('hwawei')
        assert 3 == hwawei69.add(1, 2)
        assert -1 == hwawei69.multiply(1, 2)

    def test_make_instance2(self):
        new_pc = SixCalc('IBM')
        assert SixCalc == type(new_pc)  # 타입은 상속을 표현하지 않는다.
        assert isinstance(new_pc, FourCalc)  # 상속은 이렇게 확인가능
        assert CrackCalc != type(new_pc)

    def test_call_instance_variable(self):
        # 간단한 예제. 슈퍼맨은 당연히 슈퍼히어로
        super_man = SuperCharacter('SuperMan')
        assert 'SuperMan' == super_man.name
        super_man.IS_HERO = True
        assert True == super_man.IS_HERO

        # 레드스컬은 빌런이다.
        red_skull = SuperCharacter('RedSkull')
        assert 'RedSkull' == red_skull.name
        red_skull.IS_HERO = False
        assert False == red_skull.IS_HERO

        # IsHero가 스태틱 변수임에도, 각각의 오브젝트의 값은 바뀌지 않는 것에 주의
        assert True == super_man.IS_HERO
        assert False == red_skull.IS_HERO

        # 그러나 IsHero는 스태틱 변수임으로, 클래스 자체의 값을 바꿔버릴 수 있다.
        SuperCharacter.IS_HERO = False  # 애초에 이런 짓을 안 하는게 좋다. 할 일도 별로 없고.
        # 그렇다 해도 기존에 생성된 객체들의 값이 변하는 건 아님.
        assert True == super_man.IS_HERO
        assert False == red_skull.IS_HERO

        # 단지 새로 생성되는 객체들이 바뀐 기본값을 준수할 뿐.
        joker = SuperCharacter("jok")
        assert False == joker.IS_HERO

    def test_change_const(self):
        new_drawer = DrawCircle()
        new_drawer.PI = 2
        assert 2 == new_drawer.PI


class DrawCircle():
    PI = 3.14

    def draw(self):
        return self.PI


class SuperCharacter():
    # 스태틱 클래스 변수이다.
    IS_HERO: bool

    def __init__(self, name):
        # 오브젝트 변수이다.
        self.name = name


# 이런 스타일 보다는
class Hero():
    IS_HERO: bool

    def __init__(self, is_hero: bool):
        self.IsHero = is_hero

    def get_hero(self):
        return self.IS_HERO


# 이런 스타일이 파이써닉하다.
class Villan():
    def __init__(self, is_villan: bool):
        self.isVillan = is_villan

    def get_villan(self):
        return self.isVillan

    # [문제1] Calculator 1
    # 다음은 계산기처럼 동작하는 Calculator클래스이다. add라는 메서드를 이용하면 현재 계산기의 객체 변수 value에 입력으로 받은 값을 더해 준다.
    # class Calculator:
    #     def __init__(self):
    #         self.value = 0
    #
    #     def add(val):
    #         self.value += val
    # 위와 같은 Calculator 클래스를 다음과 같이 사용하였다.
    # cal = Calculator()
    # cal.add(3)
    # cal.add(4)
    # print(cal.value)  # 7을 출력해야 한다.
    # 3과 4를 add했으므로 객체변수 value가 7이 되어 7을 출력해야 하지만 다음과 같은 오류가 발생했다.
    # Traceback (most recent call last):
    #   File "....py", line 9, in <module>
    #     cal.add(3)
    # TypeError: add() takes 1 positional argument but 2 were given
    # 오류가 발생하지 않도록 클래스의 잘못된 부분을 찾아 고치시오.
    def test_quiz1(self):
        calc = Calculator()
        assert 3 == calc.sum(3)
        assert 7 == calc.sum(4)


class Calculator():
    value = 0

    def __init__(self):
        self.value = 0

    def sum(self, val):
        self.value += val
        return self.value

    # [문제2] Calculator 2
    # 다음과 같은 Calculator 클래스가 있다.
    # class Calculator:
    #     def __init__(self, init_value):
    #         self.value = init_value
    #     def add(self, val):
    #         self.value += val
    # 이 클래스를 다음과 같이 사용해 보았다.
    # cal = Calculator()
    # cal.add(3)
    # cal.add(4)
    # print(cal.value)
    # 위 코드를 실행했더니 다음과 같은 오류가 발생한다.
    # Traceback (most recent call last):
    #   File "....py", line 8, in <module>
    #     cal = Calculator()
    # TypeError: __init__() missing 1 required positional argument: 'init_value'
    # 오류가 난 이유가 무엇인지 설명하고 오류를 해결하시오.

    # [문제3] UpgradeCalculator
    # 다음은 Calculator 클래스이다.
    # class Calculator:
    #     def __init__(self):
    #         self.value = 0
    #     def add(self, val):
    #         self.value += val
    # 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가하시오. 즉, 다음과 같이 동작하는 클래스를 만드시오.
    # cal = UpgradeCalculator()
    # cal.add(10)
    # cal.minus(7)
    # print(cal.value)  # 10에서 7을 뺀 3을 출력

    # [문제4] MaxLimitCalculator
    # 이번에 여러분이 작성해야 하는 클래스는 MaxLimitCalculator 클래스이다. MaxLimitCalculator 클래스는 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 클래스이다. 즉, 다음과 같이 동작해야 한다.
    # cal = MaxLimitCalculator()
    # cal.add(50)  # 50 더하기
    # cal.add(60)  # 60 더하기
    # print(cal.value)  # 100 출력
    # 단, 한가지 전제 조건이 있다. 그 조건은 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다는 것이다.
    # class Calculator:
    #     def __init__(self):
    #         self.value = 0
    #     def add(self, val):
    #         self.value += val
    # 위와 같은 조건을 만족하는 MaxLimitCalculator 클래스를 작성하시오.

    # [문제5] Calculator 3
    # 다음과 같이 동작하는 Calculator 클래스를 작성하시오.
    # cal1 = Calculator([1,2,3,4,5])
    # print(cal1.sum())  # 15 출력
    # print(cal1.avg())  # 3.0 출력
    # cal2 = Calculator([6,7,8,9,10])
    # print(cal2.sum())  # 40 출력
    # print(cal2.avg())  # 8.0 출력


class FourCalc():
    maker: str

    def add(self, a: int, b: int) -> int:
        return a + b

    def __init__(self, makerCompany: str):
        self.maker = makerCompany


# 상속도 아주 쉽다. 그냥 생성할때 인자로 받으면 땡.
class SixCalc(FourCalc):
    def multiply(self, a, b):
        return a * b


# 그냥 함수 새로 써주면 오버라이딩 되버린다. 음메 무서운거.
class CrackCalc(SixCalc):
    def multiply(self, a, b):
        return a - b
