import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('beauty.jpg')
        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)
        hbox.addWidget(lb1)
        self.setLayout(hbox)
        self.move(300, 300)
        self.setWindowTitle('像素图控件')
        self.show()     

    def showDate(self, date):
        self.lb1.setText(date.toString())     


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
