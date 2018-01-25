# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 22:21
# @Author  : play4fun
# @File    : freenect-cpp_pcview1.py
# @Software: PyCharm

"""
freenect-cpp_pcview1.py:
freenect-cpp_pcview 用python实现
参考源代码：https://github.com/OpenKinect/libfreenect/blob/master/wrappers/cpp/cpp_pc_view.cpp
"""
import freenect
import cv2
import numpy as np
import pickle
from OpenGL.GL import *
from OpenGL.GLU import *


def printInfo():
    txt = "\nAvailable Controls:" + "===================" + "Rotate       :   Mouse Left Button" + "Zoom         :   Mouse Wheel" + "Toggle Color :   C" + "Quit         :   Q or Esc\n"

    print(txt)


def DrawGLScene():#主要功能
    array, timestamp = freenect.sync_get_depth()
    array >>= 2  # 只需要这个

    rgbarray, timestamp2 = freenect.sync_get_video()
    rgb = cv2.cvtColor(rgbarray, cv2.COLOR_RGB2BGR)

    pass


def main():
    # device = & freenect.createDevice < MyFreenectDevice > (0);
    # device->startVideo();
    # device->startDepth();

    glutInit( & argc, argv);

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(0, 0);

    window = glutCreateWindow("LibFreenect");
    glClearColor(0.45
    f, 0.45
    f, 0.45
    f, 0.0
    f);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_ALPHA_TEST);
    glAlphaFunc(GL_GREATER, 0.0
    f);

    glMatrixMode(GL_PROJECTION);
    gluPerspective(50.0, 1.0, 900.0, 11000.0);

    glutDisplayFunc(DrawGLScene)  # 最重要是这个函数
    glutIdleFunc( & idleGLScene);
    glutReshapeFunc( & resizeGLScene);
    glutKeyboardFunc( & keyPressed);
    glutMotionFunc( & mouseMoved);
    glutMouseFunc( & mouseButtonPressed);

    printInfo()

    glutMainLoop();


if __name__ == '__main__':
    main()
