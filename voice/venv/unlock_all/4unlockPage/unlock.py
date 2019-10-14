# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unlock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import unlock_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_unlockPage(object):
    def setupUi(self, unlockPage):
        unlockPage.setObjectName("unlockPage")
        unlockPage.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(unlockPage)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(170, 5, 160, 160))
        self.graphicsView.setStyleSheet("border-image: url(:/1/re_unlock3.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.unlockVoiceBut = QtWidgets.QPushButton(self.centralwidget)
        self.unlockVoiceBut.setGeometry(QtCore.QRect(190, 175, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unlockVoiceBut.setFont(font)
        self.unlockVoiceBut.setObjectName("unlockVoiceBut")
        self.usePassBut = QtWidgets.QPushButton(self.centralwidget)
        self.usePassBut.setGeometry(QtCore.QRect(10, 240, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usePassBut.setFont(font)
        self.usePassBut.setObjectName("usePassBut")
        self.exitUnlockBut = QtWidgets.QPushButton(self.centralwidget)
        self.exitUnlockBut.setGeometry(QtCore.QRect(390, 240, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitUnlockBut.setFont(font)
        self.exitUnlockBut.setObjectName("exitUnlockBut")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 240, 100, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(320, 240, 50, 25))
        self.OK.setObjectName("OK")
        unlockPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(unlockPage)
        self.statusbar.setObjectName("statusbar")
        unlockPage.setStatusBar(self.statusbar)

        self.retranslateUi(unlockPage)
        QtCore.QMetaObject.connectSlotsByName(unlockPage)

    def retranslateUi(self, unlockPage):
        _translate = QtCore.QCoreApplication.translate
        unlockPage.setWindowTitle(_translate("unlockPage", "Safe Box"))
        self.unlockVoiceBut.setText(_translate("unlockPage", "Unlock by Voice"))
        self.usePassBut.setText(_translate("unlockPage", "Password"))
        self.exitUnlockBut.setText(_translate("unlockPage", "Exit"))
        self.OK.setText(_translate("unlockPage", "OK"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_unlockPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())