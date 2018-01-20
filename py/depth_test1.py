# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 18:52
# @Author  : play4fun
# @File    : depth_test1.py
# @Software: PyCharm

"""
depth_test1.py:
给depth添加颜色

深色，黑色，数值小0越近，
浅色，白色，数值大255越远
"""

import freenect
import cv2
import numpy as np
import pickle

if __name__ == "__main__":
    print('start')
    while True:
        array, timestamp = freenect.sync_get_depth()
        # cv2.imshow('array', array)
        # np.clip(array, a_min=0, a_max=2 ** 10 - 1, out=array)  # 修剪？
        array >>= 2#只需要这个
        depth = array.astype(np.uint8)
        cv2.imshow('Depth image', depth)

        # color_img = cv2.cvtColor(depth,cv2.COLOR_GRAY2RGB)#没用
        # cv2.imshow('color_img', color_img)

        k = cv2.waitKey(50)  # & 0xFF
        if k == 27:
            # with open('depth_ndarray-1', 'wb') as f:#保存下来，为了以后在ipython内调试
            #     pickle.dump(array, f)
            break
    freenect.sync_stop()
