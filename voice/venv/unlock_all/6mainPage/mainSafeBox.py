# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainSafeBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import delWarn
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from delWarn import Ui_delWarn

class Ui_mainSafeBox(object):
    def setupUi(self, mainSafeBox):
        mainSafeBox.setObjectName("mainSafeBox")
        mainSafeBox.resize(750, 450)
        self.centralwidget = QtWidgets.QWidget(mainSafeBox)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 550, 450))
        self.graphicsView.setObjectName("graphicsView")
        self.addBut = QtWidgets.QPushButton(self.centralwidget)
        self.addBut.setGeometry(QtCore.QRect(590, 305, 100, 25))
        self.addBut.setObjectName("addBut")
        self.lockBut = QtWidgets.QPushButton(self.centralwidget)
        self.lockBut.setGeometry(QtCore.QRect(590, 380, 100, 25))
        self.lockBut.setObjectName("lockBut")
        self.order = QtWidgets.QLabel(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(590, 170, 100, 25))
        self.order.setObjectName("order")
        self.timeOrder = QtWidgets.QCheckBox(self.centralwidget)
        self.timeOrder.setGeometry(QtCore.QRect(590, 200, 100, 25))
        self.timeOrder.setObjectName("timeOrder")
        self.typeOrder = QtWidgets.QCheckBox(self.centralwidget)
        self.typeOrder.setGeometry(QtCore.QRect(590, 230, 100, 25))
        self.typeOrder.setObjectName("typeOrder")
        self.chooseBut = QtWidgets.QPushButton(self.centralwidget)
        self.chooseBut.setGeometry(QtCore.QRect(590, 40, 100, 25))
        self.chooseBut.setObjectName("chooseBut")
        self.deleteBut = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBut.setGeometry(QtCore.QRect(590, 75, 100, 25))
        self.deleteBut.setObjectName("deleteBut")
        mainSafeBox.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainSafeBox)
        self.statusbar.setObjectName("statusbar")
        mainSafeBox.setStatusBar(self.statusbar)

        self.retranslateUi(mainSafeBox)
        QtCore.QMetaObject.connectSlotsByName(mainSafeBox)
    #     add
        self.deleteBut.clicked.connect(self.show_dialog)


    def show_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_delWarn()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def retranslateUi(self, mainSafeBox):
        _translate = QtCore.QCoreApplication.translate
        mainSafeBox.setWindowTitle(_translate("mainSafeBox", "Your Open Box"))
        self.addBut.setText(_translate("mainSafeBox", "Add"))
        self.lockBut.setText(_translate("mainSafeBox", "Lock"))
        self.order.setText(_translate("mainSafeBox", "Order by:"))
        self.timeOrder.setText(_translate("mainSafeBox", "Time"))
        self.typeOrder.setText(_translate("mainSafeBox", "Type"))
        self.chooseBut.setText(_translate("mainSafeBox", "Choose"))
        self.deleteBut.setText(_translate("mainSafeBox", "Delete"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainSafeBox()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
