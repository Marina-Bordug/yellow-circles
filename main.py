import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from random import randint
from maindesign import Design


class Circles(Design, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(Circles)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circles(self, qp):
        for i in range(5):
            c1 = randint(1, 255)
            c2 = randint(1, 255)
            c3 = randint(1, 255)
            qp.setBrush(QColor(c1, c2, c3))
            qp.setPen(QColor(c1, c2, c3))
            a = randint(1, 200)
            b = randint(1, 200)
            qp.drawEllipse(a, a, b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
