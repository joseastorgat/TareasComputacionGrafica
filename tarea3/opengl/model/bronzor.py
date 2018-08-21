# -*- coding: utf-8 -*-
from utils.CC3501Utils import *
import math
import numpy as np

class Bronzor(Figura):
    def __init__(self):
        pos = Vector(0, 0,0)
        rgb = (1.0, 1.0, 1.0)

        self.re = 100;        # Radio Externo
        self.ri = self.re * (2/3); # radio Interno
        self.eg = self.re /5;      # espesor cilindro grande 
        self.ep = self.eg * 1.4;   # espesor cilindro pequeño
        self.resf = self.re/5;     # radio de pelotas
        self.rnariz = self.resf;   # 
        super().__init__(pos, rgb)

    def figura(self):
        #self.hoja()
        glPushMatrix()
        glScalef(10,10,10)
        glRotate(90,0,1,0)
        glRotate(180,0,0,1)

        self.cuerpo()
        
        glPushMatrix()
        glTranslatef(0, self.re/2.5, self.ep/2)
        self.ojo()
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0, -self.re/2.5, self.ep/2)
        self.ojo()
        glPopMatrix()
        

        self.cara()
        self.espalda()
        glPopMatrix()

    def cuerpo(self):
        glBegin(GL_TRIANGLES)
        glColor3f(61/255,171/255,188/255)
        cilindro(self.re, self.eg , Vector(0,0,-self.eg/2), precision= 20 )

        glColor3f(45/255,124/255,139/255)
        cilindro(self.ri, self.ep , Vector(0,0,-(self.ep)/2), precision= 20 )

        for i in range(30, 331, 60) :
            esfera(radio=self.resf,  pos=Vector(math.cos(i*(math.pi/180))*self.re, math.sin(i*(math.pi/180))*self.re,0));
        glColor3f(30/255,100/255,110/255)
        esfera(radio=self.rnariz, pos=Vector(0,0, self.ep/2), max_theta = math.pi/2) #nariz
        glEnd()

    def ojo(self):

        glPushMatrix()
        glScalef(2.0, 1.0, 1)
        glBegin(GL_TRIANGLES)
        glColor3f(1,1,1)
        cilindro(self.re/10, 2, Vector(0,0,0), precision= 20 )
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glScalef(2.5, 1.0, 1)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,0)
        cilindro(self.re/25, 3, Vector(0,0,0), precision= 20 )
        glEnd()
        glPopMatrix()
            
    def hoja(self):
        c = 0.40
        t = 0.65
        coords1 = [ (chord_function(c,t,x),100*x) for x in np.linspace(0,c/4, 10) ] + [(0,c*100)]
        coords2 = [ (chord_function(c,t,x),100*x) for x in np.linspace(c/4, c, 6) ] 

        glBegin(GL_POLYGON)
        for coord in coords1+coords2:#+coords3+coords4:
            glVertex3f(coord[1], coord[0],0 )

        for coord in coords1 + coords2:
            glVertex3f(coord[1], -coord[0],0 )
        glEnd()

    def rama(self, angle=0, pos=Vector(0,0,0), scale = 1 ):

        glPushMatrix()

        glTranslatef(pos.x,pos.y,pos.z)
        glRotate(angle,0,0,1)
        glScalef(scale,scale,scale)

        self.hoja()

        glBegin(GL_QUADS)
        glVertex3f(5,2, 0)
        glVertex3f(5,-2, 0)
        glVertex3f(-70,-6, 0)
        glVertex3f(-70,6,0)
        glEnd()
        glPopMatrix()

    def espalda(self):

        glColor3f(60/255,140/255,180/255)
        glTranslatef(18,0,-self.ep/2-1)
        self.rama()
        self.rama(65, Vector(-10,30,0), 0.5)
        self.rama(65, Vector(-40,30,0), 0.5)
        self.rama(-65, Vector(-10,-30,0), 0.5)
        self.rama(-65, Vector(-40,-30,0), 0.5)

    def cara(self):
        glColor3f(22/255,62/255,69/255)
        for i in [30,150,210,330]:  
            circulo( radio=self.re/15, pos=Vector(cos(i*math.pi/180)*(self.re/2.5+ self.re/60), sin(i*math.pi/180)*(self.re/2.5 + self.re/60),self.ep/2+1))
        

        circunferencia(radio= self.re/2.5, pos=Vector(0,0, self.ep/2+1))

def chord_function(c, t, x):

    return 100*(t*c/0.2)*(0.2969*sqrt(x/c)-0.1260*(x/c)-0.3516*((x/c)**2) + 0.2843*((x/c)**3) - 0.1015*((x/c)**4)) 


def circulo(radio, pos=Vector(0,0,0)):
    paso = 30
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(pos.x, pos.y, pos.z);# center of circle
    for i in range(paso+1):
        glVertex3f(pos.x + radio*math.cos(i*2*math.pi/paso),pos.y + radio*math.sin(i*2*math.pi/paso), pos.z )
    glEnd()

def circunferencia(radio, pos=Vector(0,0,0)):
    paso = 50
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    for i in range(paso):
        glVertex3f(pos.x + radio*math.cos(i*2*math.pi/paso),pos.y + radio*math.sin(i*2*math.pi/paso), pos.z )
    glEnd()

