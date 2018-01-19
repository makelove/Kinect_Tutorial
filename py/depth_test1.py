# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 18:52
# @Author  : play4fun
# @File    : depth_test1.py
# @Software: PyCharm

"""
depth_test1.py:
给depth添加颜色
"""

import freenect
import cv2
import numpy as np
import pickle

if __name__ == "__main__":
    print('start')
    while True:
        array, _ = freenect.sync_get_depth()
        depth = array.astype(np.uint8)
        cv2.imshow('Depth image', depth)

        k = cv2.waitKey(5)  # & 0xFF
        if k == 27:
            with open('depth_ndarray-1', 'wb') as f:
                pickle.dump(array, f)
            break
