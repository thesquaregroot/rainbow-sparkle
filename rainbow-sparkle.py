#! /usr/bin/env python2
import sys
import random
import pygame
from rainbow import *
from sparkle import *
from nyan import *
from math import sin, cos, radians
from pygame import mixer
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class RSGlobals:
    zoom = 25
    xangle = 0
    yangle = 0
    time = 0
    falling_sparkles = []
    rainbows = []
    nyan = Nyan()
    rainbow_count = 15
    sparkles_per_frame = 5
    rotation_speed = 2
    vantage_height_max = 0.2
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
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 1)
    
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

    # add new objects
    for i in range(RSGlobals.sparkles_per_frame):
        xpos = random.random()*2 - 1 # -1 to 1
        zpos = random.random()*2 - 1 # -1 to 1
        ypos = 2                     # start above, fall
        RSGlobals.falling_sparkles.append(Sparkle(xpos, ypos, zpos))

    if time == 0:
        for i in range(RSGlobals.rainbow_count):
            xpos = random.random()*1.5 - 0.75
            ypos = random.random()*1.5 - 0.75
            zpos = random.random()*1.5 - 0.75
            RSGlobals.rainbows.append((SparklyRainbow(), xpos, ypos, zpos))
    
    # display objects
    # nyan cat
    glPushMatrix()
    # rotating around everything else
    glRotatef(3*RSGlobals.time, 0, 1, 0)
    glTranslatef(0, 0, -1)
    RSGlobals.nyan.render()
    glPopMatrix()
    # sparkles
    for sparkle in RSGlobals.falling_sparkles:
        sparkle.render()
        sparkle.ypos -= 0.05
        if sparkle.ypos < -2:
            RSGlobals.falling_sparkles.remove(sparkle)
    #rainbows
    glPushMatrix()
    # rotating relative to the rest of the system
    glRotate(-RSGlobals.rotation_speed*RSGlobals.time, 0, 1, 0)
    # sinusoidally vertically
    glTranslatef(0, RSGlobals.vantage_height_max*sin(radians(RSGlobals.time)), 0)
    for rainbow in RSGlobals.rainbows:
        glPushMatrix()
        glTranslatef(rainbow[1], rainbow[2], rainbow[3])
        rainbow[0].render()
        glPopMatrix()
    glPopMatrix()
    
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
    
    pygame.init()
    mixer.get_init()
    mixer.music.load('sounds/nyancat.mp3')
    mixer.music.play(-1)
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutSpecialUpFunc(specialUp)
    glutIdleFunc(display)
    glutMainLoop()

