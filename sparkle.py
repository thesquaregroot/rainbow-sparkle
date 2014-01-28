from OpenGL.GL import *

class Sparkle:
    WHITE   = [1, 1, 1]
    RED     = [1, 0, 0]
    GREEN   = [0, 1, 0]
    YELLOW  = [1, 1, 0]
    BLUE    = [0, 0, 1]

    def __init__(self):
        self.color = Sparkle.WHITE
    
    def render(self, i, j, k):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_POINTS)
        glVertex3f(i, j, k)
        glEnd()
        self.nextColor()
    
    def nextColor(self):
        if self.color == Sparkle.WHITE:
            self.color = Sparkle.RED
        elif self.color == Sparkle.RED:
            self.color = Sparkle.YELLOW
        elif self.color == Sparkle.YELLOW:
            self.color = Sparkle.GREEN
        elif self.color == Sparkle.GREEN:
            self.color = Sparkle.BLUE
        else:
            self.color = Sparkle.WHITE
    

