# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 11:32
# @Author  : play4fun
# @File    : freenect_cv2_demo1.py
# @Software: PyCharm

"""
freenect_cv2_demo1.py:
http://euanfreeman.co.uk/openkinect-python-and-opencv/

简单例子
"""

import freenect
import cv2
import numpy as np

"""
Grabs a depth map from the  sensor and creates an image from it.
"""

kernel = np.ones((5, 5), np.uint8)


def getDepthMap(mindep=2,maxdep=5):
    depth, timestamp = freenect.sync_get_depth()

    np.clip(depth, 0, 2 ** 10 - 1, depth)#修剪？
    depth >>= mindep
    # depth <<= maxdep
    depth = depth.astype(np.uint8)

    return depth


try:
    while True:
        depth4 = getDepthMap(6,10)
        depth2 = getDepthMap(2,5)
        # print('depth', type(depth2))

        blur = cv2.GaussianBlur(depth2, (5, 5), 0)

        cv2.imshow('depth4', depth4)
        # cv2.imshow('depth', depth)
        cv2.imshow('blur', blur)  # OK
        cv2.waitKey(10)
except KeyboardInterrupt:
    freenect.sync_stop()
    # freenect.close_device()
