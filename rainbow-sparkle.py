#! /usr/bin/env python
import sys
from rainbow import *
from sparkle import *
from math import sin, cos, radians
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

def getObjects():
    array = [Rainbow()]
    for i in range(50):
        array.append(Sparkle(float(i*2.0)/10.0 + 5.25, 0.1, -1))
        array.append(Sparkle(-float(i*2.0)/10.0 - 5.25, 0.1, -1))
        array.append(Sparkle(float(i*2.0)/10.0 + 5.25, 0.1, 1))
        array.append(Sparkle(-float(i*2.0)/10.0 - 5.25, 0.1, 1))
    for i in range(20):
        array.append(Sparkle(15.25, 0.1, -1.0 + float(i)/10.0))
        array.append(Sparkle(4.75, 0.1, -1.0 + float(i)/10.0))

        array.append(Sparkle(-15.25, 0.1, -1.0 + float(i)/10.0))
        array.append(Sparkle(-4.75, 0.1, -1.0 + float(i)/10.0))
    return array

class RSGlobals:
    zoom = 25
    xangle = 0
    yangle = 0
    time = 0
    objects = getObjects()
    window_id = 0
    left_held = False
    right_held = False
    up_held = False
    down_held = False

def updateFromKeyboard():
    if RSGlobals.up_held:
        RSGlobals.yangle += 5
    if RSGlobals.down_held:
        RSGlobals.yangle -= 5
    if RSGlobals.left_held:
        RSGlobals.xangle += 5
    if RSGlobals.right_held:
        RSGlobals.xangle -= 5

def display():
    updateFromKeyboard()
    
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    gluLookAt(0, 0, -RSGlobals.zoom, 0, 0, 0, 0, 1, 0)
    glRotatef(RSGlobals.xangle, 0, 1, 0)
    glRotatef(-RSGlobals.yangle, cos(radians(RSGlobals.xangle)), 0, sin(radians(RSGlobals.xangle)))

    time = RSGlobals.time
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 1, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT,  [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    
    for obj in RSGlobals.objects:
        obj.render()
    
    RSGlobals.time = time + 1
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(4, float(width)/float(height), 0.2, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def keyboard(key, x, y):
    if key == b'\x1b' or key == 'q': # ESC or 'q'
        glutDestroyWindow(RSGlobals.window_id)
        sys.exit(0)
    glutPostRedisplay()

def special(key, x, y):
    if key == GLUT_KEY_UP:
        RSGlobals.up_held = True
    elif key == GLUT_KEY_DOWN:
        RSGlobals.down_held = True
    elif key == GLUT_KEY_LEFT:
        RSGlobals.left_held = True
    elif key == GLUT_KEY_RIGHT:
        RSGlobals.right_held = True
    glutPostRedisplay()

def specialUp(key, x, y):
    if key == GLUT_KEY_UP:
        RSGlobals.up_held = False
    elif key == GLUT_KEY_DOWN:
        RSGlobals.down_held = False
    elif key == GLUT_KEY_LEFT:
        RSGlobals.left_held = False
    elif key == GLUT_KEY_RIGHT:
        RSGlobals.right_held = False
    elif key == GLUT_KEY_PAGE_UP:
        RSGlobals.zoom = max(1, RSGlobals.zoom - 1)
    elif key == GLUT_KEY_PAGE_DOWN:
        RSGlobals.zoom = min(25, RSGlobals.zoom + 1)
    glutPostRedisplay()

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 640)
    RSGlobals.window_id = glutCreateWindow(b"Hello, Kate")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutSpecialUpFunc(specialUp)
    glutIdleFunc(display)
    glutMainLoop()

