import sys
from random import randint
from design import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSorteio.clicked.connect(self.sorteia_num)

    def sorteia_num(self):
            gerador_num = randint(0, 69)
            gerador_num = str(gerador_num)

            self.numeroSorteado.setText(gerador_num)

    
if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
