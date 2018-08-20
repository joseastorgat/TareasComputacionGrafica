#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller.control import *
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

def main():

    w = 800 
    h = 600

    pygame.init()
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
    pygame.display.set_caption('Pokemons')

    game = Controller(w,h)
    run = True
    while run:
        run = game.update()
        pygame.time.wait(int(1000/30))
    pygame.quit()

if __name__ == '__main__':
    main()











