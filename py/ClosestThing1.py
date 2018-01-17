# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 23:02
# @Author  : play4fun
# @File    : ClosestThing1.py
# @Software: PyCharm

"""
ClosestThing1.py:
跳绳
"""

# import the necessary modules
import freenect
import cv2
import numpy as np
import pickle

# minThresh = 500
# minThresh = 600
minThresh = 600
# maxThresh = 700
# maxThresh = 800
maxThresh = 850


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
    pos_li=[]#保存坐标
    try:
        while True:
            # get a frame from RGB camera
            frame = get_video()
            # print('frame', type(frame),frame.shape)#<class 'numpy.ndarray'> (480, 640, 3)
            # get a frame from depth sensor
            depth = get_depth()
            # frame[depth < minThresh] = (255, 255, 255)  # (0, 0, 0)
            mindep = depth < minThresh
            frame[mindep] = (0, 0, 0)  # (255, 0, 0)  #
            # frame[depth > maxThresh] = (0, 0, 0)  # (255, 255, 255)
            maxdep = depth > maxThresh
            frame[maxdep] = (255, 255, 255)  # (0, 0, 255)  #
            # print('depth', type(depth), depth.shape)#<class 'numpy.ndarray'> (480, 640)
            try:  # 在头顶画一个圆
                rs = np.where(np.logical_and(depth >= minThresh, depth <= maxThresh) == True)
                # print(rs)
                l1 = [(x, y) for x, y in zip(rs[0], rs[1])]
                # l2 = sorted(l1, key=lambda d: d[1])
                l3 = sorted(l1)
                # point = rs[0][0], rs[1][0]
                # point = l2[0]
                # print('point:', point)
                # cv2.circle(frame, center=(point[1],point[0]), radius=10, color=(0, 255, 0), thickness=-1)#绿色

                p2 = (l3[0][1], l3[0][0])
                # print('point:', p2)
                print(p2)
                pos_li.append(p2)
                cv2.circle(frame, center=p2, radius=10, color=(255, 0, 0), thickness=-1)  # 蓝色
            except Exception as e:
                print(e)
                pass

            # display RGB image
            cv2.imshow('RGB image', frame)
            # display depth image
            # cv2.imshow('Depth image', depth.astype(np.uint8))

            # quit program when 'esc' key is pressed
            k = cv2.waitKey(5)  # & 0xFF
            if k == 27:
                break
            if k == ord('s'):  # 保存图片
                cv2.imwrite('ClosestThing1-2.png', frame)
    except Exception as e:
        print(e)
    finally:
        # freenect.close_device()
        # freenect.shutdown()
        # freenect.stop_depth()
        freenect.sync_stop()
        with open('top_pos_list-3','wb') as f:
            pickle.dump(pos_li,f)
