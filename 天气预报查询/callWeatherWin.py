import sys
from PyQt5.QtWidgets import *
from WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.clearBtn.clicked.connect(self.clearResult)
        self.ui.queryBtn.clicked.connect(self.queryWeather)
    def queryWeather(self):

        print('* queryWeather')
        cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)
        web = 'http://www.weather.com.cn/data/sk/' + cityCode + '.html'
        rep = requests.get(web)
        rep.encoding = 'utf-8'
        # print(rep.json())

        msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
        msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
        msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + '\n'
        msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n' + '度'
        msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        self.ui.resultText.setText(result)

    def transCityName(self, cityName):
        cityCode = ''

        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'
        elif cityName == '西安':
            cityCode = '101110101'

        return cityCode

    def clearResult(self):
        print('* clearResult')
        self.ui.resultText.clear()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./images/python.jpg);}")
    win.show()
    sys.exit(app.exec_())

