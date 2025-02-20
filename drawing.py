# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : drawing.py
# Time       ：2021/4/12 13:49
# Author     ：yujia
# Description：
"""
"""
@author: jiajia
@file: drawing.py
@time: 2021/3/28 15:31
"""
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import PIL
from io import BytesIO
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
number = 0

def open_image(file):
    if isinstance(file, np.ndarray):
        img = Image.fromarray(file)
    elif isinstance(file, bytes):
        img = Image.open(BytesIO(file))
    else:
        img = Image.open(file)
    img = img.convert('RGB')
    img = np.array(img)
    return img


def draw(img_path, data=None, name=None):
    "绘制识别结果"
    image_ = open_image(img_path)

    plt.imshow(image_, interpolation='none')
    if data:
        current_axis = plt.gca()
        for box_ in data:
            box = box_['crop']
            x1, y1, x2, y2 = box
            box_w = x2 - x1
            box_h = y2 - y1

            current_axis.add_patch(
                plt.Rectangle((x1, y1), box_w, box_h, color='blue', fill=False, linewidth=2))
            plt.text(
                x1,
                y1,
                s='',
                color="white",
                verticalalignment="top",
                bbox={"color": "black", "pad": 0},
            )
    # print(111)
    plt.axis('off')
    # global number
    if name:
        plt.savefig(f"{os.path.dirname(__file__)}/save_img/{name}.jpg")
    # # plt.savefig(r"C:\CodeFiles\2021\OcrCard\imgs\draw_img2/" + os.path.basename(img_path))
    # number = number + 1
    # plt.clf()
    plt.show()




if __name__ == '__main__':
    data = [{'crop': [72, 86, 285, 124], 'text': '姓名糜泽毅'}, {'crop': [72, 151, 366, 185], 'text': '性别男民族汉'}, {'crop': [74, 212, 434, 245], 'text': '出生1976年9月30日'}, {'crop': [73, 279, 508, 309], 'text': '住址 南京市玄武区富贵山3号3'}, {'crop': [175, 323, 287, 350], 'text': '幢308室'}, {'crop': [77, 429, 723, 469], 'text': '公民身份号码320114197609301517'}]
    draw("1234.jpg", data)