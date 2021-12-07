"""
Author : Jinwoo Lee
Date : 2021.12.04.
"""
# 
import math

class Animal:
    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xposition = xpos
        self.yposition = ypos
        self.velocity = 0

    def sound(self):
        pass    # 실행할 코드가 없음을 의미(문법적으로 문장이 필요하지만, 프로그램이 할 일이 없을 때 사용), Java의 Interface와 같이 의무적으로 상속시킬 때 사용하는 듯

class Horse(Animal):
    def __init__(self, age, height, color, xpos, ypos):
        Animal.__init__(self, age, height, color, xpos, ypos)           # 부모 클래스(Animal)의 생성자 호출

    def sound(self):
        print('Neigh')

    def run(self, xdistance, ydistance, time):
        self.xposition += xdistance
        self.yposition += ydistance
        total_distance = math.sqrt((xdistance + xdistance) * (ydistance + ydistance))
        self.velocity = total_distance/time

class Dog(Animal):
    def __init__(self, age, height, color, xpos, ypos):
        Animal.__init__(self, age, height, color, xpos, ypos)

    def sound(self):
        print('Bow-Wow')

if __name__ == '__main__':
    danbi = Horse(5, 160, 'brown', 0, 0)
    choco = Dog(10, 100, 'black', 50, 30)
    danbi.sound()
    choco.sound()
