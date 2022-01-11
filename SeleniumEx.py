"""
Author : Jinwoo Lee
Date : 2022.01.11.
"""

from selenium import webdriver                              # Selenium 라이브러리의 WebDriver 임포트

wd = webdriver.Chrome('./WebDriver/chromedriver.exe')       # 크롬 WebDriver 객체 생성

wd.get("http://www.hanbit.co.kr")                           # Selenium이 제어하는 크롬 창에서 웹 페이지를 열어 확인