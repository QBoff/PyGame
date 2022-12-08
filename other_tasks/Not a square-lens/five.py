import sys
from math import cos, pi, sin

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QColorDialog, QMainWindow
from PyQt5 import uic
from os.path import join

# self.screen_size = [500, 500]
SIDE_LENGTH = 140
SIDES_COUNT = 8


class Draw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m = 0
        self.flag = False
        self.screen_size = [QMainWindow.width(self), QMainWindow.height(self)]
        self.initUI()

    def initUI(self):
        uic.loadUi(join("other_tasks", "Not a square-lens", "prog.ui"), self)
        self.button_1.clicked.connect(self.run)

    def run(self):
        global SIDES_COUNT
        try:
            self.k = float(self.kk.text())

            SIDES_COUNT = int(self.n.text())
            self.m = int(self.mm.text())

            color = QColorDialog.getColor()
            if color.isValid():
                self.color = color.name()
                self.flag = True
                self.update()
        except ValueError:
            pass

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def xs(self, x):
        return x + self.screen_size[0] // 2

    def ys(self, y):
        return self.screen_size[1] // 2 - y

    def draw_star(self, qp):
        if self.flag:
            pen = QPen(QColor(self.color), 2)
            qp.setPen(pen)

            nodes = [(SIDE_LENGTH * cos(i * 2 * pi / SIDES_COUNT),
                      SIDE_LENGTH * sin(i * 2 * pi / SIDES_COUNT))
                     for i in range(SIDES_COUNT)]

            nodes2 = [(int(self.xs(node[0])),
                       int(self.ys(node[1]))) for node in nodes]

            for i in range(self.m):  # отрисовываем каждую сторону
                n = 0
                a = (0, 0)
                for y in range(-1, len(nodes2) - 1):
                    n += 1
                    if n == 1:
                        a = nodes2[y]
                    if n == SIDES_COUNT:
                        qp.drawLine(*nodes2[y], *a)
                        # высчитываем новые координаты
                        nodes2[y] = (int((nodes2[y][0] + self.k * a[0]) / (self.k + 1)),
                                     int((nodes2[y][1] + self.k * a[1]) / (self.k + 1)))
                    else:
                        qp.drawLine(*nodes2[y], *nodes2[y + 1])
                        # высчитываем новые координаты
                        nodes2[y] = (int((nodes2[y][0] + self.k * nodes2[y + 1][0]) / (self.k + 1)),
                                     int((nodes2[y][1] + self.k * nodes2[y + 1][1]) / (self.k + 1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
