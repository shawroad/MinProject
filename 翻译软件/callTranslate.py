from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import sys
from Translate import Ui_MainWindow


class Win(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)

        self.zh2en.clicked.connect(self.zh2enfun)
        self.en2zh.clicked.connect(self.en2zhfun)
        self.clearBtn.clicked.connect(self.clearinfo)

    def zh2enfun(self):
        '''中文翻译为英文'''
        word = self.textEdit1.toPlainText()
        url = 'https://fanyi.baidu.com/transapi'
        data = {
            'from': 'zh',
            'to': 'en',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': '325815.7046',
            'token': '9b1b599bf1303d7d525833a9e17579bb'
        }
        response = requests.post(url, data=data).json()  # 将获取的数据转换为json格式
        info = response['data'][0]['result'][0][1]
        self.textEdit2.setText(info)

    def en2zhfun(self):
        '''英文翻译为中文'''
        word = self.textEdit1.toPlainText()
        url = 'https://fanyi.baidu.com/transapi'
        data = {
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': '325815.7046',
            'token': '9b1b599bf1303d7d525833a9e17579bb'
        }
        response = requests.post(url, data=data).json()  # 将获取的数据转换为json格式
        info = response['data'][0]['result'][0][1]
        self.textEdit2.setText(info)

    def clearinfo(self):
        self.textEdit1.clear()
        self.textEdit2.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./data/background.jpg);}")
    win.show()
    sys.exit(app.exec_())