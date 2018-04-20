# coding=utf-8

"""Tarea 1
@author José
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color  # grafico

import tqdm
import numpy as np
import math


def rho1(i,j):
    return 0

def rho2(i,j,):
    return 1.0/(math.sqrt(( float(i)**2+ float(j)**2 + 120.0 )))

class Litoral:
    def __init__(self, ancho=4000, alto=2000, dh = 10, RRR=103, omega = 1):
        """
        Constructor
        :param ancho: Ancho
        :param alto: alto
        :param dh: Tamaño grilla diferencial
        :type ancho: int,float
        """
        self._ancho = ancho  # privada
        self._alto = alto
        self._dh = dh
        self._RRR= RRR

        self._h = int(float(alto) / dh)
        self._w = int(float(ancho) / dh)
        
        self.omega = omega   
        self._rrr = RRR/1000.0

        self._geografia = np.zeros((self._h, self._w))
        self._matrix = np.zeros((self._h, self._w))

    def reset(self):
        self.__init__(self._ancho, self._alto, self._dh)

    def get_omega_optimo(self):
        m = self._h
        n = self._w
        a = 2.0 + math.sqrt( 4.0 - (math.cos(math.pi/(n-1.0)) + math.cos(math.pi/(m-1.0)))**2)      
        self.omega = 4.0/a
        print(self.omega)

    def set_geografia(self):
        """
        Construye la geografia del Litoral
        :return:
        """


        _p1 = ( (1200.0 + 400.0*self._rrr), 0) #comienzo de playa y fabrica
        _p2 = ( _p1[0] + 120.0, 0) # fin playa y fabrica, comienzo elevación
        _p3 = ( _p1[0] + 400.0, (_p1[0] + 400.0 -_p2[0])*(100.0/300.0)) # fin elevacion suave, comienzo montaña 1
        _p4 = ( _p3[0] + 800.0, (1500.0 + 200.0*self._rrr)) # pico montaña 1
        _p5 = ( _p4[0] + 300.0, (1300.0 + 200.0*self._rrr)) # valle entre montañas
        _p6 = ( _p4[0] + 800.0, (1850.0 + 100.0*self._rrr)) # pico montaña 2

        p1 = (int(_p1[0]/self._dh), int(_p1[1]/self._dh))
        p2 = (int(_p2[0]/self._dh), int(_p2[1]/self._dh))
        p3 = (int(_p3[0]/self._dh), int(_p3[1]/self._dh))
        p4 = (int(_p4[0]/self._dh), int(_p4[1]/self._dh))
        p5 = (int(_p5[0]/self._dh), int(_p5[1]/self._dh))
        p6 = (int(_p6[0]/self._dh), int(_p6[1]/self._dh))
        p7 = (self._w - 1 , int(self._h/2))

        snow = int(1800.0/self._dh) # altura de nieve > 1800
        fab_h = int(math.ceil(20.0/self._dh)) #altura de la fabrica es 20m

        self.puntos = {"p1" : p1, "p2" : p2, "p3" : p3, "p4" : p4, "p5" : p5, "p6" : p6, "p7" : p7, "snow" : snow, "fabrica_h":fab_h} 
        self._geografia[0,p1[0]:p3[0]] = 3
        
        for x in range(0,self._w):
            if x < p1[0]:
                self._geografia[0,x] = 1 # Agua 
            
            elif x < p2[0]: 
                self._geografia[1:1+fab_h,x] = 2 #fabrica, altura 20 m

            elif x < p3[0]:
                n = p2[1]
                m = float(p3[1] - p2[1])/float(p3[0]-p2[0])
                y = int(n + m*(x-p2[0]))
                self._geografia[0:y,x] = 3 #Tierra

            elif x < p4[0]:
                n = p3[1]
                m = float(p4[1] - p3[1])/float(p4[0]-p3[0])
                y = int(n + m*(x-p3[0]))
                self._geografia[0:y,x] = 3#Tierra

            elif x < p5[0]:
                n = p4[1]
                m = float(p5[1] - p4[1])/float(p5[0]-p4[0])
                y = int(n + m*(x-p4[0]))
                self._geografia[0:y,x] = 3#Tierra

            elif x < p6[0]:
                n = p5[1]
                m = float(p6[1] - p5[1])/float(p6[0]-p5[0])
                y = int(n + m*(x-p5[0]))
                if y>snow:
                    self._geografia[snow:y,x] = 4#Nieve
                    self._geografia[0:snow,x] = 3#Tierra
                else:
                    self._geografia[0:y,x] = 3#Tierra

            else:
                n = p6[1]
                m = float(p7[1] - p6[1])/float(p7[0]-p6[0])
                y = int(n + m*(x-p6[0]))
                if y>snow:
                    self._geografia[snow:y,x] = 4#Nieve
                    self._geografia[0:snow,x] = 3#Tierra
                else:
                    self._geografia[0:y,x] = 3#Tierra
        return

    def cb(self, hora=0.0):
        """
        Pone cond borde
        :param hora: Hora
        :return:
        """

        # Playa-Mar:
        if hora>=0.0 and hora<8.0:
            M  = 4.0

        elif hora>=8.0 and hora<16.0:
            n = 4.0
            m = (20.0-4.0)/(16.0-8.0)
            M = m*(hora-8.0)+n
        
        elif hora>=16.0:
            n = 20.0
            m = (4.0-20.0)/(20.0-16.0)
            M = m*(hora-16.0)+n
        #Tierra:
        T = 20.0
        #Nieve
        N = 0.0
        #Fabrica
        F = 450*(math.cos((math.pi/12)*hora)+2)

        for y in range(0,self._h):
            temp = M - (6.0/1000.0)*(y*self._dh)

            for x in range(0,self._w):

                if self._geografia[y,x] == 1: #Mar
                    self._matrix[y,x] = M
                
                elif self._geografia[y,x] == 2: #Fabrica
                    self._matrix[y,x] = F
                
                elif self._geografia[y,x] == 3: #Tierra
                    self._matrix[y,x] = T
                
                elif self._geografia[y,x] == 4: #Nieve
                    self._matrix[y,x] = N

                elif self._geografia[y,x] == 0: #atmosfera
                    self._matrix[y,x] = temp
            
        # self._matrix[self._h-1] = M - (self._h*self._dh) *(6.0/1000.0)
        print("### Estableciendo condiciones iniciales ### ")
        print("### Hora actual: " + str(hora) + " ### ")
        print("Temperatura Mar actual: "+ str(M))
        print("Temperatura en Fabrica: " +str(F))
        print("Temperatura Atmosfera 1000 [m]: "+ str(M - (2000) *(6.0/1000.0)))
        print("Temperatura Atmosfera 2000 [m]: "+ str(M - (1000) *(6.0/1000.0)))
        print("Temperatura en Tierra: " +str(T))
        print("Temperatura en Nieve: " +str(N))
        return 
 
    
    def _fix_plot(self):
        """
        Convierte a Nan los elementos de la geografía (cerros, fabrica, mar, nieve) ,de esta manera se puede observar de mejor la temperatura de la atmosfera
        return: none
        """
        for y in range(0,self._h):
            for x in range(1,self._w):
                if self._geografia[y,x] != 0: #No atmosfera
                    self._matrix[y,x] = None
        return 
    def plot(self):
        """
        Grafica la temperatura actual
        """

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # Se agrega grafico al plot
        cax = ax.imshow(self._matrix, interpolation='none', origin="lower")
        fig.colorbar(cax)
        plt.show()
        return


    def plot_log_scale(self):
        """
        Grafica la temperatura actual con colores en escala logaritmica 
        return: none
        """

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ymax = np.nanmax(self._matrix)
        xmax = math.log(ymax,10)
        bounds = np.hstack((np.array([-10, 0]),np.logspace(1,xmax,25, endpoint=True)))
        norm = color.BoundaryNorm(boundaries=bounds, ncolors=256)
        # Se agrega grafico al plot
        cax = ax.imshow(self._matrix, interpolation='none', origin="lower", norm =norm)
        cb = fig.colorbar(cax, norm=norm, boundaries=bounds)
        # even bounds gives a contour-like effect
        plt.show()
        return

    def show_map(self): 
        """
        Grafica la temperatura actual con colores en escala logaritmica 
        return: none
        """

        fig = plt.figure()
        ax = fig.add_subplot(111)
        #colorbar customization
        cmap = color.ListedColormap(['cyan', 'blue' ,'red', 'brown', 'white'])
        bounds = [0,1,2,3,4,5]
        norm = color.BoundaryNorm(bounds, cmap.N)
        cax = plt.imshow(self._geografia, origin="lower", interpolation='none',cmap=cmap, norm=norm )
        cb = fig.colorbar(cax,cmap=cmap, norm=norm, boundaries=bounds, ticks = [0.5,1.5,2.5,3.5,4.5])
        cb.ax.set_yticklabels(['cielo','agua' ,'fabrica', 'tierra','nieve'])
        plt.show()    
        return True
    
    def start(self, iteraciones=1000, func = rho1, e0=0.001):
        for _ in tqdm.tqdm(range(iteraciones)): #1000 iteraciones
            e = 0
            for x in range(1, self._w-1): # al iterar no se consideran las condiciones de dirichlet (bordes)
                for y in range(self._h-2, 0 ,-1):
                    
                    if self._geografia[y,x] != 0 :
                        break
                    
                    elif self._geografia[y,x] == 0:
                        self._matrix[y,x], _e  = self.faux(x,y, func)
                        e+=_e
        
            # if e < e0:
                # print("break in iteration: "+str(_))
                # break
        return
    def imprime(self):
        print(self._matrix)


    def faux(self, i,j, rho = rho1):

        uij = self._matrix[j,i]
        rij = -4*self._matrix[j,i]


        #revision si se encuentra sobre un condicion de borde ( no es posible abajo)
        if (self._geografia[j-1,i] != 0 and self._geografia[j-1,i]!=2)or np.isnan(self._matrix[j-1,i]):
    
            rij+= 2*self._matrix[j+1,i]
        
        else:
            rij+=(self._matrix[j-1,i]+self._matrix[j+1,i])

        #revision de si se encuentra a izquierda o derecha de una condicion de borde (no es posible en ambos)
        
        if self._geografia[j,i-1] !=0 or np.isnan(self._matrix[j,i-1]):
            rij+= 2*self._matrix[j,i+1]

        elif self._geografia[j,i+1] !=0 or np.isnan(self._matrix[j,i+1]):
            rij+= 2*self._matrix[j,i-1]
        
        else:
            rij+=(self._matrix[j,i-1] + self._matrix[j,i+1])

        print -rho(i*self._dh,j*self._dh)
        rij+= -rho(i*self._dh,j*self._dh)*(self._dh**2)

        uij+= self.omega*rij/4.0

        e = self._matrix[j,i] - uij

        return uij, e

    # def func(i,j, rho = self.rho1):

        #Casos Generales:

        # if self._geografia[j-1, i] !=0:

        #     if self._geografia[j,i-1] !=0:


        #     elif self._geografia[j,i+1] != 0:

        #     else:


        # elif self._geografia[j, i-1] !=0:

        # elif self._geografia[j, i+1] !=0:

        # else:
        #     aux  = self._matrix[y,x] + self.omega*(self._matrix[y-1,x] + self._matrix[y+1,x] + self._matrix[y,x+1] + self._matrix[y,x-1] - 4*self._matrix[y,x] - rho(x.y)*(self._dh**2))/4.0
