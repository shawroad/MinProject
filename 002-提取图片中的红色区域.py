"""

@file   : 002-提取图片中的红色区域.py

@author : xiaolu

@time1  : 2019-06-09

"""

import cv2
import numpy as np


def train(addr):
    # 1.读取图片
    img = cv2.imread(addr)  # 载入图片
    # 2.给定红色的HSV范围
    lowerb = np.array([140, 43, 46])
    upperb = np.array([180, 255, 255])  # 取红色的HSV范围

    # 根据hsv阈值 进行二值化
    back_mask = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), lowerb, upperb)

    # cv2.imwrite('number_back_mask_by_hsv_threshold.png', back_mask)
    cv2.imshow('number_back_mask_by_hsv_threshold.png', back_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 形态学操作， 圆形核腐蚀
    kernel = np.ones((2, 2), np.uint8)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    back_mask = cv2.dilate(back_mask, kernel, iterations=4)  # 膨胀运算
    back_mask = cv2.erode(back_mask, kernel, iterations=2)  # 腐蚀操作

    # 反色 变为数字的掩模
    # num_mask = cv2.bitwise_not(back_mask)
    # 中值滤波
    num_mask = cv2.medianBlur(back_mask, 1)
    # cv2.imwrite('number_mask_filter_by_median.png', num_mask)
    # cv2.imshow('number_mask_filter_by_median.png', num_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 寻找轮廓
    # findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
    # cv2.CV_RETR_EXTERNAL 只检测最外围轮廓
    # cv2.CHAIN_APPROX_SIMPLE仅保存轮廓的拐点信息
    contours, hier = cv2.findContours(num_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 声明画布 拷贝自img
    canvas = cv2.cvtColor(num_mask, cv2.COLOR_GRAY2BGR)
    minWidth = 4  # 最小宽度
    minHeight = 20  # 最小高度

    base = 0  # 计数编号
    imgIdx = base  # 当前图片的编号

    # 检索满足条件的区域
    for cidx, cnt in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(cnt)
        if w < minWidth or h < minHeight or w * h < 80 or w * h > 8000 or w > 80 or h > 150:
            # 如果不满足条件就过滤掉  不能超出图片本身的大小
            continue
        # 获取ROI图片   # 感兴趣的区域
        digit = num_mask[y:y + h, x:(x + w)]
        digit = getStandardDigit(digit)

        cv2.imwrite(str(imgIdx) + ".png".format(imgIdx), digit)
        imgIdx += 1
        # 原图绘制矩形
        cv2.rectangle(canvas, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)

    cv2.imwrite("./reult.png", canvas)
    cv2.imshow('result.png', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getStandardDigit(img):
    # 将乱起八噪的图片整成标准大小
    STD_WIDTH = 50  # 标准宽度
    STD_HEIGHT = 50

    height, width = img.shape

    # 判断是否存在长条的1
    new_width = int(width * STD_HEIGHT / height)
    if new_width > STD_WIDTH:
        new_width = STD_WIDTH
    # 以高度为准进行缩放
    resized_num = cv2.resize(img, (new_width, STD_HEIGHT), interpolation=cv2.INTER_NEAREST)
    # 新建画布
    canvas = np.zeros((STD_HEIGHT, STD_WIDTH))
    x = int((STD_WIDTH - new_width) / 2)
    canvas[:, x:x + new_width] = resized_num
    return canvas


if __name__ == '__main__':
    addr = "./data/picture.jpg"
    train(addr)
