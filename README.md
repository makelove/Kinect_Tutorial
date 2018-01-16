# Kinect Tutorial in Python3  教程2018


- 开发环境
    - macOS
    - python 3.6
    - libfreenect
        - API:https://openkinect.github.io/libfreenect2/index.html
    - OpenCV 3.3
    - Kinect v1
    - 安装
        - Tutorial/在virtualenv安装freenect库-python3.md
- 参考图书：
    - [Kinect Hacks
by Jared St. Jean](https://www.safaribooksonline.com/library/view/kinect-hacks/9781449332181/)
    - [Hacking the Xbox Kinect](https://item.jd.com/19393582.html)    
        - 使用libfreenect
    - Raspberry-Kinect-Opencv https://github.com/Snigf12/Python-Raspberry-Kinect-Opencv---Artificial-Vision-System
    - ROS [Kinect-ASUS-Xtion-Pro-Live-Calibration-Tutorials](https://github.com/taochenshh/Kinect-ASUS-Xtion-Pro-Live-Calibration-Tutorials)

- 校准
    - https://openkinect.org/wiki/Calibration
    - 好 [Kinect校准教程](http://rgbdemo.org/index.php/Documentation/TutorialProjectorKinectCalibration)
    
    
- fakenect hands freenect-cppview    

- Skeleton Tracking骨骼追踪
    - https://github.com/joaquimrocha/Skeltrack
    - Be sure to install GFreenect before Skeltrack https://github.com/elima/GFreenect
    - Once Skeltrack is compiled run the kinect binary in the examples folder
    
- libfreenect multiple kinects同时连接多个Kinect
    - 代码参考 
        - https://github.com/shiffman/OpenKinect-for-Processing/blob/8820b4e18d43d806df2409216d6505c0fe6da90f/OpenKinect-Processing/examples/Kinect_v1/MultiKinect/MultiKinect.pde
    - https://github.com/OpenKinect/libfreenect/issues/522
    - >It is somewhat hard to tell about your PCIe bandwidth带宽不够. It is part of the motherboard configuration and it depends on the USB controller link too. You can try out different machines though, or you can use multiple machines and connect them through ROS.
    - 需要一台配备强大GPU的高端个人电脑，每个Kinect需要一个USB3控制器，每个控制器都有自己的PCI-Express x8或x16连接。
    - [亚马孙 4 Port PCI Express (PCIe) SuperSpeed USB 3.0 Card Adapter](https://www.amazon.com/Express-SuperSpeed-Adapter-Dedicated-Channels/dp/B00HJZEA2S/ref=sr_1_2?ie=UTF8&qid=1473310532&sr=8-2&keywords=startech+PCIe+usb3)
    - https://forum.openframeworks.cc/t/multiple-kinect-setup-for-real-time-volumetric-reconstruction-and-tracking-of-people/15271
    
    
```python
while(1):    
    img = get_depth()
    freenect.stop_depth(device1)
    # display the img
    # proceed without delay
    freenect.start_depth(device1)
```    