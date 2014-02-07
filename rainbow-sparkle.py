#! /usr/bin/env python
import sys
from rainbow import *
from sparkle import *
from math import sin, cos, radians
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def getSparkles():
    return [Sparkle(), Rainbow()]

class RSGlobals:
    zoom = 25
    angle = 0
    time = 0
    sparkles = getSparkles()

def display():
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    time = RSGlobals.time
    light_angle = time*15

    glPushMatrix()
    glLightfv(GL_LIGHT0, GL_POSITION, [cos(radians(light_angle)), 0, sin(radians(light_angle)), 0])
    glPopMatrix()
    
    gluLookAt(0, 0, -RSGlobals.zoom, 0, 0, 0, 0, 1, 0)
    glRotatef(-RSGlobals.angle, 0, 1, 0)
    
    for sparkle in RSGlobals.sparkles:
        sparkle.render()
    
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
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)

def keyboard(key, x, y):
    if (key == GLUT_KEY_UP):
        RSGlobals.zoom = max(RSGlobals.zoom-1, 1)
    elif (key == GLUT_KEY_DOWN):
        RSGlobals.zoom = min(RSGlobals.zoom+1, 50)
    elif (key == GLUT_KEY_LEFT):
        RSGlobals.angle += 5
    elif (key == GLUT_KEY_RIGHT):
        RSGlobals.angle -= 5

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 640)
    glutCreateWindow(b"Hello, Kate")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard)
    glutIdleFunc(display)
    glutMainLoop()

