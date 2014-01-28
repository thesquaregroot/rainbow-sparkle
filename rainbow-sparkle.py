#! /usr/bin/env python
import sys
from sparkle import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

screen_width=640
screen_height=480

sparkles = [Sparkle()]

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, screen_width, 0, screen_height, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    for sparkle in sparkles:
        sparkle.render(screen_width/2, screen_height/2, 0)
    
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(screen_width, screen_height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Hello, Kate")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

