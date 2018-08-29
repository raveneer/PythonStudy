import pytest
from ast import literal_eval
#
# # 배워보고 싶다~!
# class TestIO():
#
#     # def test_makeFile(self):
#     #     f = open("새파일.txt", 'w')
#     #     for number in range(1,10):
#     #         data = "%d번째 줄입니다\n" % number
#     #         f.write(data)
#     #     f.close()
#     #     assert True
#
#     def test_readFile(self):
#         f = open("새파일.txt", 'r')
#         line = f.readline()
#         assert "1번째 줄입니다\n" == line
#         f.close()
#
#     def test_readLines(self):
#         f = open("새파일.txt", 'r')
#         lines = f.readlines()
#         counter =0
#         for line in lines:
#             counter +=1
#             assert "%d번째 줄입니다\n" %counter == line
#         f.close()
#
#     #with를 쓰면 문을 벗어날 떄 바로 닫는다. c#의 using과 같음.
#     def test_usingWith(self):
#         with open("새파일.txt", 'r') as f:
#             line = f.readline()
#             assert "1번째 줄입니다\n" == line

#[문제1] 파일 읽고 출력하기
# 다음은 "test.txt"라는 파일에 "Life is too short" 라는 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f2 = open("test.txt", 'r')
# print(f2.read())
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정하시오.
#     def test_quiz1(self):
#
#         f1 = open("testIOQuiz1.txt", 'w')
#         f1.write("Life is too short")
#         f1.close()
#
#         f2 = open("testIOQuiz1.txt", 'r')
#         assert "Life is too short" == f2.read()


# [문제2] 파일저장
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성하시오. (단, 프로그램을 다시 실행하더라도 기존 작성한 내용을 유지하고 새로 입력한 내용이 추가되어야 한다.)
# 다음은 실행 예제이다.
# 저장할 내용을 입력하세요:
# 실행 할 때마다 사용자가 입력한 내용이 test.txt파일에 추가되어야 한다.
#     def test_quiz2(self):
#         #지우기 위해서
#         open("testIOQuiz2", 'w').close()
#
#         f1 = open("testIOQuiz2", 'a')
#         f1.write("a")
#         f1.close()
#         f1 = open("testIOQuiz2", 'r')
#         assert "a" == f1.read()
#         f1.close()
#
#         f1 = open("testIOQuiz2", 'a')
#         f1.write("b")
#         f1.close()
#         f1 = open("testIOQuiz2", 'r')
#         assert "ab" == f1.read()
#         f1.close()

# [문제3] 역순 저장
#
# 다음과 같은 내용의 파일 abc.txt가 있다.
#
# abc.txt
#
# AAA
# BBB
# CCC
# DDD
# EEE
# 이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
#
# EEE
# DDD
# CCC
# BBB
# AAA
#
# [문제4] 파일 수정
# 다음과 같은 내용을 지닌 파일 test.txt 가 있다.
# test.txt
# Life is too short
# you need java
# 이 파일의 내용중 java라는 문자열을 python으로 바꾸어서 저장하시오.
#     def test_quiz4(self):
#         open("testIOQuiz4", 'w').close()
#         with open("testIOQuiz4", 'w') as f:
#             f.write("Life is too short\n you need java")
#
#         text =""
#
#         with open("testIOQuiz4", 'r') as f:
#             text = f.read()
#         text = text.replace("java", "python")
#         assert text == "Life is too short\n you need python"
#
#         with open("testIOQuiz4", 'w') as f:
#             f.write(text)
#
#         with open("testIOQuiz4", 'r') as f:
#             assert "Life is too short\n you need python" == f.read()