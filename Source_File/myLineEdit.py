from PyQt5 import QtCore, QtWidgets

class myLineEdit(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()