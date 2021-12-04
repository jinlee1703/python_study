class Horse:
    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xposition = xpos
        self.yposition = ypos
        self.velocity = 0

class Alphabets:
    __str = ""
    def __init__(self, text):
        self.text = text
        Alphabets.__str += text
    def print_class_variable(self):
        print(Alphabets.__str)

if __name__ == '__main__':
    o1 = Alphabets('p')
    o2 = Alphabets('y')
    o3 = Alphabets('t')
    o4 = Alphabets('h')
    o5 = Alphabets('o')
    o6 = Alphabets('n')

    o1.print_class_variable()
    o2.print_class_variable()