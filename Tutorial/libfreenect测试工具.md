## libfreenect测试工具
- 按ESC退出

- freenect-camtest
- freenect-chunkview 深度
- freenect-cpp_pcview
    - 好，有用。带坐标系
    - 放大
- freenect-cppview  同时在2个窗口显示 RGB和depth图像   
- freenect-hiview 高清？
- freenect-micview 多个相机？
    - Number of devices found: 1

- freenect-regtest
- freenect-regview 彩色 ？
- freenect-tiltdemo 向上或向下
```bash
led[2] tilt[14] accel[0.155661,10.584956,-0.167635]
led[1] tilt[11] accel[0.407114,10.249685,2.658213]
led[3] tilt[5] accel[0.263426,10.393373,1.987673]
led[2] tilt[-6] accel[0.263426,10.584956,1.125550]
led[5] tilt[0] accel[0.359218,10.584956,-0.981862]
```


- freenect-glview
    - 'w' - tilt up, 's' - level, 'x' - tilt down
    - '0'-'6' - select LED mode, 
    - '+' & '-' - change IR intensity强度
    - 'f' - change video format, 'm' - mirror video, 'o' - rotate video with accelerometer
    - 'e' - auto exposure, 'b' - white balance, 'r' - raw color, 
    - 'n' - near mode (K4W only)

- freenect-glpclview
    - 3D
    - 合并 RGB和depth图像

```bash
freenect-glview
#
Kinect camera test
Number of devices found: 1
Found sibling device [single on same bus]
GL thread
[Stream 70] Negotiated packet size 1920
write_register: 0x0105 <= 0x00
write_register: 0x0006 <= 0x00
write_register: 0x0012 <= 0x03
write_register: 0x0013 <= 0x01
write_register: 0x0014 <= 0x1e
write_register: 0x0006 <= 0x02
write_register: 0x0017 <= 0x00
[Stream 80] Negotiated packet size 1920
write_register: 0x000c <= 0x00
write_register: 0x000d <= 0x01
write_register: 0x000e <= 0x1e
write_register: 0x0005 <= 0x01
[Stream 70] Lost 159 total packets in 0 frames (inf lppf)
[Stream 70] Lost 171 total packets in 0 frames (inf lppf)
write_register: 0x0047 <= 0x00
'w' - tilt up, 's' - level, 'x' - tilt down, '0'-'6' - select LED mode, '+' & '-' - change IR intensity
'f' - change video format, 'm' - mirror video, 'o' - rotate video with accelerometer
'e' - auto exposure, 'b' - white balance, 'r' - raw color, 'n' - near mode (K4W only)
```

- freenect-wavrecord
```bash
Number of devices found: 1
Found sibling device [single on same bus]
Uploading firmware to audio device in bootloader state.
Trying to open ./audios.bin as firmware...
Trying to open /Users/play/.libfreenect/audios.bin as firmware...
Trying to open /usr/local/share/libfreenect/audios.bin as firmware...
Trying to open /usr/share/libfreenect/audios.bin as firmware...
Trying to open ./../Resources/audios.bin as firmware...
upload_firmware: failed to find firmware file.
upload_firmware failed: -2
Could not open device
```

- fakenect
```bash
Usage: /usr/local/bin/fakenect <database> <application> <args>
```

- fakenect-record
```bash
Records the Kinect sensor data to a directory
Result can be used as input to Fakenect
Usage:
  record [-h] [-ffmpeg] [-ffmpeg-opts <options>] <target basename>

#会产生2个视频文件,没有音频
fakenect-record -ffmpeg test_record
#
ffmpeg -pix_fmt rgb24 -s 640x480 -f rawvideo -i /dev/stdin -aspect 4:3 -r 20 -vcodec msmpeg4 -b 30000k test_record-depth.avi
ffmpeg -pix_fmt rgb24 -s 640x480 -f rawvideo -i /dev/stdin -aspect 4:3 -r 20 -vcodec msmpeg4 -b 30000k test_record-rgb.avi

#
test_record-depth.avi
test_record-index.txt
test_record-rgb.avi

#
fakenect-record test_record2
#产生一大堆文件，包括depth的dump文件和RGB的ppm图像文件
```