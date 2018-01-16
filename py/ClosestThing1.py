# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 23:02
# @Author  : play4fun
# @File    : ClosestThing1.py
# @Software: PyCharm

"""
ClosestThing1.py:
"""

# import the necessary modules
import freenect
import cv2
import numpy as np

minThresh = 500
# maxThresh = 830
maxThresh = 700


# function to get RGB image from kinect
def get_video() -> np.ndarray:
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth() -> np.ndarray:
    array, _ = freenect.sync_get_depth()
    # array=np.clip(array,minThresh,maxThresh)

    # array = array.astype(np.uint8)
    return array
    # return a2


if __name__ == "__main__":
    print('start')
    try:
        while True:
            # get a frame from RGB camera
            frame = get_video()
            # print('frame', type(frame),frame.shape)#<class 'numpy.ndarray'> (480, 640, 3)
            # get a frame from depth sensor
            depth = get_depth()
            frame[depth < minThresh] = (255, 255, 255)  # (0, 0, 0)
            frame[depth > maxThresh] = (0, 0, 0)  # (255, 255, 255)
            # print('depth', type(depth), depth.shape)#<class 'numpy.ndarray'> (480, 640)
            # display RGB image
            cv2.imshow('RGB image', frame)
            # display depth image
            cv2.imshow('Depth image', depth.astype(np.uint8))

            # quit program when 'esc' key is pressed
            k = cv2.waitKey(5)  # & 0xFF
            if k == 27:
                break
            if k == ord('s'):  # 保存图片
                cv2.imwrite('ClosestThing1.png', frame)
    except Exception as e:
        print(e)
