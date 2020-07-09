from PyQt5 import QtWidgets, QtCore, QtGui
import Datacall
import FMain
import DetailWidget
import Login_UI
import datetime
import os
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout

class MainUI(QtWidgets.QMainWindow, FMain.Ui_MainWindow):
    count = 0
    step = 0
    max_count = 0
    Material_Wt = 0
    state = False
    limit = False
    value = 0
    Temp_Wt = 0
    Input_Status = False
    windowList = []

    # 1.扫码获取工位号，根据工位号获取罐体号和介质号(按顺序)
    # 2.确认罐体皮重
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        url = os.path.dirname(os.path.abspath(__file__))
        url = url + "/Image_File/icon/keyboard.ico"
        self.Btn_Keyboard.setIcon(QtGui.QIcon(url))
        self.Lne_QR.setFocus()
        self.groupBox.hide()
        self.Grp_Warning.hide()
        self.m_pDetailWidget = DetailWidget.DetailWidget()
        self.m_pDetailWidget.signalText.connect(self.Slot_Txt)
        self.Timer = QtCore.QTimer()
        # self.Timer_Balance = QtCore.QTimer()
        # self.Balance = Balance.BalanceData()
        self.Init_Function()
        # self.Timer_Balance.start(5)
        self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请先使用砝码进行磅秤校验!")
        self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   磅秤校验完毕后请扫描工位编码!")
        # self.Init_Widgets()

    def __del__(self):
        # self.Timer_Balance.stop()
        self.Timer.stop()

    # 初始化按键功能，二维码数据一获取到马上调用二维码识别功能
    def Init_Function(self):
        self.Lne_QR.returnPressed.connect(self.Code_Recognition)
        self.Btn_Weigh.clicked.connect(self.Finish)
        self.Btn_Warning.clicked.connect(self.Warning_Slot)
        self.KeyBoard_Slot()
        self.Timer.timeout.connect(self.Timeout_respone)
        self.Btn_Login.clicked.connect(self.Login_Slot)
        # self.Timer_Balance.timeout.connect(self.Timeout_respone_wt)

    # 获取工位号，进行充装的数据获取
    def Get_Formula(self):
        try:
            self.Material = Datacall.GetData("Select * from t_material where f_formula = " + self.Lne_QR.text() + " Order By f_id ASC")
            self.Formula = Datacall.GetData("Select * from t_formula where f_formula = " + self.Lne_QR.text() + " AND f_batch = '0'")
            if self.Material and self.Formula:
                self.Txe_Recode.clear()
                self.Lne_Formule.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.Lne_Formule.setText(self.Formula[0]["f_formula"])
                self.max_count = len(self.Material)
                self.step = 1
                self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   工位号:" + self.Formula[0]["f_formula"] + "开始充装!")
                self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请扫描对应罐体的编码!")

            else:
                self.Lne_QR.clear()
                self.Lne_Formule.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.Lne_QR.setFocus()
                self.Warning("未找到对应充装订单，请确认!")

        except Exception as e:
            print(e)

    # 获取罐体相关信息
    def Get_Drum(self):
        try:
            self.Drum = Datacall.GetData("Select * from t_drum where f_drum = " + self.Lne_QR.text())
            if self.Drum:
                self.Compare_Drum()
            else:
                self.Lne_QR.clear()
                self.Lne_QR.setFocus()
                self.Warning("未找到对应充装罐体号，请确认!")

        except Exception as e:
            print(e)

    # 比较罐的类别及确认罐的毛重误差
    def Compare_Drum(self):
        try:
            if self.Drum[0]['f_drumtype'] == self.Formula[0]['f_drumtype']:
                Act_Wt = float(self.Lbl_Wt.text())
                Up_Wt = float(self.Drum[0]['f_wt']) * (1 + float(self.Drum[0]['f_diff']))
                Down_Wt = float(self.Drum[0]['f_wt']) * (1 - float(self.Drum[0]['f_diff']))
                self.Lne_Pail.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.Lne_PailWt.setText(str(self.Drum[0]['f_wt']))
                self.Lne_Pail.setText(self.Drum[0]["f_drum"])
                if (Act_Wt <= Up_Wt) and (Act_Wt >= Down_Wt):
                    self.Lne_PailWt.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.step = 2
                    self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   罐号:" + self.Drum[0]["f_drum"] + "匹配成功，罐体类型为:" + self.Drum[0]["f_drumtype"])
                    self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请扫描第1种原料编码进行确认!")
                else:
                    self.Lne_QR.clear()
                    self.Lne_PailWt.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.Lne_QR.setFocus()
                    self.Warning("罐体重量异常，请确认!")

            else:
                self.Lne_QR.clear()
                self.self.Lne_Pail.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.Lne_QR.setFocus()
                self.Warning("罐体类型不匹配，请确认!")

        except Exception as e:
            print(e)

    # 通知PLC开关

    # 介质匹配
    def Compare_Material(self):
        try:
            if self.state == False:
                if self.Lne_QR.text() == self.Material[self.count]["f_material"]:
                    if self.count == 0:
                        self.Timer.start(1000)
                        self.Temp_Wt += int(self.Lbl_Wt.text())
                        self.self.Lne_Material.setStyleSheet("background-color: rgb(0, 255, 0);")
                        self.Material_Wt = float(self.Material[self.count]["f_scale"]) * int(self.Formula[0]["f_wt"])
                        self.Lne_Material.setText(self.Material[self.count]["f_material"])
                        self.Lne_MaterialWt.setText(str(self.Material_Wt))
                        self.Lne_PreError.setText(str(self.Material[self.count]["f_diff"]))
                        self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   开始第" + str(self.count + 1) + "种原料的投入, 原料号为:" + self.Lne_Material.text())
                        self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请扫描第" + str(self.count + 2) + "种原料编码进行确认!")
                    else:
                        Act_Wt = float(self.Lbl_Wt.text())
                        Up_Wt = self.Material_Wt * float(1 + self.Material[self.count - 1]["f_diff"])
                        Down_Wt = self.Material_Wt * float(1 - self.Material[self.count - 1]["f_diff"])
                        if (Act_Wt >= Down_Wt) and (Act_Wt <= Up_Wt):
                            self.Temp_Wt += int(self.Lbl_Wt.text())
                            self.Lne_Material.setStyleSheet("background-color: rgb(0, 255, 0);")
                            self.Lne_MaterialWt.setStyleSheet("")
                            self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   第" + str(self.count + 1) + "种原料的投入完毕, 原料号为:" + self.Lne_Material.text())
                            self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请扫描第" + str(self.count + 2) + "种原料编码进行确认!")
                            self.Material_Wt = float(self.Material[self.count]["f_scale"]) * int(self.Formula[0]["f_wt"])
                            self.Lne_Material.setText(self.Material[self.count]["f_material"])
                            self.Lne_MaterialWt.setText(str(self.Material_Wt))
                            self.Lne_PreError.setText(str(self.Material[self.count]["f_diff"]))
                            self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   开始第" + str(self.count + 1) + "种原料的投入, 原料号为:" + self.Lne_Material.text())
                        else:
                            self.count -= self.count
                            self.Lne_QR.clear()
                            self.Lne_MaterialWt.setStyleSheet("background-color: rgb(255, 0, 0);")
                            self.Lne_QR.setFocus()
                            self.Warning("介质重量不达标，请确认!")
                    if self.count < self.max_count - 1:
                        self.count = self.count + 1
                    else:
                        self.state = True
                else:
                    self.Lne_QR.clear()
                    self.Lne_Material.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.Lne_QR.setFocus()
                    self.Warning("当前介质与所需介质不匹配，请确认!")
            else:
                self.Lne_QR.clear()
                self.Lne_QR.setFocus()
                self.Warning("请点击按钮完成充装！")

        except Exception as e:
            print(e)

    # 完成
    def Finish(self):
        try:
            if self.state == True:
                Act_Wt = float(self.Lbl_Wt.text())
                Up_Wt = self.Material_Wt * float(1 + self.Material[self.max_count - 1]["f_diff"])
                Down_Wt = self.Material_Wt * float(1 - self.Material[self.max_count - 1]["f_diff"])
                if (Act_Wt >= Down_Wt) and (Act_Wt <= Up_Wt):
                    self.Lne_MaterialWt.setStyleSheet("")
                    self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   第" + str(self.count + 1) + "种原料的投入完毕, 原料号为:" + self.Lne_Material.text())
                    self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   请点击充装完成按钮进行结束操作!")
                    self.Timer.stop()
                    self.progressBar.setValue(0)
                    self.Lne_Material.clear()
                    self.Lne_MaterialWt.clear()
                    self.Lne_PreError.clear()
                    self.Lne_Formule.clear()
                    self.Lne_Pail.clear()
                    self.Lne_PailWt.clear()
                    self.state = False
                    self.step = 0
                    self.Material_Wt = 0
                    self.count = 0
                    self.max_count = 0
                    self.Temp_Wt = 0
                    self.Txe_Recode.appendPlainText(str(datetime.datetime.now()) + "   充装订单:" + self.Formula[0]["f_formula"] + "已完成全部充装!")
                    del self.Material[:]
                    del self.Formula[:]
                    del self.Drum[:]
                else:
                    self.Lne_QR.clear()
                    self.Lne_MaterialWt.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.Lne_QR.setFocus()
                    self.Warning("充装重量不达标，请确认!")
            else:
                self.Lne_QR.clear()
                self.Lne_QR.setFocus()
                self.Warning("充装未完成!")

        except Exception as e:
            print(e)
        self.Lne_QR.setFocus()

    # 二维码识别
    def Code_Recognition(self):
        if self.step == 0:
            self.Get_Formula()

        elif self.step == 1:
            self.Get_Drum()
        else:
            self.Compare_Material()

        self.Lne_QR.clear()
        self.Lne_QR.setFocus()

    def Timeout_respone(self):
        self.value =round(int(self.Lbl_Wt.text())/self.Material_Wt, 2) * 100
        self.progressBar.setValue(self.value)
        if self.value >= 90:
            self.progressBar.setStyleSheet("QProgressBar::chunk {   background-color: #FF0000;   width: 20px;} QProgressBar {   border: 2px solid grey;   border-radius: 5px;   text-align: center;}")
        else:
            self.progressBar.setStyleSheet("QProgressBar::chunk {   background-color: #00EC00;   width: 20px;} QProgressBar {   border: 2px solid grey;   border-radius: 5px;   text-align: center;}")

        if self.value > 100:
            self.progressBar.setValue(100)
            self.progressBar.setStyleSheet("QProgressBar::chunk {   background-color: #FF0000;   width: 20px;} QProgressBar {   border: 2px solid grey;   border-radius: 5px;   text-align: center;}")

    #def Timeout_respone_wt(self):
    #     result = self.Balance.Data_Recv()
    #     if result >= 0:
    #         self.Lbl_Wt.setText(str(round(result * 1000) - self.Temp_Wt))

        # Material_Wt = float(self.Material[self.count]["f_scale"]) * int(self.Formula[0]["f_wt"])
        # Lne_Material.setText(self.Material[self.count]["f_material"])
        # Lne_MaterialWt.setText(str(self.Material_Wt))


    # 虚拟键盘
    def KeyBoard_Show(self):
        self.groupBox.show()

    def Btn1_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("1")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_1.text())
            m_pPoint = self.groupBox.pos() + self.Btn_1.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn2_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("2")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_2.text())
            m_pPoint = self.groupBox.pos() + self.Btn_2.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn3_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("3")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_3.text())
            m_pPoint = self.groupBox.pos() + self.Btn_3.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn4_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("4")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_4.text())
            m_pPoint = self.groupBox.pos() + self.Btn_4.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn5_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("5")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_5.text())
            m_pPoint = self.groupBox.pos() + self.Btn_5.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn6_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("6")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_6.text())
            m_pPoint = self.groupBox.pos() + self.Btn_6.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn7_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("7")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_7.text())
            m_pPoint = self.groupBox.pos() + self.Btn_7.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn8_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("8")
        else:
            self.m_pDetailWidget.set_small_pad_text(self.Btn_8.text())
            m_pPoint = self.groupBox.pos() + self.Btn_8.pos()
            self.m_pDetailWidget.move(m_pPoint.x() - 42, m_pPoint.y() - 60)

    def Btn9_Function(self):
        if not self.Input_Status:
            self.Lne_QR.insert("9")
        else:
            _Str = 'Y;Z;'
            _StrList = _Str.split(";")
            self.m_pDetailWidget.set_small_pad_text(_StrList)
            m_pPoint = self.groupBox.pos() + self.Btn_9.pos()
            self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 60)

    def Btn0_Function(self):
        self.Lne_QR.insert("0")

    def BtnPoint_Function(self):
        self.Lne_QR.insert(".")

    def BtnHyphen_Function(self):
        self.Lne_QR.insert("-")

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
        self.Lne_QR.backspace()

    def BtnEnter_Function(self):
        self.Code_Recognition()

    def BtnHide_Function(self):
        self.m_pDetailWidget.close()
        self.groupBox.hide()

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

    def Slot_Txt(self, Str):
        self.Lne_QR.insert(Str)

    def KeyBoard_Slot(self):
        self.Btn_Keyboard.clicked.connect(self.KeyBoard_Show)
        self.Btn_Switch.clicked.connect(self.BtnSwitch_Function)
        self.Btn_Backspace.clicked.connect(self.BtnBackspace_Function)
        self.Btn_Enter.clicked.connect(self.BtnEnter_Function)
        self.Btn_Hide.clicked.connect(self.BtnHide_Function)
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
        self.Btn_Point.clicked.connect(self.BtnPoint_Function)
        self.Btn_Hyphen.clicked.connect(self.BtnHyphen_Function)

    def Login_Slot(self):
        self.close()
        Login = Login_UI.Login_UI()
        Login.show()
        self.windowList.append(Login)

    def Warning(self, Str):
        self.Grp_Warning.show()
        self.Lbl_Warning.setText(Str)

    def Warning_Slot(self):
        self.Grp_Warning.hide()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainUI()
#     window.show()
#     sys.exit(app.exec_())
