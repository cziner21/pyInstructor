#coding: utf8
import sys
from Views import loadingView
from PyQt4.QtGui import *
from PySide.QtCore import *

class Loading(QMainWindow,loadingView.Ui_MainWindow):
    def __init__(self,parent=None):

        super(Loading,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Loading()
    form.show()
    app.exec_()
