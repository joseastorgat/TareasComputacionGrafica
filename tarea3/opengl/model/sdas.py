# -*- coding: utf-8 -*-
from utils.CC3501Utils import *
import math


class Bronzor:
    # Crea un paralelepipedo centrado en 0 con las dimensiones especificadas
    def __init__(self):
        self.pos = Vector(0, 0, 0)
        self.angulo = 0

        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        glBegin(GL_TRIANGLES)

        glColor3f(0, 128 / 255, 128 / 255)
        cilindro(1000, 400, Vector(0, 0, -200))
        glColor3f(0, 70 / 255, 128 / 255)
        cilindro(800, 440, Vector(0, 0, -220))

        r = 1000
        t = 0
        for i in range(0, 6):
            x = r * math.cos(t)
            y = r * math.sin(t)
            esfera(200, Vector(x, y, 0))
            t += math.pi / 3

        glColor3f(0, 128 / 255, 128 / 255)
        r = 400
        t = 30 * (math.pi / 180)
        x = r * math.cos(t)
        y = r * math.sin(t)
        z = 200
        esfera(60, Vector(x, y, z))
        esfera(60, Vector(x, -1 * y, z))
        esfera(60, Vector(-1 * x, -1 * y, z))
        esfera(60, Vector(-1 * x, y, z))

        esfera(200, Vector(0, 0, 200))
        glEnd()

        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        r = 400
        t_i = 0
        for i in range(0, int(360 / 30)):
            t_f = t_i + 30 * (math.pi / 180)
            x_i = r * math.cos(t_i)
            x_f = r * math.cos(t_f)
            y_i = r * math.sin(t_i)
            y_f = r * math.sin(t_f)
            glVertex3f(x_i, y_i, 221)
            glVertex3f(x_f, y_f, 221)
            t_i += 30 * (math.pi / 180)
        glEnd()

        glLineWidth(1)

        glPushMatrix()
        glTranslatef(-350, -250, 0)
        glRotatef(90, 0, 0, 1)
        self.eye()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-350, 450, 0)
        glRotatef(90, 0, 0, 1)
        self.eye()
        glPopMatrix()

        glColor3f(0, 90 / 255, 128 / 255)
        glPushMatrix()
        glTranslatef(250, 0, 0)
        glRotatef(-90, 0, 0, 1)
        self.leaf(35)
        self.branch2(20, 40)
        glPopMatrix()

        a = 20
        an = -20
        t_y = -300
        t_x = -200
        h = 15
        glPushMatrix()
        glTranslatef(100, t_y, 0)
        glRotatef(180 - an, 0, 0, 1)
        self.leaf(a)
        self.branch(a, h)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(100, -1 * t_y, 0)
        glRotatef(an, 0, 0, 1)
        self.leaf(a)
        self.branch(a, h)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(t_x, t_y, 0)
        glRotatef(180 - an, 0, 0, 1)
        self.leaf(a)
        self.branch(a, h)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(t_x, -1 * t_y, 0)
        glRotatef(an, 0, 0, 1)
        self.leaf(a)
        self.branch(a, h)
        glPopMatrix()

        glEndList()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje Z
        glCallList(self.lista)
        glPopMatrix()

    def eye(self):
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        x = 0
        y = -450
        z = 230
        glVertex3f(x, y, z)
        glVertex3f(x, y + 200, z)
        glVertex3f(x - 25, y + 250, z)
        glVertex3f(x - 75, y + 300, z)
        glVertex3f(x - 125, y + 300, z)
        glVertex3f(x - 175, y + 250, z)
        glVertex3f(x - 200, y + 200, z)
        glVertex3f(x - 200, y, z)
        glVertex3f(x - 175, y - 50, z)
        glVertex3f(x - 125, y - 100, z)
        glVertex3f(x - 75, y - 100, z)
        glVertex3f(x - 25, y - 50, z)

        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        x = 0
        y = -450
        z = 232
        glVertex3f(x - 50, y + 50, z)
        glVertex3f(x - 50, y + 150, z)
        glVertex3f(x - 75, y + 200, z)
        glVertex3f(x - 125, y + 200, z)
        glVertex3f(x - 150, y + 150, z)
        glVertex3f(x - 150, y + 50, z)
        glVertex3f(x - 125, y, z)
        glVertex3f(x - 75, y, z)

        glEnd()

    def leaf(self, a):
        glBegin(GL_POLYGON)
        z = -230
        glVertex3f(1 * a, 0, z)
        glVertex3f(3 * a, 1 * a, z)
        glVertex3f(4 * a, 3 * a, z)
        glVertex3f(4 * a, 5 * a, z)
        glVertex3f(3.5 * a, 7 * a, z)
        glVertex3f(2.5 * a, 9 * a, z)
        glVertex3f(1.5 * a, 10 * a, z)

        glVertex3f(0, 11 * a, z)

        glVertex3f(-1.5 * a, 10 * a, z)
        glVertex3f(-2.5 * a, 9 * a, z)
        glVertex3f(-3.5 * a, 7 * a, z)
        glVertex3f(-4 * a, 5 * a, z)
        glVertex3f(-4 * a, 3 * a, z)
        glVertex3f(-3 * a, 1 * a, z)
        glVertex3f(-1 * a, 0, z)

        glEnd()

    def branch(self, a, h):
        glBegin(GL_QUADS)
        z = -230
        glVertex3f(-1 * a, 0, z)
        glVertex3f(1 * a, 0 * a, z)
        glVertex3f(2 * a, -1 * h * a, z)
        glVertex3f(-2 * a, -1 * h * a, z)

        glEnd()

    def branch2(self, a, h):
        glBegin(GL_POLYGON)
        z = -230
        glVertex3f(-1.5 * a, 0, z)
        glVertex3f(1.5 * a, 0 * a, z)
        glVertex3f(4 * a, -1 * h * a, z)
        glVertex3f(-4 * a, -1 * h * a, z)

        glEnd()
