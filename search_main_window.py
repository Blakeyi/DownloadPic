# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import webbrowser


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 553)
        self.defaultPath = ''
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
        self.cwd = os.getcwd()  # 获取当前程序文件位置
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
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_saveDir = QtWidgets.QAction(MainWindow)
        self.action_saveDir.setObjectName("action_saveDir")
        self.action_openUrl = QtWidgets.QAction(MainWindow)
        self.action_openUrl.setObjectName("action_openUrl")
        self.action_openDir = QtWidgets.QAction(MainWindow)
        self.action_openDir.setObjectName("action_openDir")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setObjectName("actionPreferences")
        self.menuSetting.addAction(self.action_saveDir)
        self.menuSetting.addAction(self.action_Preferences)
        self.menuFile.addAction(self.action_openUrl)
        self.menuFile.addAction(self.action_openDir)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.action_openDir.triggered.connect(self.openfile)
        self.action_openUrl.triggered.connect(self.openWeb)
        self.action_saveDir.triggered.connect(self.select_file)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openfile(self):
        curpath = "start explorer " + self.cwd
        os.system(curpath)

    def openWeb(self):  # 使用默认浏览器打开网址
        url = self.urlEdit.text()
        if url == '':
            self.textShow.setText('打开网址失败，请检查输入')
        else:
            webbrowser.open(url)

    def select_file(self):  # 选择下载的图片文件保存路径
        savePath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cwd)  # 起始路径
        if savePath == '':
            self.textShow.setText("您未选择文件夹")
        else:
            self.defaultPath = savePath

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancle.setText(_translate("MainWindow", "取消下载"))
        self.label.setText(_translate("MainWindow", "网址："))
        self.label_2.setText(_translate("MainWindow", "                        欢迎使用图片下载工具"))
        self.start.setText(_translate("MainWindow", "开始下载"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_saveDir.setText(_translate("MainWindow", "SaveDirectory"))
        self.action_openUrl.setText(_translate("MainWindow", "OpenUrl"))
        self.action_openDir.setText(_translate("MainWindow", "OpenDir"))
        self.action_Preferences.setText(_translate("MainWindow", "Preferences"))
