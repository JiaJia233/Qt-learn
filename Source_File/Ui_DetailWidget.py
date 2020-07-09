# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work_Space\work_test\Python\Numpad\DetailWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetailWidget(object):
    def setupUi(self, DetailWidget):
        DetailWidget.setObjectName("DetailWidget")
        DetailWidget.resize(200, 60)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DetailWidget)
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetMain = QtWidgets.QWidget(DetailWidget)
        self.widgetMain.setMinimumSize(QtCore.QSize(1, 1))
        self.widgetMain.setMaximumSize(QtCore.QSize(1000, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widgetMain.setFont(font)
        self.widgetMain.setStyleSheet("QWidget{background-color: rgb(153, 70, 99);}\n"
"QPushButton:hover {\n"
"    \n"
" background-color: rgb(0, 0, 255);\n"
" }\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.widgetMain.setObjectName("widgetMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetMain)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnF1 = QtWidgets.QPushButton(self.widgetMain)
        self.btnF1.setMinimumSize(QtCore.QSize(60, 60))
        self.btnF1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnF1.setText("")
        self.btnF1.setAutoRepeat(False)
        self.btnF1.setAutoDefault(False)
        self.btnF1.setDefault(False)
        self.btnF1.setFlat(True)
        self.btnF1.setObjectName("btnF1")
        self.horizontalLayout.addWidget(self.btnF1)
        self.btnF2 = QtWidgets.QPushButton(self.widgetMain)
        self.btnF2.setMinimumSize(QtCore.QSize(60, 60))
        self.btnF2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnF2.setText("")
        self.btnF2.setFlat(True)
        self.btnF2.setObjectName("btnF2")
        self.horizontalLayout.addWidget(self.btnF2)
        self.btnF3 = QtWidgets.QPushButton(self.widgetMain)
        self.btnF3.setMinimumSize(QtCore.QSize(60, 60))
        self.btnF3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnF3.setText("")
        self.btnF3.setFlat(True)
        self.btnF3.setObjectName("btnF3")
        self.horizontalLayout.addWidget(self.btnF3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widgetMain)

        self.retranslateUi(DetailWidget)
        QtCore.QMetaObject.connectSlotsByName(DetailWidget)

    def retranslateUi(self, DetailWidget):
        _translate = QtCore.QCoreApplication.translate
        DetailWidget.setWindowTitle(_translate("DetailWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetailWidget = QtWidgets.QWidget()
    ui = Ui_DetailWidget()
    ui.setupUi(DetailWidget)
    DetailWidget.show()
    sys.exit(app.exec_())

