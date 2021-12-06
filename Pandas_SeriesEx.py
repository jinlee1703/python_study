"""
Author : Jinwoo Lee
Date : 2021.12.06.
"""

import pandas as pd
print(pd.__version__)

# Series 생성 : pd.Series()
print("==========data1==========")
data1 = [10, 20, 30, 40, 50]
print(data1)

print("==========data2==========")
data2 = ['1반', '2반', '3반', '4반', '5반']
print(data2)

print("==========data2==========")

# 리스트를 이용하여 Series 생성
print("==========sr1==========")
sr1 = pd.Series(data1)
print(sr1)

print("==========sr2==========")
sr2 = pd.Series(data2)
print(sr2)

# 값을 이용하여 Series 생성
print("==========sr3==========")
sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)
print("==========sr4==========")
sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

# 인덱스를 지정하여 Series 생성
print("==========sr5==========")
sr5 = pd.Series(data1, index=[1000, 1001, 1002, 1003, 1004])
print(sr5)
print("==========sr6==========")
sr6 = pd.Series(data1, index=data2)
print(sr6)
print("==========sr7==========")
sr7 = pd.Series(data2, index=data1)
print(sr7)
print("==========sr8==========")
sr8 = pd.Series(data2, index=sr4)
print(sr8)

# Series 인덱싱
print("==========sr8 인덱싱==========")
print(sr8[2])
print(sr8['수'])
print(sr8[-1])

# Series 슬라이싱
print("==========sr8 슬라이싱==========")
print(sr8[0:4])

# Series 인덱스 구하기: index
print("==========sr8 index==========")
print(sr8.index)

# series 값 구하기
print("==========sr8 values==========")
print(sr8.values)

# Series 원소가 숫자이면 덧셈 수행
print(sr1 + sr3)

# Series 원소가 문자이면 문자열 연결 수행
print(sr4 + sr2)