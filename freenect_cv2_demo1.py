# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 11:32
# @Author  : play4fun
# @File    : freenect_cv2_demo1.py
# @Software: PyCharm

"""
freenect_cv2_demo1.py:
简单例子
"""

import freenect
import cv2
import numpy as np

"""
Grabs a depth map from the  sensor and creates an image from it.
"""


def getDepthMap():
    depth, timestamp = freenect.sync_get_depth()

    np.clip(depth, 0, 2 ** 10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)

    return depth


while True:
    depth = getDepthMap()
    print('depth', type(depth))

    blur = cv2.GaussianBlur(depth, (5, 5), 0)

    # cv2.imshow('depth', depth)
    cv2.imshow('blur', blur)#OK
    cv2.waitKey(10)
