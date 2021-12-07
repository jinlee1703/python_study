"""
Author : Jinwoo Lee
Date : 2021.12.07.
"""

import matplotlib.pyplot as plt

# 바 차트 그리기
y1 = [350, 410, 520, 695]                               # 데이터 준비
y2 = [200, 250, 385, 350]
x = range(len(y1))                                      # y1 길이를 범위로 x 리스트인 [0, 1, 2, 3] 생성

plt.bar(x, y1, width=0.7, color="blue")                 # x축과 y축 데이터를 지정하여 바 차트 생성
plt.bar(x, y2, width=0.7, color="red", bottom=y1)

plt.title('Quarterly sales')                            # 차트 제목 설정
plt.xlabel('Quarters')                                  # x축 레이블 설정
plt.ylabel('sales')                                     # y축 레이블 설정

xLabel = ['first', 'second', 'third', 'fourth']         # 눈금 이름 리스트 생성
plt.xticks(x, xLabel, fontsize=10)                      # 바 차트의 x축 눈금 이름 설정
plt.legend(['chairs', 'desks'])                         # 범례 설정
plt.show()                                              # 바 차트 표시
