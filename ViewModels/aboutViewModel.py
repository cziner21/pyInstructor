#coding: utf8
from Views import aboutView
from PyQt4.QtGui import *

class About(QMainWindow,aboutView.Ui_AboutWindow):
    def __init__(self,parent=None):
        super(About,self).__init__(parent)
        self.setupUi(self)