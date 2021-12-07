"""
Author : Jinwoo Lee
Date : 2021.12.07.
"""

# import matplotlib as plt
# print(plt.__version__)
import matplotlib.pyplot as plt

# 라인플롯 차트 그리기
x = [2016, 2017, 2018, 2019, 2020]      # 데이터 준비
y = [350, 410, 520, 695, 543]

plt.plot(x, y)                          # x축과 y축 데이터를 지정하여 라인플롯 생성

plt.title('Annual sales')               # 차트 제목 설정
plt.xlabel('years')                     # x축 레이블 설정
plt.ylabel('sales')                     # y축 레이블 설정
plt.show()                              # 라인플롯 표시
