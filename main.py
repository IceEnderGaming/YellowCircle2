import sys
import random

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.paint_flag = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.paint_flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint_flag is True:
            qp = QPainter()
            qp.begin(self)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setBrush(color)
            self.drawCircle(qp)

    def drawCircle(self, qp):
        radius = random.randint(0, 100)
        qp.drawEllipse(random.randint(0, 500), random.randint(0, 500), radius, radius)
        self.paint_flag = False


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
