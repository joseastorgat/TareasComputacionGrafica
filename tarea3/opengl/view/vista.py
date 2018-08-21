#!/usr/bin/env python
# -*- coding: utf-8 -*-


from OpenGL.GL import *
from OpenGL.GLUT import *

from utils.CC3501Utils import *
from utils.AuxiliaryFunctions import *
import pygame
import os

class Vista:
    def __init__(self, camera, pokemones):
        self.camera = camera
        self.pokemones = pokemones

    def dibujar(self, fill_polygons, show_axes):
    # limpia la pantalla (buffer de color y de profundidad)
        glutInit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if fill_polygons:
            glPolygonMode(GL_FRONT, GL_FILL) # Pintar 
            glPolygonMode(GL_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)

        # posibilidad de mostrar o no los ejes
        if show_axes:
            glCallList(axesList(100000))
        
        rgb = [0.0, 0.0, 0.0, 1.0]
        glColor4fv(rgb)

        for pokemon in self.pokemones:
          pokemon.dibujar()

        self.camera.mirar()

        # glLoadIdentity()
        # gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
        #           camAt.x, camAt.y, camAt.z,  # mirando hacia
        #           0.0, 0.0, 1.0)  # inclinacion
        
        pygame.display.flip()  # vuelca el dibujo a la pantalla
