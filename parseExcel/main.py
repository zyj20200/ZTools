# -*- coding: utf-8 -*-
"""
@author: zyj
@time: 2023/1/5 15:52
"""

import sys
from parseExcel2 import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListView
from utils import parseExcel2json

class UI(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)
        self.pushButton_selectFile.clicked.connect(self.selectFile)
        self.pushButton_transform.clicked.connect(self.transform)

    def selectFile(self):
        self.excelPath, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Excel Files (*.xlsx *.xls *.csv)")
        print(self.excelPath)
        if self.excelPath:
            self.textBrowser.setText(self.excelPath)

    def transform(self):
        if self.excelPath:
            #self.textBrowser.clear()
            self.textBrowser.setText(parseExcel2json(self.excelPath))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
