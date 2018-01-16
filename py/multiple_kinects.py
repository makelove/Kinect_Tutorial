# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 10:55
# @Author  : play4fun
# @File    : multiple_kinects.py
# @Software: PyCharm

"""
multiple_kinects.py:
"""
import freenect

context = freenect.init()
num_devices = freenect.num_devices(context)

device1 = freenect.open_device(context, 0)
device2 = freenect.open_device(context, 1)

print('device1',device1)
print('device2',device2)


while True:
    depth_frames = [freenect.sync_get_depth(i) for i in range(num_devices)]
    video_frames = [freenect.sync_get_video(i) for i in range(num_devices)]

freenect.sync_stop()
# To run it asynchronously, you'll need to open the devices manually and call freenect.runloop() from multiple threads.