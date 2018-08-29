import pytest

#from 패키지명 import 모듈명

from VKLib.Collection import *
from VKLib.Math import Sum

# 패키지 = 폴더
# 모듈 = 파일
# __all__ 을 지정해서 '모듈'들을 *로 임포팅 가능.
# 패키지 안의 패키지는 *로 불러올 수 없음. 왜냐면 '모듈'로 판단되기 때문임.
# import '모듈' 임.
class TestPackage():

    def test_import(self):
        pc = Sum.Calculator()

    def test_import2(self):
        crasher = Crash.Crasher()
