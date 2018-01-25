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
import cv2, sys
import numpy as np
import pickle

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print(''' Error: PyOpenGL not installed properly ''')
    sys.exit()

window = 0  # Number of the glut window.
mx = -1
my = -1  # Prevous mouse coordinates
anglex = 0
angley = 0  # Panning angles
zoom = 1  # Zoom factor
color = True  # Flag to indicate to use of color in the cloud


def printInfo():
    txt = "\nAvailable Controls:" + "===================" + "Rotate       :   Mouse Left Button" + "Zoom         :   Mouse Wheel" + "Toggle Color :   C" + "Quit         :   Q or Esc\n"

    print(txt)


def DrawGLScene():  # 主要功能
    # 深度相机
    depth, timestamp = freenect.sync_get_depth()
    depth >>= 2  # 只需要这个
    # RGB相机
    rgbarray, timestamp2 = freenect.sync_get_video()
    rgb = cv2.cvtColor(rgbarray, cv2.COLOR_RGB2BGR)

    #
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPointSize(1.0)

    glBegin(GL_POINTS)

    #TODO 有错误，不能正常显示 ！！
    col3 = glColor3ub(255, 255, 255)
    # if (!color) glColor3ub(255, 255, 255):
    if not color and col3:
        # for (int i = 0; i < 480 * 640; ++i):
        for i in range(480 * 640):

            if color:
                glColor3ub(rgb[3 * i + 0],  # R
                           rgb[3 * i + 1],  # G
                           rgb[3 * i + 2])  # B

                f = 595.0
                # Convert from image plane  coordinates to world  coordinates

                glVertex3f((i % 640 - (640 - 1) / 2.) * depth[i] / f,  # X = (x - cx) * d / fx
                           (i / 640 - (480 - 1) / 2.) * depth[i] / f,  # Y = (y - cy) * d / fy
                           depth[i])  # Z = d

    glEnd()

    # Draw world coordinate frame
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)  # X - axis
    glVertex3f(0, 0, 0)
    glVertex3f(50, 0, 0)
    glColor3ub(0, 255, 0)  # Y - axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 50, 0)
    glColor3ub(0, 0, 255)  # Z - axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 50)
    glEnd()

    # Place the camera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScalef(zoom, zoom, 1)
    gluLookAt(-7 * anglex, -7 * angley, -1000.0,
              0.0, 0.0, 2000.0,
              0.0, -1.0, 0.0)

    glutSwapBuffers()


def idleGLScene():
    glutPostRedisplay()


def resizeGLScene(width: int, height: int):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, float(width / height), 900.0, 11000.0)

    glMatrixMode(GL_MODELVIEW)


def mouseMoved(x: int, y: int):
    global mx, my, anglex, angley

    if mx >= 0 and my >= 0:
        anglex += x - mx
        angley += y - my

    mx = x
    my = y


def keyPressed(key, x: int, y: int):
    global color
    if key == b'C' or key == b'c':
        color = not color
        # break;

    if key == b'Q' or key == b'q' or key == b'\x1b':  # ESC
        glutDestroyWindow(window)
        # device->stopDepth();
        # device->stopVideo();
        freenect.sync_stop()
        exit(0)


def main():
    # device = & freenect.createDevice < MyFreenectDevice > (0);
    # device->startVideo();
    # device->startDepth();

    # glutInit( & argc, argv);
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)

    global window
    window = glutCreateWindow("freenect-cpp_pcview")
    glClearColor(0.45, 0.45, 0.45, 0.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glAlphaFunc(GL_GREATER, 0.0)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(50.0, 1.0, 900.0, 11000.0)

    glutDisplayFunc(DrawGLScene)  # 最重要是这个函数
    glutIdleFunc(idleGLScene)

    # TODO
    glutReshapeFunc(resizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutMotionFunc(mouseMoved)
    # glutMouseFunc(mouseButtonPressed)

    printInfo()

    glutMainLoop()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
