# -*-coding:UTF-8 -*-
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')  # 将matplotlib绑定在pyqt5上

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QFileDialog
import sys
import matplotlib.pyplot as plt


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


import pylab as pl
pl.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体



class ShowWindow(QWidget):
    def __init__(self):
        super(ShowWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建控件对象
        self.inputLabel = QLabel("请输入文件路径:")
        self.editLine = QLineEdit()
        self.selectButton = QPushButton("...")

        self.selectButton.clicked.connect(self.selectFile)

        inputLayout = QHBoxLayout()  # 水平
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)
        inputLayout.addWidget(self.selectButton)

        # a figure instance to plot on
        self.figure = plt.figure()
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # 以上两句是建立一张画布。。将matplotlib所画的图显示到上面来


        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.button = QPushButton('画折线图')
        self.button.clicked.connect(self.plotText)
        self.button1 =  QPushButton('画散点图')
        self.button1.clicked.connect(self.scatterText)

        plotLayout = QVBoxLayout()  # 垂直
        plotLayout.addWidget(self.canvas)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.button)
        buttonLayout.addWidget(self.button1)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(plotLayout)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.show()

    # 选择图形数据文件存放地址
    def selectFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        self.editLine.setText(fileName1)

    # 画图
    def plotText(self):
        X = []
        Y = []
        input_file = self.editLine.text()
        # input_file = r'E:\pyqt\1.txt'
        with open(input_file, 'r') as f:
            for line in f.readlines():
                data = line[:-1].split(',')  # 不含最后一个换行符
                X.append(data[0])
                Y.append(data[1])

        Ax = self.figure.add_subplot(111)  # Create a `axes' instance in the figure
        Ax.clear()
        Ax.set_ylabel('X轴')
        Ax.set_xlabel('Y轴')
        Ax.plot(X, Y)
        self.canvas.draw()  # 更新画布

    def scatterText(self):

        X = []
        Y = []
        input_file = self.editLine.text()
        # input_file = r'E:\pyqt\1.txt'
        with open(input_file, 'r') as f:
            for line in f.readlines():
                data = line[:-1].split(',')  # 不含最后一个换行符
                X.append(data[0])
                Y.append(data[1])

        Ax = self.figure.add_subplot(111)  # Create a `axes' instance in the figure
        Ax.clear()
        Ax.set_ylabel('角度')
        Ax.set_xlabel('时间')
        # Ax.plot(X, Y)
        Ax.scatter(X, Y)
        self.canvas.draw()  # 更新画布


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())