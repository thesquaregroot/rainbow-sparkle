from OpenGL.GL import *
from math import sin, cos, radians

class Rainbow:
    DEFAULT_CENTRAL_ANGLE = 180
    DEFAULT_INNER_RADIUS = 0.05
    DEFAULT_OUTER_RADIUS = 0.15
    RESOLUTION_ANGLE = 1
    
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
    
    def setColor(self, color, next_color, angle, max_angle):
        red = float((max_angle-angle)*color[0] + angle*next_color[0])/max_angle
        grn = float((max_angle-angle)*color[1] + angle*next_color[1])/max_angle
        blu = float((max_angle-angle)*color[2] + angle*next_color[2])/max_angle
        glColor3f(red, grn, blu)
    
    def render(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        for color_index in range(len(Rainbow.COLORS)-1):
            color = Rainbow.COLORS[color_index]
            next_color = Rainbow.COLORS[color_index+1]
            max_angle = self.central_angle / (len(Rainbow.COLORS)-1)
            angle = 0
            increase = Rainbow.RESOLUTION_ANGLE
            while angle != max_angle:
                self.setColor(color, next_color, angle, max_angle)
                glBegin(GL_QUADS)
                glVertex3f(self.inner_radius, 0, 0)
                glVertex3f(self.outer_radius, 0, 0)
                glVertex3f(self.outer_radius*cos(radians(Rainbow.RESOLUTION_ANGLE)), self.outer_radius*sin(radians(Rainbow.RESOLUTION_ANGLE)), 0)
                glVertex3f(self.inner_radius*cos(radians(Rainbow.RESOLUTION_ANGLE)), self.inner_radius*sin(radians(Rainbow.RESOLUTION_ANGLE)), 0)
                glEnd()
                glRotatef(increase, 0, 0, 1)
                increase = min(Rainbow.RESOLUTION_ANGLE, max_angle-angle)
                angle += increase
        glPopMatrix()
        glEnable(GL_LIGHTING)

