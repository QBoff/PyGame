import sys
from math import cos, radians, sin
from os.path import join
from turtle import Screen, Turtle

from PIL import Image
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider

LSystem = {}


# function for turtle, You can try it!!!!!!
# just write:
# screen = Screen()
# yr = Turtle()
# yr.speed("fastest")
# hilbert_curve(yr, 10, 1, 4)
# screen.exitonclick()
def hilbert_curve(turtle, A, parity, n):

    if n < 1:
        return

    turtle.left(parity * 90)
    hilbert_curve(turtle, A, - parity, n - 1)
    turtle.forward(A)
    turtle.right(parity * 90)
    hilbert_curve(turtle, A, parity, n - 1)
    turtle.forward(A)
    hilbert_curve(turtle, A, parity, n - 1)
    turtle.right(parity * 90)
    turtle.forward(A)
    hilbert_curve(turtle, A, - parity, n - 1)
    turtle.left(parity * 90)


# читаем данные из файла
def readlsystem():
    with open(join("other_tasks", "l_system", "data.txt"), "rt", encoding='utf8') as f:
        data = f.readlines()
    LSystem['name'] = data[0].strip()
    LSystem['angle'] = 360 / int(data[1].strip())
    LSystem['axioma'] = data[2].strip().replace("-", "")
    LSystem['theorems'] = [data[3].strip().split()[1]]
    if LSystem['name'] == "The dragon curve":
        LSystem['theorems'].append(data[4].strip().split()[1])
    print(LSystem)


# строим n-этап эволюции
def buildlsystem(n):
    result = LSystem['axioma']
    for _ in range(n):
        new = ''
        for ch in result:
            if ch == LSystem['axioma']:
                new += ''.join(LSystem['theorems'])
            else:
                new += ch
        result = new
    return result


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.initUI()

    def initUI(self):
        uic.loadUi(join("other_tasks", "l_system", "prog.ui"), self)

        self.sld.setValue(1)

        self.sld.setTickInterval(1)
        self.sld.setRange(1, 6)
        self.sld.setFocusPolicy(Qt.StrongFocus)
        self.sld.setTickPosition(QSlider.TicksBothSides)
        self.sld.setSingleStep(1)
        self.sld.valueChanged.connect(self.paintEvent)
        self.show()

    def hilbert(self, pen, A, parity, n, pos):
        if n < 1:
            return
        angel = 0
        angel += parity * 90
        self.hilbert(pen, A, -parity, n, pos)
        pen.drawLine(pos[0], pos[1], pos[0] + A, pos[1] + A)
        angel = parity * 90

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawFlag()
        self.qp.end()
        self.update()

    def drawFlag(self):

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.qp.setPen(pen)  # берем карандаш (черный, толщина 2, жирная линия)
        readlsystem()

        if LSystem["name"] == "The dragon curve":
            pos = [970, 545, 0]  # место старта (x, y, угол)
        elif LSystem["name"] == "Кривая Коха":
            pos = [70, 645, 0]
        elif LSystem["name"] == "Кривая Гильберта":
            pos = [70, 645, 0]
        elif LSystem["name"] == "Nice tree":
            pos = [170, 345, 0]

        flag = buildlsystem(self.sld.value())
        depls = 1
        dep = self.sld.value()

        for ch in flag:  # бежим по строке и рисуем соответствующий элемент
            if ch == "F" or ch == "X" or ch == "Y":
                self.qp.drawLine(pos[0], pos[1], pos[0] + int(
                    15 * cos(radians(pos[2]))), pos[1] + int(15 * sin(radians(pos[2]))))
                pos[0] += int(15 * cos(radians(pos[2])))
                pos[1] += int(15 * sin(radians(pos[2])))
            elif ch == '-':
                pos[2] -= LSystem['angle']
            elif ch == '+':
                pos[2] += LSystem['angle']


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    sys.exit(app.exec_())
