# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WinShowImg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 321, 261))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 150, 321, 261))
        self.label_3.setObjectName("label_3")
        self.readBtn = QtWidgets.QPushButton(self.centralwidget)
        self.readBtn.setGeometry(QtCore.QRect(170, 480, 73, 23))
        self.readBtn.setObjectName("readBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(540, 480, 73, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.quiteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quiteBtn.setGeometry(QtCore.QRect(640, 480, 73, 23))
        self.quiteBtn.setObjectName("quiteBtn")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(430, 480, 73, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 420, 141, 141))
        self.groupBox.setObjectName("groupBox")
        self.processBtn1 = QtWidgets.QPushButton(self.groupBox)
        self.processBtn1.setGeometry(QtCore.QRect(30, 20, 73, 23))
        self.processBtn1.setObjectName("processBtn1")
        self.processBtn2 = QtWidgets.QPushButton(self.groupBox)
        self.processBtn2.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.processBtn2.setObjectName("processBtn2")
        self.processBtn3 = QtWidgets.QPushButton(self.groupBox)
        self.processBtn3.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.processBtn3.setObjectName("processBtn3")
        self.processBtn4 = QtWidgets.QPushButton(self.groupBox)
        self.processBtn4.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.processBtn4.setObjectName("processBtn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "图片处理软件"))
        self.label_2.setText(_translate("MainWindow", "待处理的图像"))
        self.label_3.setText(_translate("MainWindow", "处理过后的图像"))
        self.readBtn.setText(_translate("MainWindow", "读取图片"))
        self.clearBtn.setText(_translate("MainWindow", "清空显示"))
        self.quiteBtn.setText(_translate("MainWindow", "退出程序"))
        self.saveBtn.setText(_translate("MainWindow", "保存结果"))
        self.groupBox.setTitle(_translate("MainWindow", "图像处理"))
        self.processBtn1.setText(_translate("MainWindow", "图像模糊"))
        self.processBtn2.setText(_translate("MainWindow", "边缘检测"))
        self.processBtn3.setText(_translate("MainWindow", "灰度化"))
        self.processBtn4.setText(_translate("MainWindow", "均衡化"))

