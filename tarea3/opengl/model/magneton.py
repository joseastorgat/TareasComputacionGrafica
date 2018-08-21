#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from utils.CC3501Utils import *
import math
import numpy as np

class Magneton(Figura):
    def __init__(self):
        pos = Vector(0, 0,0)
        rgb = (1.0, 1.0, 1.0)

        super().__init__(pos, rgb)

    def figura(self):
        #self.hoja()
        # glPushMatrix()
        self.cuerpo()
        
    def cuerpo(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0.5,0.5,0.5)
        esfera(radio=500, pos=Vector(0,0,0), max_theta= math.pi*160/180 )
        # glColor3f(1,1,1)
        # esfera(radio=500,pos=Vector(0,0,0), min_theta=math.pi*5/180, max_theta= math.pi*20/180 )
        glColor3f(0,0,0)
        esfera(radio=500, pos=Vector(0,0,0), min_theta= math.pi*160/180 )
        glEnd()

