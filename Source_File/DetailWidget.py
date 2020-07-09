# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

import Ui_DetailWidget


class DetailWidget(QWidget, Ui_DetailWidget.Ui_DetailWidget):
	signalText = QtCore.pyqtSignal(str)

	def __init__(self):
		super(DetailWidget, self).__init__()
		self.setupUi(self)
		self.setWindowFlags(Qt.WindowDoesNotAcceptFocus | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.btnF1.clicked.connect(self.on_btn_f1_clicked)
		self.btnF2.clicked.connect(self.on_btn_f2_clicked)
		self.btnF3.clicked.connect(self.on_btn_f3_clicked)
		# self.hide()

	def on_btn_f1_clicked(self):
		self.signalText.emit(self.btnF1.text())
		self.hide()

	def on_btn_f2_clicked(self):
		self.signalText.emit(self.btnF2.text())
		self.hide()

	def on_btn_f3_clicked(self):
		self.signalText.emit(self.btnF3.text())
		self.hide()

	def set_small_pad_text(self, strlist):
		self.btnF1.setText(strlist[0])
		self.btnF2.setText(strlist[1])
		self.btnF3.setText(strlist[2])

		if self.btnF3.text().strip() == '':
			self.btnF3.hide()
			self.setMinimumWidth(120)
			self.setMaximumWidth(120)
		else:
			self.btnF3.show()
			self.setMinimumWidth(200)
		self.setWindowFlags(Qt.WindowDoesNotAcceptFocus | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.show()


