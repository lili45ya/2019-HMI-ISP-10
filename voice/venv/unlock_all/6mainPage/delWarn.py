# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delWarn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import delWarn_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_delWarn(object):
    def setupUi(self, delWarn):
        delWarn.setObjectName("delWarn")
        delWarn.resize(400, 300)
        self.graphicsView = QtWidgets.QGraphicsView(delWarn)
        self.graphicsView.setGeometry(QtCore.QRect(120, 10, 160, 160))
        self.graphicsView.setStyleSheet("border-image: url(:/1/delWarn.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.warnLabel = QtWidgets.QLabel(delWarn)
        self.warnLabel.setGeometry(QtCore.QRect(0, 180, 400, 25))
        self.warnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warnLabel.setObjectName("warnLabel")
        self.delAnyway = QtWidgets.QPushButton(delWarn)
        self.delAnyway.setGeometry(QtCore.QRect(150, 210, 100, 25))
        self.delAnyway.setObjectName("delAnyway")
        self.back = QtWidgets.QPushButton(delWarn)
        self.back.setGeometry(QtCore.QRect(150, 245, 100, 25))
        self.back.setObjectName("back")

        self.retranslateUi(delWarn)
        QtCore.QMetaObject.connectSlotsByName(delWarn)

    def retranslateUi(self, delWarn):
        _translate = QtCore.QCoreApplication.translate
        delWarn.setWindowTitle(_translate("delWarn", "Warning"))
        self.warnLabel.setText(_translate("delWarn", "The deletetion cannot be cancelled."))
        self.delAnyway.setText(_translate("delWarn", "Delete"))
        self.back.setText(_translate("delWarn", "Back"))

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_delWarn()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
