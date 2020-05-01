# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.urlEdit.setFont(font)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout.addWidget(self.urlEdit, 4, 1, 1, 1)
        self.cancle = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.cancle.setFont(font)
        self.cancle.setObjectName("cancle")
        self.gridLayout.addWidget(self.cancle, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.textShow = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.textShow.setFont(font)
        self.textShow.setObjectName("textShow")
        self.gridLayout_2.addWidget(self.textShow, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 23))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsaveDirectory = QtWidgets.QAction(MainWindow)
        self.actionsaveDirectory.setObjectName("actionsaveDirectory")
        self.menuSetting.addAction(self.actionsaveDirectory)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancle.setText(_translate("MainWindow", "取消下载"))
        self.label.setText(_translate("MainWindow", "网址："))
        self.label_2.setText(_translate("MainWindow", "                        欢迎使用图片下载工具"))
        self.start.setText(_translate("MainWindow", "开始下载"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionsaveDirectory.setText(_translate("MainWindow", "saveDirectory"))
