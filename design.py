# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 379)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.numeroSorteado = QtWidgets.QLabel(self.centralwidget)
        self.numeroSorteado.setGeometry(QtCore.QRect(20, 170, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(47)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.numeroSorteado.setFont(font)
        self.numeroSorteado.setText("")
        self.numeroSorteado.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.numeroSorteado.setObjectName("numeroSorteado")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 481, 121))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnSorteio = QtWidgets.QPushButton(self.centralwidget)
        self.btnSorteio.setGeometry(QtCore.QRect(180, 330, 134, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSorteio.sizePolicy().hasHeightForWidth())
        self.btnSorteio.setSizePolicy(sizePolicy)
        self.btnSorteio.setObjectName("btnSorteio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sorteador de números"))
        self.label.setText(_translate("MainWindow", "O número sorteado foi..."))
        self.btnSorteio.setText(_translate("MainWindow", "Clique para sortear"))