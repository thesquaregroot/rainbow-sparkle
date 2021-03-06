from OpenGL.GL import *
from math import sin, cos, radians
from sparkle import Sparkle

class Rainbow:
    DEFAULT_CENTRAL_ANGLE = 180
    DEFAULT_INNER_RADIUS = 0.05
    DEFAULT_OUTER_RADIUS = 0.15
    DEFAULT_DEPTH = 0.01
    DEFAULT_OPACITY = 0.8
    RESOLUTION_ANGLE = 2
    
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
    EDGE_SPARKLES = 25
    END_SPARKLES = 5
    BUFFER_SPACE = 0.005

    def __init__(self, central_angle = Rainbow.DEFAULT_CENTRAL_ANGLE, inner_radius = Rainbow.DEFAULT_INNER_RADIUS, outer_radius = Rainbow.DEFAULT_OUTER_RADIUS, depth=Rainbow.DEFAULT_DEPTH, opacity=Rainbow.DEFAULT_OPACITY):
        Rainbow.__init__(self, central_angle, inner_radius, outer_radius, depth, opacity)
        self.sparkles = []
        sparkle_distance = depth + SparklyRainbow.BUFFER_SPACE
        for i in range(SparklyRainbow.EDGE_SPARKLES):
            # along front and back edges
            perc = float(i)/SparklyRainbow.EDGE_SPARKLES
            # left side
            self.sparkles.append(Sparkle(inner_radius + perc*(outer_radius-inner_radius)-SparklyRainbow.BUFFER_SPACE, 0, sparkle_distance))
            self.sparkles.append(Sparkle(inner_radius + perc*(outer_radius-inner_radius)-SparklyRainbow.BUFFER_SPACE, 0, -sparkle_distance))
            # right side
            self.sparkles.append(Sparkle(-(inner_radius + perc*(outer_radius-inner_radius)+SparklyRainbow.BUFFER_SPACE), 0, sparkle_distance))
            self.sparkles.append(Sparkle(-(inner_radius + perc*(outer_radius-inner_radius)+SparklyRainbow.BUFFER_SPACE), 0, -sparkle_distance))
        for i in range(SparklyRainbow.END_SPARKLES):
            # along outer end and inner end
            perc = float(i)/SparklyRainbow.END_SPARKLES
            # left side
            self.sparkles.append(Sparkle(inner_radius-SparklyRainbow.BUFFER_SPACE, 0, sparkle_distance - perc*2*sparkle_distance))
            self.sparkles.append(Sparkle(outer_radius+SparklyRainbow.BUFFER_SPACE, 0, sparkle_distance - perc*2*sparkle_distance))
            # right side
            self.sparkles.append(Sparkle(-inner_radius+SparklyRainbow.BUFFER_SPACE, 0, sparkle_distance - perc*2*sparkle_distance))
            self.sparkles.append(Sparkle(-outer_radius-SparklyRainbow.BUFFER_SPACE, 0, sparkle_distance - perc*2*sparkle_distance))
    
    def render(self):
        Rainbow.render(self);
        for sparkle in self.sparkles:
            sparkle.render()

