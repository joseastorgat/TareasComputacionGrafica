# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *

from utils.CC3501Utils import *
from utils.AuxiliaryFunctions import *
import pygame
import os

import math
import numpy as np

class Camera(Figura):
    def __init__(self, pos_camera=Vector(4000,0,0), looking_at=Vector(0,0,0), cam_orientation=Vector(0,0,1)):

        self.pos = pos_camera
        self.lookAt = looking_at
        self.orientation = cam_orientation
        self.r_vel =10
        self.fi_vel = 0.1
        self.theta_vel = 0.1
        self.angulo = 0
        self.vel_ang = 0.1

    def mirar(self):

        # pond = 1 if self._thetha > -math.pi and self._thetha < math.pi else -1

        glLoadIdentity()
        gluLookAt(self.pos.x, self.pos.y, self.pos.z,  # posicion
                  self.lookAt.x, self.lookAt.y, self.lookAt.z,  # mirando hacia
                  self.orientation.x, self.orientation.y,  self.orientation.z)  # inclinacion

    def mover(self, vel = Vector(0,0,0)):

        # pond = 1 if self._thetha > -math.pi/2 and self._thetha < math.pi/2-0.1 else -1
        if ((self.pos.theta()+self.theta_vel*vel.z)>0 and (self.pos.theta()+self.theta_vel*vel.z) < math.pi):
            self.pos = rotarTheta(self.pos , self.theta_vel*vel.z)
        self.pos = rotarFi(self.pos , self.fi_vel*vel.y)
        self.pos = desplazarRadialmente(self.pos , self.r_vel*vel.x)

    def rotar(self, vel):

        self.angulo += vel*self.vel_ang
        self.orientation = Vector(0, math.sin(self.angulo), math.cos(self.angulo))


    def translate(self, new_pos = Vector(0,0,1000)):
        self.pos = new_pos

    def change_focus(self, new_focus = Vector(0,0,0)):
        self.lookAt = new_focus