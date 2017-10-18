from PyQt5 import QtCore, QtGui, QtWidgets
from base import Ui_MainWindow
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox



class mywindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindows,self).__init__()
        self.setupUi(self)
        self.radioButton_4.setChecked(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText("a693930096@gmail.com")
        self.RxCount.setReadOnly(True)
        self.RxCount.setText("0")
        self.TxCount.setReadOnly(True)
        self.TxCount.setText("0")
        self.pushButton.setDisabled(True)

        BAUDRATES = ["9600", "4800", "115200"]
        self.conN.addItems(self.Port_List())
        self.conB.addItems(BAUDRATES)
        self.textEdit.setText("欢迎使用")
        self.clearRx.clicked.connect(self.textEdit.clear)
        self.clearTx.clicked.connect(self.textEdit_2.clear)
        self.Openserialbtn.clicked.connect(self.openserial)
        self.pushButton.clicked.connect( self.sendSerialdata )
        self.pushButton_2.clicked.connect( self.closeSerial )
        # 获取COM号列表
    def Port_List(self):
            Com_List = []
            port_list = list( serial.tools.list_ports.comports() )
            for port in port_list:
                Com_List.append( port[0] )
            return Com_List

    def openserial(self):
        # 打开串口
           ser = serial.Serial()
           ser.port = self.conN.currentText()
           ser.baudrate = self.conB.currentText()
           ser.bytesize = serial.EIGHTBITS#int( self.SerialDataComboBox.currentText() )
           ser.parity = serial.PARITY_NONE#ParityValue[0]
           ser.stopbits = serial.STOPBITS_ONE#int( self.SerialStopBitsComboBox.currentText() )
           ser.open()
           print(ser.isOpen())
           if ser.isOpen() is True:
            self.lineEdit.setText("port open successfullly!!")
            self.pushButton.setDisabled( False )

    def closeSerial(self):
        print("close")
        #ser.close()
        self.pushButton.setDisabled( True )
        self.lineEdit.clear()
    def sendSerialdata(self):
        print("send")



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindows()
    ui.show()
    sys.exit(app.exec_())