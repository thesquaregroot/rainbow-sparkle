from OpenGL.GL import *
from rainbow import Rainbow

class Nyan:
    BLACK = [0, 0, 0]
    BROWN = [0.8, 0.6, 0.3]
    PINK = [1, 0.7, 0.8]
    RED = [1, 0.1, 0.5]
    GRAY = [0.6, 0.6, 0.6]
    WHITE = [1, 1, 1]

    DEFAULT_WIDTH = 0.1
    TRAIL_LENGTH = 5
    POP_TART = [
                    [None,  None,   BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  None,   None],
                    [None,  BLACK,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BLACK,  None],
                    [BLACK, BROWN,  BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   RED,    PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   RED,    PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  PINK,   PINK,   RED,    PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BLACK],
                    [BLACK, BROWN,  BROWN,  PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   PINK,   BROWN,  BROWN,  BLACK],
                    [None,  BLACK,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BROWN,  BLACK,  None],
                    [None,  None,   BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  None,   None]
                ]
    FACE = [
                [None,  None,   BLACK,  BLACK,  None,   None,   None,   None,   None,   None,   None,   None,   None,   BLACK,  BLACK,  None,   None],
                [None,  BLACK,  GRAY,   GRAY,   BLACK,  None,   None,   None,   None,   None,   None,   None,   BLACK,  GRAY,   GRAY,   BLACK,  None],
                [None,  BLACK,  GRAY,   GRAY,   GRAY,   BLACK,  None,   None,   None,   None,   None,   BLACK,  GRAY,   GRAY,   GRAY,   BLACK,  None],
                [None,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  None,   None,   None,   BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  None],
                [None,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  BLACK,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  None],
                [None,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  None],
                [BLACK, GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK],
                [BLACK, GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK],
                [BLACK, GRAY,   GRAY,   GRAY,   GRAY,   WHITE,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   WHITE,  BLACK,  GRAY,   GRAY,   BLACK],
                [BLACK, GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  BLACK,  GRAY,   GRAY,   GRAY,   BLACK,  GRAY,   BLACK,  BLACK,  GRAY,   GRAY,   BLACK],
                [BLACK, GRAY,   PINK,   PINK,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   PINK,   PINK,   BLACK],
                [BLACK, GRAY,   PINK,   PINK,   GRAY,   GRAY,   BLACK,  GRAY,   GRAY,   BLACK,  GRAY,   GRAY,   BLACK,  GRAY,   PINK,   PINK,   BLACK],
                [None,  BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  GRAY,   GRAY,   BLACK,  None],
                [None,  None,   BLACK,  GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   GRAY,   BLACK,  None,   None],
                [None,  None,   None,   BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  BLACK,  None,   None,   None]
            ]
    TAIL1 = [
                [BLACK, BLACK,  BLACK,  BLACK,  None,   None],
                [BLACK, GRAY,   GRAY,   BLACK,  BLACK,  None],
                [BLACK, BLACK,  GRAY,   GRAY,   BLACK,  BLACK],
                [None,  BLACK,  BLACK,  GRAY,   GRAY,   BLACK],
                [None,  None,   BLACK,  BLACK,  GRAY,   GRAY],
                [None,  None,   None,   BLACK,  BLACK,  BLACK],
                [None,  None,   None,   None,   BLACK,  BLACK]
            ]
    TAIL2 = [
                [None,  None,   None,   None,   None,   None],
                [None,  None,   None,   None,   None,   None],
                [None,  None,   None,   None,   None,   BLACK],
                [None,  None,   BLACK,  BLACK,  BLACK,  BLACK],
                [BLACK, BLACK,  GRAY,   GRAY,   GRAY,   GRAY],
                [BLACK, GRAY,   GRAY,   GRAY,   BLACK,  BLACK],
                [None,  BLACK,  BLACK,  BLACK,  BLACK,  None]
            ]
    FEET1 = [
                [None,  BLACK,  BLACK,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                [BLACK, GRAY,   GRAY,   GRAY,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                [BLACK, GRAY,   GRAY,   BLACK,  None,   BLACK,  GRAY,   GRAY,   BLACK,  None,   None,   None,   None,   None,   BLACK,  GRAY,   GRAY,   BLACK,  None,   None,   BLACK,  GRAY,   GRAY,   BLACK,  None],
                [BLACK, BLACK,  BLACK,  None,   None,   BLACK,  BLACK,  BLACK,  None,   None,   None,   None,   None,   None,   None,   BLACK,  BLACK,  BLACK,  None,   None,   None,   BLACK,  BLACK,  BLACK,  None]
            ]
    FEET2 = [
                [None,  None,  BLACK,  BLACK,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                [None,  BLACK, GRAY,   GRAY,    BLACK,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                [None,  BLACK, GRAY,   GRAY,    BLACK,  None,   BLACK,  GRAY,   GRAY,   BLACK,  None,   None,   None,   None,   None,   BLACK,  GRAY,   GRAY,   BLACK,  None,   None,   BLACK,  GRAY,   GRAY,   BLACK],
                [None,  BLACK, BLACK,  BLACK,   None,   None,   None,   BLACK,  BLACK,  BLACK,  None,   None,   None,   None,   None,   None,   BLACK,  BLACK,  BLACK,  None,   None,   None,   BLACK,  BLACK,  None]
            ]

    TRAILING_RAINBOW = [
                            [Rainbow.RED,       Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED],
                            [Rainbow.RED,       Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED],
                            [Rainbow.RED,       Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED,    Rainbow.RED],
                            [Rainbow.ORANGE,    Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE],
                            [Rainbow.ORANGE,    Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE],
                            [Rainbow.ORANGE,    Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE, Rainbow.ORANGE],
                            [Rainbow.YELLOW,    Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW],
                            [Rainbow.YELLOW,    Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW],
                            [Rainbow.YELLOW,    Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW, Rainbow.YELLOW],
                            [Rainbow.GREEN,     Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN],
                            [Rainbow.GREEN,     Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN],
                            [Rainbow.GREEN,     Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN,  Rainbow.GREEN],
                            [Rainbow.BLUE,      Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE],
                            [Rainbow.BLUE,      Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE],
                            [Rainbow.BLUE,      Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE,   Rainbow.BLUE],
                            [Rainbow.PURPLE,    Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE],
                            [Rainbow.PURPLE,    Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE],
                            [Rainbow.PURPLE,    Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE, Rainbow.PURPLE]
                        ]
    
    def __init__(self, pop_tart_width = DEFAULT_WIDTH):
        self.cube_width = float(pop_tart_width) / len(Nyan.POP_TART[0])
        self.pos = 0
    
    def draw_cube(self, width, front_color, base_color):
        # draw front_colored square
        glBegin(GL_QUADS)
        glColor3f(front_color[0], front_color[1], front_color[2])
        glVertex3f(0,       0,       -width)
        glVertex3f(-width,   0,       -width)
        glVertex3f(-width,   -width,  -width)
        glVertex3f(0,       -width,  -width)
        # draw back of head (and then sides)
        if base_color != None:
            glColor3f(base_color[0], base_color[1], base_color[2])
        glVertex3f(0,        0,       0)
        glVertex3f(-width,    0,       0)
        glVertex3f(-width,    -width,  0)
        glVertex3f(0,        -width,  0)
        # top
        glVertex3f(0,        0,  -width)
        glVertex3f(-width,    0,  -width)
        glVertex3f(-width,    0,  0)
        glVertex3f(0,        0,  0)
        # bottom
        glVertex3f(0,        -width,  -width)
        glVertex3f(-width,    -width,  -width)
        glVertex3f(-width,    -width,  0)
        glVertex3f(0,        -width,  0)
        # left
        glVertex3f(0,   0,       0)
        glVertex3f(0,   0,       -width)
        glVertex3f(0,   -width,  -width)
        glVertex3f(0,   -width,  0)
        # right
        glVertex3f(-width,   0,       0)
        glVertex3f(-width,   0,       -width)
        glVertex3f(-width,   -width,  -width)
        glVertex3f(-width,   -width,  0)
        glEnd()

    def draw_from_matrix(self, matrix, cube_width, base_color):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # get cube color by index
                color = matrix[i][j]
                if color is not None:
                    glPushMatrix()
                    # move to cube position
                    glTranslatef(-cube_width*j, -cube_width*i, 0)
                    # draw cube
                    self.draw_cube(cube_width, color, base_color)
                    glPopMatrix()
    
    def render(self):
        pos_offset = self.cube_width * self.pos
        pop_tart_width = len(Nyan.POP_TART[0])*self.cube_width
        pop_tart_height = len(Nyan.POP_TART)*self.cube_width
        face_width = len(Nyan.FACE[0])*self.cube_width
        face_height = len(Nyan.FACE)*self.cube_width

        glDisable(GL_LIGHTING)
        glPushMatrix()
        # attempt to center nyan cat
        glTranslate(pop_tart_width/2-self.pos*self.cube_width, pop_tart_height/2, 0)
        # draw pop tart
        self.draw_from_matrix(Nyan.POP_TART, self.cube_width, Nyan.BROWN)
        
        height_diff = pop_tart_height - face_height
        # move to head position
        glPushMatrix()
        glTranslate(-(pop_tart_width - face_width*2/3), -height_diff+pos_offset, -self.cube_width)
        # draw head
        self.draw_from_matrix(Nyan.FACE, self.cube_width, Nyan.GRAY)
        glPopMatrix()
        
        # draw tail/legs
        tail = Nyan.TAIL1
        feet = Nyan.FEET1
        if self.pos == 1:
            tail = Nyan.TAIL2
            feet = Nyan.FEET2
        glPushMatrix()
        glTranslate(len(tail[0])*self.cube_width, -pop_tart_height/3, -self.cube_width)
        self.draw_from_matrix(tail, self.cube_width, Nyan.GRAY)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(2*self.cube_width, -(pop_tart_height-2*self.cube_width), -self.cube_width)
        self.draw_from_matrix(feet, self.cube_width, Nyan.GRAY)
        glPopMatrix()
        
        # rainbow
        glPushMatrix()
        glTranslate(len(Nyan.TRAILING_RAINBOW[0])*self.cube_width, pos_offset, 0)
        self.draw_from_matrix(Nyan.TRAILING_RAINBOW, self.cube_width, None)
        for i in range(Nyan.TRAIL_LENGTH):
            glTranslate(len(Nyan.TRAILING_RAINBOW[0])*self.cube_width, (1-2*self.pos)*self.cube_width, 0)
            self.draw_from_matrix(Nyan.TRAILING_RAINBOW, self.cube_width, None)
            glTranslate(len(Nyan.TRAILING_RAINBOW[0])*self.cube_width, (2*self.pos-1)*self.cube_width, 0)
            self.draw_from_matrix(Nyan.TRAILING_RAINBOW, self.cube_width, None)
        glPopMatrix()

        glPopMatrix()
        glEnable(GL_LIGHTING)
        
        # next pos
        self.pos = (self.pos+1) % 2

