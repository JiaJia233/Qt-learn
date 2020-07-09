import FLogin
import DetailWidget
import Datacall
import Main_UI
from PyQt5 import QtCore, QtWidgets, QtGui
import os


class Login_UI(QtWidgets.QDialog, FLogin.Ui_Dialog):
    clicked = QtCore.pyqtSignal()
    removed = QtCore.pyqtSignal()
    Signal_Txt = QtCore.pyqtSignal(str)
    Input_Status = False
    Focus_Status = False
    Keyboard_Status = False
    windowList = []

    def __init__(self):
        super(Login_UI, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.m_pDetailWidget = DetailWidget.DetailWidget()
        self.m_pDetailWidget.signalText.connect(self.Slot_Txt)
        url = os.path.dirname(os.path.abspath(__file__))
        url = url + "/Image_File/icon/keyboard.png"
        self.Btn_Keyboard.setIcon(QtGui.QIcon(url))
        self.groupBox.hide()
        self.Gpb_Warning.hide()
        self.resize(480, 281)
        self.Signal_Slot()

    def __del__(self):
        self.m_pDetailWidget.close()

    def Signal_Slot(self):
        self.Btn_Login.clicked.connect(self.Login)
        self.Btn_Keyboard.clicked.connect(self.Keyboard_Show)
        self.Btn_Warning.clicked.connect(self.Warning_Slot)
        self.Lne_ID.installEventFilter(self)
        self.clicked.connect(self.IDFocus_Slot)
        self.Lne_Passwd.installEventFilter(self)
        self.removed.connect(self.PassFocus_Slot)
        self.Btn_Switch.clicked.connect(self.BtnSwitch_Function)
        self.Btn_BackSpace.clicked.connect(self.BtnBackspace_Function)
        self.Btn_1.clicked.connect(self.Btn1_Function)
        self.Btn_2.clicked.connect(self.Btn2_Function)
        self.Btn_3.clicked.connect(self.Btn3_Function)
        self.Btn_4.clicked.connect(self.Btn4_Function)
        self.Btn_5.clicked.connect(self.Btn5_Function)
        self.Btn_6.clicked.connect(self.Btn6_Function)
        self.Btn_7.clicked.connect(self.Btn7_Function)
        self.Btn_8.clicked.connect(self.Btn8_Function)
        self.Btn_9.clicked.connect(self.Btn9_Function)
        self.Btn_0.clicked.connect(self.Btn0_Function)

    def Set_PadText(self, TxtList):
        self.Btn_1.setText(TxtList[0])
        self.Btn_2.setText(TxtList[1])
        self.Btn_3.setText(TxtList[2])
        self.Btn_4.setText(TxtList[3])
        self.Btn_5.setText(TxtList[4])
        self.Btn_6.setText(TxtList[5])
        self.Btn_7.setText(TxtList[6])
        self.Btn_8.setText(TxtList[7])
        self.Btn_9.setText(TxtList[8])
        self.Btn_0.setText(TxtList[9])

    def Login(self):
        Data = Datacall.GetData("Select * from t_member where f_name = '" + self.Lne_ID.text() + "'")
        if Data != []:
            print(str(Data[0]['f_passwd']))
            if Data[0]['f_passwd'] == self.Lne_Passwd.text():
                self.Lne_ID.clear()
                self.Lne_Passwd.clear()
                self.close()
                Main = Main_UI.MainUI()
                Main.show()
                self.windowList.append(Main)
            else:
                self.Lne_ID.clear()
                self.Lne_Passwd.clear()
                self.Warning("密码错误，请重新输入!")
        else:
            self.Lne_ID.clear()
            self.Lne_Passwd.clear()
            self.Warning("账号不存在，请重新输入!")

    def Keyboard_Show(self):
        if not self.Keyboard_Status:
            self.resize(480, 680)
            self.groupBox.show()
            self.Keyboard_Status = True
        else:
            self.resize(480, 281)
            self.groupBox.hide()
            self.Keyboard_Status = False
            self.m_pDetailWidget.close()

    def Btn1_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("1")
            else:
                self.Lne_Passwd.insert("1")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_1.text())
            m_pPoint = self.groupBox.pos() + self.Btn_1.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn2_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("2")
            else:
                self.Lne_Passwd.insert("2")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_2.text())
            m_pPoint = self.groupBox.pos() + self.Btn_2.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn3_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("3")
            else:
                self.Lne_Passwd.insert("3")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_3.text())
            m_pPoint = self.groupBox.pos() + self.Btn_3.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn4_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("4")
            else:
                self.Lne_Passwd.insert("4")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_4.text())
            m_pPoint = self.groupBox.pos() + self.Btn_4.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn5_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("5")
            else:
                self.Lne_Passwd.insert("5")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_5.text())
            m_pPoint = self.groupBox.pos() + self.Btn_5.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn6_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("6")
            else:
                self.Lne_Passwd.insert("6")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_6.text())
            m_pPoint = self.groupBox.pos() + self.Btn_6.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn7_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("7")
            else:
                self.Lne_Passwd.insert("7")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_7.text())
            m_pPoint = self.groupBox.pos() + self.Btn_7.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn8_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("8")
            else:
                self.Lne_Passwd.insert("8")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_8.text())
            m_pPoint = self.groupBox.pos() + self.Btn_8.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 15, m_pPoint.y() - 20)

    def Btn9_Function(self):
        if not self.Input_Status:
            if not self.Focus_Status:
                self.Lne_ID.insert("9")
            else:
                self.Lne_Passwd.insert("9")
        else:
            _Str = 'Y;Z;'
            _StrList = _Str.split(";")
            self.m_pDetailWidget.set_small_pad_text(_StrList)
            m_pPoint = self.groupBox.pos() + self.Btn_9.pos() + self.pos()
            self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 20)

    def Btn0_Function(self):
        if not self.Focus_Status:
            self.Lne_ID.insert("0")
        else:
            self.Lne_Passwd.insert("0")

    def BtnSwitch_Function(self):
        if not self.Input_Status:
            self.Input_Status = True
            _Str = 'ABC;DEF;GHI;JKL;MNO;PQR;STU;VWX;YZ;0'
            _StrList = _Str.split(';')
            self.Set_PadText(_StrList)
        else:
            self.Input_Status = False
            _Str = '1;2;3;4;5;6;7;8;9;0'
            _StrList = _Str.split(';')
            self.Set_PadText(_StrList)

    def BtnBackspace_Function(self):
        if not self.Focus_Status:
            self.Lne_ID.backspace()
        else:
            self.Lne_Passwd.backspace()

    def Send_Txt(self):
        self.Signal_Txt.emit(self.Lne_ID.text())
        self.Lne_ID.clear()
        self.Lne_Passwd.clear()

    def Slot_Txt(self, Str):
        if not self.Focus_Status:
            self.Lne_ID.insert(Str)
        else:
            self.Lne_Passwd.insert(Str)

    def IDFocus_Slot(self):
        self.Focus_Status = False

    def PassFocus_Slot(self):
        self.Focus_Status = True

    def Warning_Slot(self):
        self.Gpb_Warning.hide()

    def eventFilter(self, QObject, QEvent):
        if QObject == self.Lne_ID:
            if QEvent.type() == QtCore.QEvent.FocusIn:
                self.clicked.emit()

        elif QObject == self.Lne_Passwd:
            if QEvent.type() == QtCore.QEvent.FocusIn:
                self.removed.emit()
        return False

    def Warning(self, Str):
        self.Gpb_Warning.show()
        self.Lbl_Warning.setText(Str)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = Login_UI()
#     Dialog.show()
#     sys.exit(app.exec_())