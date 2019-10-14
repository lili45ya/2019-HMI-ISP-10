# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voiceFail2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import failed_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_voiceFail2(object):
    def setupUi(self, voiceFail2):
        voiceFail2.setObjectName("voiceFail2")
        voiceFail2.resize(400, 300)
        self.graphicsView = QtWidgets.QGraphicsView(voiceFail2)
        self.graphicsView.setGeometry(QtCore.QRect(122, 20, 156, 168))
        self.graphicsView.setStyleSheet("border-image: url(:/1/failed.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.tryAgain = QtWidgets.QPushButton(voiceFail2)
        self.tryAgain.setGeometry(QtCore.QRect(150, 210, 100, 25))
        self.tryAgain.setObjectName("tryAgain")
        self.thenPassword = QtWidgets.QPushButton(voiceFail2)
        self.thenPassword.setGeometry(QtCore.QRect(150, 250, 100, 25))
        self.thenPassword.setObjectName("thenPassword")

        self.retranslateUi(voiceFail2)
        QtCore.QMetaObject.connectSlotsByName(voiceFail2)

    def retranslateUi(self, voiceFail2):
        _translate = QtCore.QCoreApplication.translate
        voiceFail2.setWindowTitle(_translate("voiceFail2", "Decrypt Failed"))
        self.tryAgain.setText(_translate("voiceFail2", "Try Again"))
        self.thenPassword.setText(_translate("voiceFail2", "Password"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_voiceFail2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())