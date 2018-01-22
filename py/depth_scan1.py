# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:30
# @Author  : play4fun
# @File    : depth_scan1.py
# @Software: PyCharm

"""
depth_scan1.py:
产生 扫描状的条纹
"""

import freenect
import cv2
import numpy as np
import pickle


def scan_out(arr):
    depth2 = arr.copy()
    for x in range(depth2.min() + 1, depth2.max(), 2):
        depth2[depth2 == x] = 0
    return depth2


if __name__ == "__main__":
    rgb = 'd'
    print('start')
    while True:
        array, timestamp = freenect.sync_get_depth()
        array >>= 2  # 只需要这个
        # array = scan_out(array)
        depth = array.astype(np.uint8)
        depth = scan_out(depth)

        if rgb != 'd':#降低了速度？
            tmp = depth.copy()
            depth = np.empty([depth.shape[0], depth.shape[1], 3], dtype=np.uint8)
            for i in range(depth.shape[0]):
                for j in range(depth.shape[1]):
                    if rgb == 'b':
                        depth[i, j] = [tmp[i, j], 0, 0]
                    if rgb == 'g':
                        depth[i, j] = [0, tmp[i, j], 0]
                    if rgb == 'r':
                        depth[i, j] = [0, 0, tmp[i, j]]

        cv2.imshow('Depth image', depth)

        k = cv2.waitKey(1)  # & 0xFF
        if k == 27:
            # with open('depth-scan_ndarray-2', 'wb') as f:#保存下来，为了以后在ipython内调试
            #     pickle.dump(array, f)
            break
        try:
            if chr(k) in ['r', 'g', 'b', 'd']:
                rgb = chr(k)
        except:
            pass
    freenect.sync_stop()
