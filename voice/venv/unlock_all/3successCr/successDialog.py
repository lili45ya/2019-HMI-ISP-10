# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import successCr_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_successDialog(object):
    def setupUi(self, successDialog):
        successDialog.setObjectName("successDialog")
        successDialog.resize(400, 300)
        self.graphicsView = QtWidgets.QGraphicsView(successDialog)
        self.graphicsView.setGeometry(QtCore.QRect(100, 20, 200, 200))
        self.graphicsView.setStyleSheet("border-image: url(:/success/check.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(successDialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 100, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(successDialog)
        QtCore.QMetaObject.connectSlotsByName(successDialog)

    def retranslateUi(self, successDialog):
        _translate = QtCore.QCoreApplication.translate
        successDialog.setWindowTitle(_translate("successDialog", "Dialog"))
        self.pushButton.setText(_translate("successDialog", "Back"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_successDialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())