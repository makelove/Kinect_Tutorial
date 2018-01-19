## Kinect_Processing，很简单！

- https://github.com/shiffman/OpenKinect-for-Processing
    - 代码example：https://github.com/shiffman/OpenKinect-for-Processing/tree/master/OpenKinect-Processing/examples
- 很好的介绍[Getting Started with Kinect and Processing](http://shiffman.net/p5/kinect/)
- 视频教程
    - Youtube [12: Kinect and Processing Tutorial](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZMlWHdcy8hAGDy6IaoxUKf)
    - 讲得很棒。开发语言是Processing
    - 代码
        - https://github.com/CodingTrain/Rainbow-Code/tree/26a50f8177f79a10bc73f588d44e3dd82b37ad7a/Tutorials/Processing/12_kinect
        - svn export  https://github.com/CodingTrain/Rainbow-Code/trunk/Tutorials/Processing/12_kinect
    
- 安装步骤
    - 下载processing https://processing.org/download/
    - 【速写本】-->【添加库文件】-->搜索 open Kinect for processing
    - 便可以使用
    
- 可能需要使用处理kinect库的所有有用的函数：
    - initDevice() - 开始一切（视频，深度，红外）
    - activateDevice(int) - 连接多个设备时激活特定的设备
    - initVideo() - 仅开始视频
    - enableIR(boolean) - 打开或关闭红外摄像机图像（仅限v1）
    - initDepth() - 只开始深度
    - enableColorDepth(boolean) - 打开或关闭深度值作为彩色图像
    - enableMirror(boolean) - 镜像图像和深度数据（仅限v1）
    - PImage getVideoImage() - 抓取RGB（或v1）视频图像
    - PImage getIrImage() - 抓取红外图像（仅限v2）
    - PImage getDepthImage() - 抓取深度图图像
    - PImage getRegisteredImage() - 抓取注册的深度图像（仅限v2）
    - int[] getRawDepth() - 抓取原始深度数据
    - float getTilt() - 获取当前传感器角度（0到30度之间）（仅限v1）
    - setTilt(float) - 调整传感器角度（0到30度之间）（仅限v1）    