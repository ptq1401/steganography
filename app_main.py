from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import app_home
import app_decode
import app_encode

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def mainUi():
    global ui
    ui = app_home.Ui_Home()
    ui.setupUi(MainWindow)
    ui.but_decode.clicked.connect(decode_UI)
    ui.but_encode.clicked.connect(encode_UI)
    MainWindow.show()

def decode_UI():
    global ui
    ui = app_decode.Ui_Decoding()
    ui.setupUi(MainWindow)
    ui.pushButton_2.clicked.connect(mainUi)
    MainWindow.show()

def encode_UI():
    global ui
    ui = app_encode.Ui_ENCODING()
    ui.setupUi(MainWindow)
    ui.back.clicked.connect(mainUi)
    MainWindow.show()

mainUi()
MainWindow.setWindowIcon(QtGui.QIcon('Icon.jpg'))
sys.exit(app.exec_())
