"""
Author : Jinwoo Lee
Date : 2022.01.09.
"""

from bs4 import BeautifulSoup               # 파이썬에서 HTML 파싱(웹 페이지의 HTML 구조를 분석하는 작업)을 위해 사용하는 라이브러리

html = "<h1 id='title'>한빛출판네트워크</h1><div class='top><ul class='menu'><li><a class='login' href='http://www.hanbit.co.kr/member/login.html'>로그인</a></li></ul><ul class='brand'><li><a href='http://www.hanbit.co.kr/media/'>한빛미디어</a></li><li><a href='http://www.hanbit.co.kr/academy/'>한빛아카데미</a></li></ul></div>"

soup = BeautifulSoup(html, 'html.parser')   # HTML 파싱(1: 분석할 HTML을 저장한 문재열 객체[html], 2: 사용할 분석기['html.parser'])

print(soup.prettify())                      # prettify() 함수 : 객체 soup에 저장된 내용을 HTML 문서 형태로 출력

print("\n========================================\n")

# 태그 파싱하기, 지정된 한 개의 태그만 파싱 : 가장 먼저 생성된 한 개의 태그만 파싱되는 듯
print(soup.h1)

tag_h1 = soup.h1
print(tag_h1)

tag_div = soup.div
print(tag_div)

tag_ul = soup.ul
print(tag_ul)

tag_li = soup.li
print(tag_li)

tag_a = soup.a
print(tag_a)

print("\n========================================\n")

# 태그 파싱하기, 지정된 태그를 모두 파싱하여 리스트를 구성
tag_ul_all = soup.find_all("ul")
print(tag_ul_all)

tag_li_all = soup.find_all("li")
print(tag_li_all)

tag_a_all = soup.find_all("a")
print(tag_a_all)

# 속성을 이용하여 파싱
# attrs: 속성 이름과 속성값으로 딕셔너리 구성
# find(): 속성을 이용하여 특정 태그 파싱
# select(): 지정한 태그를 모두 파싱하여 리스트 구성 [태그#id 속성값], [태그.class 속성값]
print(tag_a.attrs)          # 속성 이름과 속성값으로 딕셔너리 구성

print(tag_a['href'])        # 속성값 확인하기
print(tag_a['class'])

tag_ul_2 = soup.find('ul', attrs={'class': 'brand'})    # ul 태그 중에서 class의 속성값이 brand인 태그 찾기
print(tag_ul_2)

title = soup.find(id="title")       # id 속성값이 title인 태그 찾기
print(title)
print(title.string)                 # title의 string만 출력

li_list = soup.select("div>ul.brand>li")    # div 태그블록 안에서 ul 태그의 class 속성값이 brand인 블록 안의 li 태그 블록을 모두 추출하기
print(li_list)

for li in li_list:
    print(li.string)