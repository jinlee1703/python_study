"""
Author : Jinwoo Lee
Date : 2021.12.05.
"""

# 파일 객체 생성 (파일모드 : 'w') : write()
f = open("D:/새파일.txt", 'w')
print(f)

for i in range(1, 6):             # 파일 쓰기
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.close()                         # 파일 닫기


# 파일에 내용 추가하기 (파일모드 : 'a')
f = open("D:/새파일.txt", 'a')
for i in range (6, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)

f.close()


# 파일 읽기(1) : 파일 모드 'r', readline()
f = open("D:/새파일.txt", 'r')
line = f.readline()
print(line)
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 파일 읽기(2) : 파일 모드 'r', readlines()
f = open("D:/새파일.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

# 파일 읽기(3) : 파일 모드 'r', read()
f = open("D:/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일 처리 후 파일 닫기(자동 처리)
with open("D:/새파일.txt", 'w') as f:
    f.write("Now is better than never.")
    
data = f.read()     # 파일 객체 f를 이용한 파일 처리가 끝나고 파일을 닫은 상태에서 f.read()로 파일 읽기를 하였으므로 에러 발생