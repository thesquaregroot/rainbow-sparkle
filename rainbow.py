from OpenGL.GL import *
from math import sin, cos, radians
from sparkle import Sparkle

class Rainbow:
    DEFAULT_CENTRAL_ANGLE = 180
    DEFAULT_INNER_RADIUS = 0.05
    DEFAULT_OUTER_RADIUS = 0.15
    DEFAULT_DEPTH = 0.01
    DEFAULT_OPACITY = 0.8
    RESOLUTION_ANGLE = 1
    
    RED = [1, 0, 0]
    ORANGE = [1, 0.5, 0]
    YELLOW = [1, 1, 0]
    GREEN = [0, 1, 0]
    BLUE = [0, 0, 1]
    PURPLE = [1, 0, 1]

    COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

    def __init__(self, central_angle = DEFAULT_CENTRAL_ANGLE, inner_radius = DEFAULT_INNER_RADIUS, outer_radius = DEFAULT_OUTER_RADIUS, depth=DEFAULT_DEPTH, opacity=DEFAULT_OPACITY):
        self.central_angle = central_angle
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.depth = depth
        self.opacity = opacity
    
    def setColor(self, color, next_color, angle, max_angle):
        red = float((max_angle-angle)*color[0] + (angle+1)*next_color[0])/max_angle
        grn = float((max_angle-angle)*color[1] + angle*next_color[1])/max_angle
        blu = float((max_angle-angle)*color[2] + angle*next_color[2])/max_angle
        glColor4f(red, grn, blu, self.opacity)
#        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [red, grn, blu, self.opacity])
#        glMaterialfv(GL_FRONT, GL_SPECULAR, [red, grn, blu, self.opacity])
#        glMaterialfv(GL_FRONT, GL_SHININESS, [10])

    def render(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        for color_index in range(len(Rainbow.COLORS)-1):
            color = Rainbow.COLORS[color_index]
            next_color = Rainbow.COLORS[color_index+1]
            max_angle = self.central_angle / (len(Rainbow.COLORS)-1)
            angle = 0
            while angle != max_angle:
                increase = min(Rainbow.RESOLUTION_ANGLE, max_angle-angle)
                self.setColor(color, next_color, angle, max_angle)
                glBegin(GL_QUAD_STRIP)
                # create square cylinder (slight fan)
                glVertex3f(self.inner_radius, 0, self.depth)
                glVertex3f(self.outer_radius, 0, self.depth)
                glVertex3f(self.inner_radius*cos(radians(increase)), self.inner_radius*sin(radians(increase)), self.depth)
                glVertex3f(self.outer_radius*cos(radians(increase)), self.outer_radius*sin(radians(increase)), self.depth)
                glVertex3f(self.inner_radius*cos(radians(increase)), self.inner_radius*sin(radians(increase)), -self.depth)
                glVertex3f(self.outer_radius*cos(radians(increase)), self.outer_radius*sin(radians(increase)), -self.depth)
                glVertex3f(self.inner_radius, 0, -self.depth)
                glVertex3f(self.outer_radius, 0, -self.depth)
                glVertex3f(self.inner_radius, 0, self.depth)
                glVertex3f(self.outer_radius, 0, self.depth)
                glEnd()
                glBegin(GL_QUADS)
                # close top with square
                glVertex3f(self.outer_radius, 0, self.depth)
                glVertex3f(self.outer_radius*cos(radians(increase)), self.outer_radius*sin(radians(increase)), self.depth)
                glVertex3f(self.outer_radius*cos(radians(increase)), self.outer_radius*sin(radians(increase)), -self.depth)
                glVertex3f(self.outer_radius, 0, -self.depth)
                # close bottom with square
                glVertex3f(self.inner_radius, 0, self.depth)
                glVertex3f(self.inner_radius*cos(radians(increase)), self.inner_radius*sin(radians(increase)), self.depth)
                glVertex3f(self.inner_radius*cos(radians(increase)), self.inner_radius*sin(radians(increase)), -self.depth)
                glVertex3f(self.inner_radius, 0, -self.depth)
                glEnd()
                glRotatef(increase, 0, 0, 1)
                angle += increase
        glPopMatrix()
        glEnable(GL_LIGHTING)

class SparklyRainbow(Rainbow):
    def __init__(self, central_angle = Rainbow.DEFAULT_CENTRAL_ANGLE, inner_radius = Rainbow.DEFAULT_INNER_RADIUS, outer_radius = Rainbow.DEFAULT_OUTER_RADIUS, depth=Rainbow.DEFAULT_DEPTH, opacity=Rainbow.DEFAULT_OPACITY):
        super().__init__(central_angle, inner_radius, outer_radius, depth, opacity)
        self.sparkles = []
        for i in range(50):
            self.sparkles.append(Sparkle(float(i*2.0)/10.0 + 5.25, 0.1, -1))
            self.sparkles.append(Sparkle(-float(i*2.0)/10.0 - 5.25, 0.1, -1))
            self.sparkles.append(Sparkle(float(i*2.0)/10.0 + 5.25, 0.1, 1))
            self.sparkles.append(Sparkle(-float(i*2.0)/10.0 - 5.25, 0.1, 1))
        for i in range(20):
            self.sparkles.append(Sparkle(15.25, 0.1, -1.0 + float(i)/10.0))
            self.sparkles.append(Sparkle(4.75, 0.1, -1.0 + float(i)/10.0))
            self.sparkles.append(Sparkle(-15.25, 0.1, -1.0 + float(i)/10.0))
            self.sparkles.append(Sparkle(-4.75, 0.1, -1.0 + float(i)/10.0))
    
    def render(self):
        super().render();
        for sparkle in self.sparkles:
            sparkle.render()

