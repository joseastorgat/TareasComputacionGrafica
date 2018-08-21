#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

#Utils
from utils.CC3501Utils import *
from utils.AuxiliaryFunctions import *

#Modelos
from model     import bronzor
# from model     import magneton

from model.camera    import Camera
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
        self.camera = Camera()

        self.vista = vista.Vista(camera= self.camera, pokemones=self.pokemones)
        #self.vista.dibujar()
        
        self.show_axes = True
        self.polygon = True
        self.color = "b"
        self.run = True

    def update(self):
        #ejes: rojo x
        #       

        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                self.run = False
            
        if pressed[K_UP]:
            self.camera.mover(Vector(0,0,1))
         
        if pressed[K_DOWN]:
            self.camera.mover(Vector(0,0,-1))
     
        if pressed[K_RIGHT]:
            self.camera.mover(Vector(0,1,0))
     
        if pressed[K_LEFT]:
            self.camera.mover(Vector(0,-1,0))

        if pressed[K_w]:
            if pressed[K_LSHIFT]:
                self.camera.mover(Vector(5,0,0))
            else:   
                self.camera.mover(Vector(2,0,0))
     
        if pressed[K_s]:
            if pressed[K_LSHIFT]:
                self.camera.mover(Vector(-5,0,0))
            else:   
                self.camera.mover(Vector(-2,0,0))
     
        if pressed[K_d]:
            self.camera.rotar(-1)
     
        if pressed[K_a]:
            self.camera.rotar(1)

        if pressed[K_1]:
            self.show_axes = not self.show_axes

        if pressed[K_2]:
            self.polygon = not self.polygon

        if pressed[K_3]:

            if self.color == "n":
                glClearColor(1.0, 1.0, 1.0, 1.0)
                self.color = "b"
            else :
                glClearColor(0.0, 0.0, 0.0, 1.0)
                self.color = "n"

        if pressed[K_ESCAPE]:
            run = False

        self.vista.dibujar(self.show_axes, self.polygon)
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

