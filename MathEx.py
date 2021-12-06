"""
Author : Jinwoo Lee
Date : 2021.12.04.
"""

import math

print(math.pi)      # 원주율 pi 값
print(math.e)       # 오일러 수 e 값

radius = 5.0
area = (radius ** 2) * math.pi      # 원의 넓이 : 반지름 * 반지름 * 3.14
theta = math.radians(60)

x = radius * math.cos(theta)
y = radius * math.sin(theta)

print("area : " + str(area))
print("x : " + str(x))
print("y : " + str(y))
