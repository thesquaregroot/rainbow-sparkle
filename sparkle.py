from OpenGL.GL import *
from OpenGL.GLUT import glutSolidSphere

class Sparkle:
    WHITE   = [  1,    1,   1, 1]
    GOLD    = [  1,  0.5,   0, 1]
    GREEN   = [0.1,    1, 0.1, 1]
    YELLOW  = [  1,    1,   0, 1]
    SILVER  = [0.7,  0.7, 0.7, 1]
    amb_and_diff_prop = [0.7, 0.7, 0.7, 1.0]
    specular_prop     = [0.8, 0.8, 0.8, 1.0]

    def __init__(self):
        self.color = Sparkle.WHITE
    
    def render(self, i=0, j=0, k=0):
        glPushMatrix()
        glTranslatef(i, j, k)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [i*j for i,j in zip(self.color,Sparkle.amb_and_diff_prop)])
        glMaterialfv(GL_FRONT, GL_SPECULAR,            [i*j for i,j in zip(self.color,Sparkle.specular_prop)])
        glMaterialfv(GL_FRONT, GL_SHININESS,           [80])
        glutSolidSphere(0.01, 100, 100)
        self.nextColor()
        glPopMatrix()
    
    def nextColor(self):
        if self.color == Sparkle.WHITE:
            self.color = Sparkle.GOLD
        elif self.color == Sparkle.GOLD:
            self.color = Sparkle.YELLOW
        elif self.color == Sparkle.YELLOW:
            self.color = Sparkle.GREEN
        elif self.color == Sparkle.GREEN:
            self.color = Sparkle.SILVER
        else:
            self.color = Sparkle.WHITE

