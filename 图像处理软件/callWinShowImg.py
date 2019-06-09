import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from WinShowImg import Ui_MainWindow
import sys

class Win(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        self.readBtn.clicked.connect(self.openImg)
        self.processBtn1.clicked.connect(self.blurImg)
        self.processBtn2.clicked.connect(self.edgeDistinct)
        self.processBtn3.clicked.connect(self.cornerDistinct)
        self.processBtn4.clicked.connect(self.meanImg)
        self.saveBtn.clicked.connect(self.saveImg)
        self.clearBtn.clicked.connect(self.clearImg)
        self.quiteBtn.clicked.connect(self.quiteImg)
        self.img1 = np.ndarray(())
        self.img2 = np.ndarray(())
        self.temp = np.ndarray(())

    def openImg(self):
        # # 调用打开文件diglog
        fileName, tmp = QFileDialog.getOpenFileName(self, 'Open Image', './data', '*.png *.jpg *.bmp')

        if fileName is '':
            return

        self.img1 = cv2.imread(fileName)

        height, width, channel = self.img1.shape
        bytesPerLine = 3*width
        self.qImg = QImage(self.img1.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        # 图形缩放
        self.qImg = self.qImg.scaled(self.label_2.width(), self.label_2.height(),
                                     Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # 将Qimage展示出来
        self.label_2.setPixmap(QPixmap.fromImage(self.qImg))

    def blurImg(self):
        '''
        图像模糊
        :return:
        '''
        if self.img1.size == 1:
            return

        # 对图像进行模糊处理，窗口设定为5*5
        self.img2 = cv2.blur(self.img1, (5, 5))

        height, width, channel = self.img2.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img2.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        # 将Qimage展示出来

        # 图形缩放
        self.qImg = self.qImg.scaled(self.label_3.width(), self.label_3.height(),
                                     Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        self.label_3.setPixmap(QPixmap.fromImage(self.qImg))


    def edgeDistinct(self):
        '''
        边缘检测
        :return:
        '''
        if self.img1.size == 1:
            return

        self.temp = cv2.cvtColor(self.img1, cv2.IMREAD_GRAYSCALE)

        self.temp = cv2.Canny(self.temp, 200, 300)

        self.img2 = cv2.cvtColor(self.temp, cv2.COLOR_GRAY2BGR)
        height, width, channel = self.img2.shape
        bytesPerLine = 3 * width     # 每一行的比特数，8位三通道的就是宽度*3
        self.qImg = QImage(self.img2.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        self.qImg = self.qImg.scaled(self.label_2.width(), self.label_2.height(),
                                     Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 将Qimage展示出来
        self.label_3.setPixmap(QPixmap.fromImage(self.qImg))

    def cornerDistinct(self):
        '''
        转换为灰度图
        :return:
        '''

        if self.img1.size == 1:
            return

        self.temp = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY)

        self.img2 = cv2.cvtColor(self.temp, cv2.COLOR_GRAY2BGR)

        height, width, channel = self.img2.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img2.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.qImg = self.qImg.scaled(self.label_2.width(), self.label_2.height(),
                                     Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 将Qimage展示出来
        self.label_3.setPixmap(QPixmap.fromImage(self.qImg))

    def meanImg(self):
        '''
        图像均衡化
        :return:
        '''
        if self.img1.size == 1:
            return

        img_yuv = cv2.cvtColor(self.img1, cv2.COLOR_BGR2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])  # 均衡y通道

        # 将其转化为BGR
        self.img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        height, width, channel = self.img2.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img2.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        self.qImg = self.qImg.scaled(self.label_2.width(), self.label_2.height(),
                                     Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 将Qimage展示出来
        self.label_3.setPixmap(QPixmap.fromImage(self.qImg))

    def saveImg(self):
        # 调用存储文件dialog
        filename, tmp = QFileDialog.getSaveFileName(self, 'Open Image', './data', '*.png*.jpg*.bmp')
        if filename is '':
            return
        if self.img2.size == 1:
            return

        # 调用opencv写入图像
        cv2.imwrite(filename, self.img2)

    def clearImg(self):

        self.label_2.clear()
        self.label_3.clear()

    def quiteImg(self):

        qApp = QApplication.instance()
        qApp.quit()  # 我们关闭窗口调用的是QApplication()的方法

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./data/background.jpg);}")
    win.show()
    sys.exit(app.exec_())



