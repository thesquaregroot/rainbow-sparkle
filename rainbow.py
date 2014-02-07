from OpenGL.GL import *
from math import sin, cos, radians

class Rainbow:
    DEFAULT_CENTRAL_ANGLE = 180
    DEFAULT_INNER_RADIUS = 0.05
    DEFAULT_OUTER_RADIUS = 0.15
    RESOLUTION_ANGLE = 5
    
    RED = [1, 0, 0]
    ORANGE = [1, 0.5, 0]
    YELLOW = [1, 1, 0]
    GREEN = [0, 1, 0]
    BLUE = [0, 0, 1]
    PURPLE = [1, 0, 1]

    COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

    def __init__(self, central_angle = DEFAULT_CENTRAL_ANGLE, inner_radius = DEFAULT_INNER_RADIUS, outer_radius = DEFAULT_OUTER_RADIUS):
        self.central_angle = central_angle
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
    
    def render(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        for color in Rainbow.COLORS:
            glColor3f(color[0], color[1], color[2])
            max_angle = self.central_angle / len(Rainbow.COLORS)
            i = 0
            while i != max_angle:
                glBegin(GL_QUADS)
                glVertex3f(self.inner_radius, 0, 0)
                glVertex3f(self.outer_radius, 0, 0)
                glVertex3f(self.outer_radius*cos(radians(Rainbow.RESOLUTION_ANGLE)), self.outer_radius*sin(radians(Rainbow.RESOLUTION_ANGLE)), 0)
                glVertex3f(self.inner_radius*cos(radians(Rainbow.RESOLUTION_ANGLE)), self.inner_radius*sin(radians(Rainbow.RESOLUTION_ANGLE)), 0)
                glEnd()
                glRotatef(Rainbow.RESOLUTION_ANGLE, 0, 0, 1)
                i = min(i+Rainbow.RESOLUTION_ANGLE, max_angle)
        glPopMatrix()
        glEnable(GL_LIGHTING)

