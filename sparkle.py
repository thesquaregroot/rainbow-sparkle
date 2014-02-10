from OpenGL.GL import *
from OpenGL.GLUT import *

class Sparkle:
    GOLD    = [1, 0.5, 0, 1]
    dull_amb_and_diff    = [0.1, 0.1, 0.1, 1.0]
    dull_specular        = [0.2, 0.2, 0.2, 1.0]
    bright_amb_and_diff  = [0.8, 0.8, 0.8, 1.0]
    bright_specular      = [0.8, 0.8, 0.8, 1.0]
    
    def __init__(self, i=0, j=0, k=0):
        self.color = Sparkle.GOLD
        self.frame = 0
        self.xpos = i
        self.ypos = j
        self.zpos = k
    
    def render(self):
        glPushMatrix()
        glTranslatef(self.xpos, self.ypos, self.zpos)
        glScalef(0.01, 0.01, 0.01)
        glRotatef(5*self.frame, 0, 1, 0)
        glRotatef(10*self.frame, 1, 0, 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [i*j for i,j in zip(self.color, Sparkle.bright_amb_and_diff)])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR,            [i*j for i,j in zip(self.color, Sparkle.bright_specular)])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, [80])
        glBegin(GL_TRIANGLES)
        glVertex3f(   0,   0.3,  0)
        glVertex3f(-0.2, -0.2,  0)
        glVertex3f( 0.2, -0.2,  0)
        glEnd()
        glPopMatrix()
        self.frame += 1
        self.ypos -= 0.05

