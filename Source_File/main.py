import sys
from PyQt5 import QtWidgets
import Login_UI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Login_UI.Login_UI()
    Dialog.show()
    sys.exit(app.exec_())