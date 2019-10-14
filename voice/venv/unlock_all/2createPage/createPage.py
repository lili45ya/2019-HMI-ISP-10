# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import createPage_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_crPage(object):
    def setupUi(self, crPage):
        crPage.setObjectName("crPage")
        crPage.resize(500, 300)
        crPage.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(crPage)
        self.centralwidget.setObjectName("centralwidget")
        self.crPic = QtWidgets.QGraphicsView(self.centralwidget)
        self.crPic.setGeometry(QtCore.QRect(0, 70, 200, 160))
        self.crPic.setStyleSheet("border-image: url(:/cPage/1.png);")
        self.crPic.setObjectName("crPic")
        self.yourPassword = QtWidgets.QLabel(self.centralwidget)
        self.yourPassword.setGeometry(QtCore.QRect(200, 70, 140, 25))
        self.yourPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yourPassword.setObjectName("yourPassword")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 140, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.yourPassword_2 = QtWidgets.QLabel(self.centralwidget)
        self.yourPassword_2.setGeometry(QtCore.QRect(200, 150, 140, 25))
        self.yourPassword_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yourPassword_2.setObjectName("yourPassword_2")
        self.recordLogo = QtWidgets.QPushButton(self.centralwidget)
        self.recordLogo.setGeometry(QtCore.QRect(200, 180, 90, 25))
        self.recordLogo.setObjectName("recordLogo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 245, 280, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        crPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(crPage)
        self.statusbar.setObjectName("statusbar")
        crPage.setStatusBar(self.statusbar)

        self.retranslateUi(crPage)
        QtCore.QMetaObject.connectSlotsByName(crPage)

    def retranslateUi(self, crPage):
        _translate = QtCore.QCoreApplication.translate
        crPage.setWindowTitle(_translate("crPage", "Safe Box - Create Account"))
        self.yourPassword.setText(_translate("crPage", "Your Password:"))
        self.yourPassword_2.setText(_translate("crPage", "Record Voice:"))
        self.recordLogo.setText(_translate("crPage", "Record"))
        self.label.setText(_translate("crPage", "Your Voice data will be stored locally"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_crPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
