# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\w0404884\OneDrive - Nova Scotia Community College\Courses\PROG-1700 - Logic Prog\Week12\UISamples\RadioButtons\RadioButtons.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(178, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButtonRed = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRed.setGeometry(QtCore.QRect(20, 160, 82, 17))
        self.radioButtonRed.setChecked(True)
        self.radioButtonRed.setObjectName("radioButtonRed")
        self.radioButtonGreen = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonGreen.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.radioButtonGreen.setObjectName("radioButtonGreen")
        self.radioButtonBlue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBlue.setGeometry(QtCore.QRect(100, 180, 82, 17))
        self.radioButtonBlue.setObjectName("radioButtonBlue")
        self.radioButtonYellow = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonYellow.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButtonYellow.setObjectName("radioButtonYellow")
        self.labelColor = QtWidgets.QLabel(self.centralwidget)
        self.labelColor.setGeometry(QtCore.QRect(10, 10, 151, 141))
        self.labelColor.setStyleSheet("background-color:red;")
        self.labelColor.setText("")
        self.labelColor.setObjectName("labelColor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 178, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Colors"))
        self.radioButtonRed.setText(_translate("MainWindow", "Red"))
        self.radioButtonGreen.setText(_translate("MainWindow", "Green"))
        self.radioButtonBlue.setText(_translate("MainWindow", "Blue"))
        self.radioButtonYellow.setText(_translate("MainWindow", "Yellow"))

