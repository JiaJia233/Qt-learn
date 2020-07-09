# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'UI_File\FQR.ui'
# Created by: PyQt5 UI code generator 5.12
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Lbl_Video = QtWidgets.QLabel(self.centralwidget)
        self.Lbl_Video.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Lbl_Video.setObjectName("Lbl_Video")
        self.Btn_Con = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Con.setGeometry(QtCore.QRect(970, 10, 161, 71))
        self.Btn_Con.setObjectName("Btn_Con")
        self.Btn_Send = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Send.setGeometry(QtCore.QRect(970, 110, 161, 71))
        self.Btn_Send.setObjectName("Btn_Send")
        self.Txt_Detect = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_Detect.setGeometry(QtCore.QRect(10, 560, 1121, 41))
        self.Txt_Detect.setObjectName("Txt_Detect")
        self.Txt_Host = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_Host.setGeometry(QtCore.QRect(970, 200, 161, 31))
        self.Txt_Host.setObjectName("Txt_Host")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Lbl_Video.setText(_translate("MainWindow", "视频流"))
        self.Btn_Con.setText(_translate("MainWindow", "连接相机"))
        self.Btn_Send.setText(_translate("MainWindow", "发送数据"))


