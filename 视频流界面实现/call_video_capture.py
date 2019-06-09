from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Video_Capture import Ui_MainWindow
import cv2

class Win(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        self.timer_camera = QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0

        # 按钮绑定槽函数
        self.pushButton.clicked.connect(self.open_video)
        self.pushButton_2.clicked.connect(self.close_video)
        self.timer_camera.timeout.connect(self.show_video)
        self.pushButton_3.clicked.connect(self.close)


    def open_video(self):

        # 判断timer有没有被激活
        if self.timer_camera.isActive() == False:
            # 若没有被激活，则将摄像头打开
            flag = self.cap.open(self.CAM_NUM)

            if flag == False:
                # 看一下摄像头是否打开成功 若没有成功个，弹出一个提醒的窗口
                msg = QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QMessageBox.Ok,
                                                    defaultButton=QMessageBox.Ok)

            else:
                self.timer_camera.start(30)  # 每个0.03秒刷新一次


    def close_video(self):

        # 判断timer是否是激活状态，如果是激活状态，则说明视频是开启的，我们只需将摄像头释放掉
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()
            self.label.clear()

    def show_video(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))    # 将读出的视频重置大小
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)   # 将读出的视频编码进行改变，BGR2RGB
        # 将转化后的图片传给Qimage,然后绘制按在label上
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(showImage))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())
