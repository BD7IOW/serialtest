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
        port_list = list( serial.tools.list_ports.comports() )
        if len( port_list ) <= 0:
           print("The Serial port can't find!")
           # QMessageBox.information(
            #    self,
             #   "Warnning!",
              #  "The Serial port can't find!",
               # QMessageBox.Yes
            #)

        else:
            port_list_0 = list( port_list[0] )

            port_serial = port_list_0[0]

            ser = serial.Serial( port_serial, 9600, timeout=60 )
            comname =list(ser.name)
            liststr = "".join(comname)
            print(liststr)
            self.conN.addItem(liststr)#cant not use additems(list-of-str)
            #self.conN.addItem("COMX")
            print("check which port was really used >", ser.name)
        BAUDRATES = ["9600", "4800", "115200"]
        self.conB.addItems(BAUDRATES)
        self.textEdit.setText("欢迎使用")
        self.clearRx.clicked.connect(self.textEdit.clear)
        self.clearTx.clicked.connect(self.textEdit_2.clear)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindows()
    ui.show()
    sys.exit(app.exec_())