"""
Author : Jinwoo Lee
Date : 2021.12.05.
"""

import numpy as np
print(np.__version__)

# 리스트를 이용하여 numpy 생성
print("[ar1]")
ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)
print(type(ar1))        # 객체 ar1의 자료형 확인

print("[ar2]")
ar2 = np.array([[10, 20, 30], [40, 50, 60]])
print(ar2)

# 값의 범위를 지정하여 numpy 생성
print("[ar3]")
ar3 = np.arange(1, 11, 2)
print(ar3)

# 구조를 지정하여 numpy 생성 : 3행 2열로 구조 변경
print("[ar4]")
ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
print(ar4)

# 초기값과 구조를 지정하여 numpy 생성 : 0으로 초기화하고 2행 3열 구조를 생성
print("[ar5]")
ar5 = np.zeros((2, 3))
print(ar5)

# numpy 슬라이싱
print("[ar6]")
ar6 = ar2[0:2, 0:2]
print(ar6)

print("[ar7]")
ar7 = ar2[0, :]     # 0행의 모든 열 슬라이싱
print(ar7)

# numpy 사칙 연산
print("[ar8]")
ar8 = ar1 + 10
print(ar8)

print(ar1 + ar8)

print(ar8 - ar1)

print(ar1 * 2)

print(ar1 / 2)

# numpy 행렬곱 연산
print("[ar9]")
ar9 = np.dot(ar2, ar4)
print(ar9)
print(ar9)
