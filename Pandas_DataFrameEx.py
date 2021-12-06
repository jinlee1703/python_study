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

# pd.DataFrame() : 데이터 프레임 출력
print("========== data_dic ==========")
data_dic = {
    'year': [2018, 2019, 2020],
    'sales': [350, 450, 1099]
}
print(data_dic)

# 딕셔너리를 이용하여 DataFrame 생성
print("========== df1 ==========")
df1 = pd.DataFrame(data_dic)
print(df1)

# 리스트를 이용하여 DataFrame 생성 1
print("========== df2 ==========")
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index=['중간고사', '기말고사'], columns=data2[0:3])
print(df2)

# 리스트를 이용하여 DataFrame 생성 2
print("========== df3 ==========")
data_df = [['20201101', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
print(df3)

# DataFrame 열 이름 지정
print("========== df3 ==========")
df3.columns = ['학번', '이름', '중간고사', '기말고사']
print(df3)

# DataFrame 조회
print("========== df3.head(2) ==========")
print(df3.head(2))      # 위에서부터 2개 행 조회
print("========== df3.tail(2) ==========")
print(df3.tail(2))      # 아래에서부터 2개 행 조회
print("========== df3['이름'] ==========")
print(df3['이름'])       # '이름' 칼럼 조회

# CSV 파일로 저장
df3.to_csv('D:/python_study/base/Pandas_DataFrameEx_score.csv', header='False')        # 절대 경로 : 최상위 디렉토리가 반드시 포함된 경로를 의미
df3.to_csv('Pandas_DataFrameEx_score.csv', header='False')                             # 상대 경로 : 현재 디렉토리(비교 대상)를 기준으로 작성된 경로

# CSV 파일을 DataFrame으로 불러오기
print("========== df4 ==========")
df4 = pd.read_csv('Pandas_DataFrameEx_score.csv', encoding='utf-8', index_col=0, engine='python')
print(df4)