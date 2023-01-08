import sys

import difflib

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('other_tasks/antiplagiat/prog.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.PushButton.clicked.connect(self.sravnit)

    def sravnit(self):
        str1 = self.str1.toPlainText()
        str2 = self.str2.toPlainText()

        y = difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100
        if self.Porog.text():
            if int(self.Porog.text()) >= round(y, 2):
                self.label.setText(f"Текст похож на {round(y, 2)}%")
                self.label.setStyleSheet('QLabel {background-color: green;}')
            else:
                self.label.setText(f"Текст похож на {round(y, 2)}%")
                self.label.setStyleSheet('QLabel {background-color: red;}')
        else:
            self.label.setText("Введите порог сравнения")
            self.label.setStyleSheet('QLabel {background-color: red;}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())