"""
Author : Jinwoo Lee
Date : 2021.12.05.
"""

print(abs(-3.5))            # abs(x) : 숫자 x의 절대값을 반환

print(all([1, 2, 3, 4]))    # all(iterable_x) : 그룹 자료형의 변수 x의 모든 원소가 참(0이 아닌 값)이면 True 반환
print(all([4, -2, 0.0, 4]))

print(any([1, 2, 3, 4]))    # any(iterable_x) : 그룹 자료형의 변수 x의 원소 중 하나라도 참이면 True 반환
print(any([4, -2, 0.0, 4]))

print(chr(97))              # chr(x) : 아스키코드 값 x에 대한 문자 출력
print(chr(48))

print(ord('a'))             # ord(x) : 문자 c에 대한 아스키코드 값 출력
print(ord('0'))

print(dir([1, 2, 3]))       # dir(x) : 객체 x가 가진 멤버 변수와 멤버함수 보여주기
print(dir({'1':'a'}))
print(dir(1))

print(divmod(7, 3))         # divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(1.3, 0.2))

print(oct(8))               # oct(x) : 정수값 x를 8진수로 변환하여 반환
print(oct(234))

print(hex(16))              # hex(x) : 정수값 x를 16진수로 변환하여 반환
print(hex(234))

a = 3
print(id(a))                # id(object) : object(객체)의 주소값을 반환

print(int('3'))             # int(x) : x를 정수 형태로 반환

print(str(3))               # str(x) : x를 문자열 형태로 반환

print(list("Python"))       # list(x) : x를 리스트로 반환
print(list((1, 2, 3)))

print(tuple("Python"))      # tuple(x) : x를 튜플로 반환
print(tuple((1, 2, 3)))

print(type("abc"))          # type(x) : x의 자료형을 반환
print(type(a))

sum = lambda a, b: a+b      # lambda : 간단한 삽입형 함수 생성
print(sum)
print(sum(3, 5))

print(max([1, 4, 2, 8, 6])) # max(iterable_x) : 반복 가능한 그룹 자료형 x를 입력받은 뒤 최대값을 반환
print(max("Python"))

print(min([1, 4, 2, 8, 6])) # min(iterable_x) : 반복 가능한 그룹 자료형 x를 입력받은 뒤 최소값을 반환
print(min("Python"))

print(pow(2, 4))            # pow(x, y) : x의 y제곱 결과값 반환

c = input()                 # input() : 사용자 입력으로 받은 값을 문자열로 반환
print(c)
c = input("정수를 입력하세요: ")
print(c)

print(range(5))             # range(x) : 입력받은 숫자에 해당되는 범위의 값을 반환
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))

print(len('Python'))        # len(s) : 입력값 s의 길이를 반환

print(sorted([3, 0, 2, 1])) # sorted(iterable_x) : 입력값을 정렬하여 리스트로 반환
print(sorted('Python'))

import urllib.request                                       # import 패키지명.모듈명
print(urllib.request.Request('http://www.hanb.co.kr'))      # 패키지명.모듈명.모듈함수()

import pandas                                               # import 모듈명
print(pandas.DataFrame())                                   # 모듈명.모듈함수()

from datetime import datetime                               # from 패키지명 import 모듈명
print(datetime.now())                                       # 모듈명.모듈함수()