# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FLogin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 281)
        Dialog.setMaximumSize(QtCore.QSize(480, 680))
        Dialog.setStyleSheet("border:0px solid rgb(255, 255, 255);\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:0px solid rgb(255, 255, 255);\n"
"border-style:outset;\n"
"background:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 187, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:0px solid rgb(255, 255, 255);\n"
"border-style:outset;\n"
"background:transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.Btn_Login = QtWidgets.QPushButton(Dialog)
        self.Btn_Login.setGeometry(QtCore.QRect(338, 110, 123, 123))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.Btn_Login.setFont(font)
        self.Btn_Login.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_Login.setObjectName("Btn_Login")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 290, 471, 391))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Btn_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_1.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_1.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_1.setFont(font)
        self.Btn_1.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_1.setObjectName("Btn_1")
        self.horizontalLayout.addWidget(self.Btn_1)
        self.Btn_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_2.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_2.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_2.setFont(font)
        self.Btn_2.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_2.setObjectName("Btn_2")
        self.horizontalLayout.addWidget(self.Btn_2)
        self.Btn_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_3.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_3.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_3.setFont(font)
        self.Btn_3.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_3.setObjectName("Btn_3")
        self.horizontalLayout.addWidget(self.Btn_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Btn_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_4.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_4.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_4.setFont(font)
        self.Btn_4.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_4.setObjectName("Btn_4")
        self.horizontalLayout_3.addWidget(self.Btn_4)
        self.Btn_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_5.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_5.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_5.setFont(font)
        self.Btn_5.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_5.setObjectName("Btn_5")
        self.horizontalLayout_3.addWidget(self.Btn_5)
        self.Btn_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_6.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_6.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_6.setFont(font)
        self.Btn_6.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_6.setObjectName("Btn_6")
        self.horizontalLayout_3.addWidget(self.Btn_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_7.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_7.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_7.setFont(font)
        self.Btn_7.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_7.setObjectName("Btn_7")
        self.horizontalLayout_2.addWidget(self.Btn_7)
        self.Btn_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_8.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_8.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_8.setFont(font)
        self.Btn_8.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_8.setObjectName("Btn_8")
        self.horizontalLayout_2.addWidget(self.Btn_8)
        self.Btn_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_9.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_9.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_9.setFont(font)
        self.Btn_9.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_9.setObjectName("Btn_9")
        self.horizontalLayout_2.addWidget(self.Btn_9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Btn_Switch = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_Switch.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_Switch.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Switch.setFont(font)
        self.Btn_Switch.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_Switch.setObjectName("Btn_Switch")
        self.horizontalLayout_4.addWidget(self.Btn_Switch)
        self.Btn_0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_0.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_0.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_0.setFont(font)
        self.Btn_0.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_0.setObjectName("Btn_0")
        self.horizontalLayout_4.addWidget(self.Btn_0)
        self.Btn_BackSpace = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_BackSpace.setMinimumSize(QtCore.QSize(135, 80))
        self.Btn_BackSpace.setMaximumSize(QtCore.QSize(135, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_BackSpace.setFont(font)
        self.Btn_BackSpace.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_BackSpace.setObjectName("Btn_BackSpace")
        self.horizontalLayout_4.addWidget(self.Btn_BackSpace)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius:4px;\n"
"border:0px solid rgb(255, 255, 255);\n"
"border-style:outset;\n"
"background:transparent;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Btn_Keyboard = QtWidgets.QPushButton(Dialog)
        self.Btn_Keyboard.setGeometry(QtCore.QRect(286, 193, 35, 35))
        self.Btn_Keyboard.setStyleSheet("border-radius:4px;\n"
"border:0px solid rgb(255, 255, 255);\n"
"border-style:outset;\n"
"background:transparent;")
        self.Btn_Keyboard.setText("")
        self.Btn_Keyboard.setIconSize(QtCore.QSize(32, 32))
        self.Btn_Keyboard.setObjectName("Btn_Keyboard")
        self.Lne_ID = QtWidgets.QLineEdit(Dialog)
        self.Lne_ID.setGeometry(QtCore.QRect(104, 112, 221, 41))
        self.Lne_ID.setStyleSheet("border-radius:4px;\n"
"border:1px solid rgb(111, 156, 207);")
        self.Lne_ID.setObjectName("Lne_ID")
        self.Lne_Passwd = QtWidgets.QLineEdit(Dialog)
        self.Lne_Passwd.setGeometry(QtCore.QRect(104, 190, 221, 41))
        self.Lne_Passwd.setStyleSheet("border-radius:4px;\n"
"border:1px solid rgb(111, 156, 207);")
        self.Lne_Passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Lne_Passwd.setObjectName("Lne_Passwd")
        self.Gpb_Warning = QtWidgets.QGroupBox(Dialog)
        self.Gpb_Warning.setGeometry(QtCore.QRect(70, 70, 331, 171))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Gpb_Warning.setFont(font)
        self.Gpb_Warning.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Gpb_Warning.setObjectName("Gpb_Warning")
        self.Lbl_Warning = QtWidgets.QLabel(self.Gpb_Warning)
        self.Lbl_Warning.setGeometry(QtCore.QRect(10, 40, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.Lbl_Warning.setFont(font)
        self.Lbl_Warning.setStyleSheet("border:0px solid rgb(255, 255, 255);\n"
"border-style:outset;\n"
"background:transparent;")
        self.Lbl_Warning.setAlignment(QtCore.Qt.AlignCenter)
        self.Lbl_Warning.setObjectName("Lbl_Warning")
        self.Btn_Warning = QtWidgets.QPushButton(self.Gpb_Warning)
        self.Btn_Warning.setGeometry(QtCore.QRect(80, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Warning.setFont(font)
        self.Btn_Warning.setStyleSheet("background-color: transparent;\n"
"border: 2px solid #555555;\n"
"border-radius: 6px;")
        self.Btn_Warning.setObjectName("Btn_Warning")
        self.Lne_Passwd.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.Btn_Login.raise_()
        self.groupBox.raise_()
        self.label_3.raise_()
        self.Btn_Keyboard.raise_()
        self.Lne_ID.raise_()
        self.Gpb_Warning.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小配料登陆"))
        self.label.setText(_translate("Dialog", "工号:"))
        self.label_2.setText(_translate("Dialog", "密码:"))
        self.Btn_Login.setText(_translate("Dialog", "登陆"))
        self.Btn_1.setText(_translate("Dialog", "1"))
        self.Btn_2.setText(_translate("Dialog", "2"))
        self.Btn_3.setText(_translate("Dialog", "3"))
        self.Btn_4.setText(_translate("Dialog", "4"))
        self.Btn_5.setText(_translate("Dialog", "5"))
        self.Btn_6.setText(_translate("Dialog", "6"))
        self.Btn_7.setText(_translate("Dialog", "7"))
        self.Btn_8.setText(_translate("Dialog", "8"))
        self.Btn_9.setText(_translate("Dialog", "9"))
        self.Btn_Switch.setText(_translate("Dialog", "Switch\n"
"更换"))
        self.Btn_0.setText(_translate("Dialog", "0"))
        self.Btn_BackSpace.setText(_translate("Dialog", "BackSpace\n"
"回格"))
        self.label_3.setText(_translate("Dialog", "小  配  料  系  统"))
        self.Lne_ID.setText(_translate("Dialog", "JUN"))
        self.Lne_Passwd.setText(_translate("Dialog", "123456"))
        self.Gpb_Warning.setTitle(_translate("Dialog", "警告"))
        self.Lbl_Warning.setText(_translate("Dialog", "警告内容"))
        self.Btn_Warning.setText(_translate("Dialog", "确定"))