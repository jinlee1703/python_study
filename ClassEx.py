"""
Author : Jinwoo Lee

Date : 2021.12.04.
"""

class Horse:
    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xposition = xpos
        self.yposition = ypos
        self.velocity = 0

class Alphabets:
    __str = ""                          # 내부 멤버변수
    def __init__(self, text):           # 객체 생성자
        self.text = text
        Alphabets.__str += text
    def print_class_variable(self):
        print(Alphabets.__str)

if __name__ == '__main__':              # 현재 파일 안에서 실행되는 경우 : __main__ / import해서 다른 파일에서 실행되는 경우 ClassEx
    o1 = Alphabets('p')                 # 6개의 객체가 생성되는 과정에서 Alphabets 클래스의 클래스 변수인 str이 서로 공유
    o2 = Alphabets('y')
    o3 = Alphabets('t')
    o4 = Alphabets('h')
    o5 = Alphabets('o')
    o6 = Alphabets('n')

    o1.print_class_variable()
    o2.print_class_variable()
