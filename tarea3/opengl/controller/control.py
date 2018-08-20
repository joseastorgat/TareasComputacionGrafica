#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

#Utils
from utils.CC3501Utils import *
from utils.AuxiliaryFunctions import *

#Modelos
from model     import bronzor
#from models.camera    import Camera


from view import vista


class Controller:
    def __init__(self, width, height):

        #Iniciar OpenGL
        init()
        reshape(width, height)
                
        #crear Pokemones  
        self.asda = bronzor.Bronzor()
        #self.bronzor = 1

        self.pokemones = [ self.asda]

        self.camPos = Vector(0, 0, 4000)  # posicion de la camara
        self.camAt = Vector(14140, -200, -328000)  # posicion que se enfoca
        glLoadIdentity()
        gluLookAt(2000.0, 2000.0, 2000.0,
                0.0, 0.0, 0.0,
                0.0, 0.0, 1.0)

        #self.camera = Camera()
        self.camera =1

        self.vista = vista.Vista(camera= self.camera, pokemones=self.pokemones)
        #self.vista.dibujar()
        

        self.run = True

    def update(self):
        

        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                self.run = False
            
        if pressed[K_UP]:
            self.camPos = sumar(ponderar(100, normalizar(self.camAt)), self.camPos)
     
        if pressed[K_DOWN]:
            self.camPos = sumar(ponderar(-100, normalizar(self.camAt)), self.camPos)
     
        if pressed[K_RIGHT]:
            self.camPos = sumar(ponderar(-100, rotarFi(normalizar(self.camAt), 90)), self.camPos)
     
        if pressed[K_LEFT]:
            self.camPos = sumar(ponderar(100, rotarFi(normalizar(self.camAt), 90)), self.camPos)

        if pressed[K_w]:
            self.camAt = sumar(Vector(0, 0, 1000), self.camAt)
     
        if pressed[K_s]:
            self.camAt = sumar(Vector(0, 0, -1000), self.camAt)
     
        if pressed[K_d]:
            self.camAt = rotarFi(self.camAt, 0.1)
     
        if pressed[K_a]:
            self.camAt = rotarFi(self.camAt, -0.1)

        # Cambiar desde donde se mira

        if pressed[K_1]:
            self.camPos = Vector(0, 0, 4000)
            self.camAt = Vector(14140, -200, -328000)

        if pressed[K_2]:
            self.camPos = Vector(1926.700, 1926.700, 104.30)
            self.camAt = Vector(-10000, -10000, -2000)

        if pressed[K_3]:
            self.camPos = Vector(0, 0, -4000)
            self.camAt = Vector(-14140, 200, 328000)

        if pressed[K_ESCAPE]:
            run = False

        self.vista.dibujar(self.camAt, self.camPos)
        return self.run


### los siguientes métodos fueron extraídos desde el Ejemplo :

def init():
    # setea el color de fondo
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glEnable(GL_BLEND) # Transparencias
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glShadeModel(GL_SMOOTH) # Tipo de iluminación
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)  # Proyección en perspectiva
    glLoadIdentity()
    gluPerspective(60.0, float(width) / float(height), 0.1, 20000.0)
    # glOrtho(-w,w,-h,h,1,20000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

