# coding=utf-8

"""Tarea 1
@author José
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color  # grafico
import time
import numpy as np
import math
import sys

def rho1(i,j):
    return 0

def rho2(i,j,):
    return 1.0/(math.sqrt(( float(i)**2+ float(j)**2 + 120.0 )))

class Litoral:
        #medidas litoral
    def __init__(self, dh = 20, RRR=103, scale = 0.025):
        """
        Constructor
        :param ancho: Ancho
        :param alto: alto
        :param dh: Tamaño grilla diferencial
        :type ancho: int,float
        """
        #medidas del litoral        
        self._ancho = 4000  # privada
        self._alto = 2000
        #geografia
        self._RRR= RRR
        #grilla diferencial
        self.scale = scale

        self.__dh=dh
        self._dh = dh*self.scale
        self._h = int((float(self._alto) / self._dh)*self.scale)
        self._w = int((float(self._ancho) / self._dh)*self.scale)
        
        self._rrr = RRR/1000.0

        self._geografia = np.zeros((self._h, self._w))
        self._matrix = np.zeros((self._h, self._w))

        self.hora=0
        self.last_omega=0

        print("### Litoral ### ")
        print("Diferencial: {0} [m]".format(dh))
        print("H: {0}".format(self._dh))
        print("Ancho Matriz: {0}".format(self._w))
        print("Alto Matriz: {0}".format(self._h))
        print("RRR: {0}".format(RRR))
        print("### ### ### ")

        self.set_geografia()

    def reset(self):
        self.__init__(self.__dh,self._RRR, self.scale)


    def set_geografia(self):
        """
        Construye la geografia del Litoral
        :return:
        """
        _p1 = ( (1200.0 + 400.0*self._rrr), 0)#comienzo de playa y fabrica
        _p2 = ( _p1[0] + 120.0, 0) # fin playa y fabrica, comienzo elevación
        _p3 = ( _p1[0] + 400.0, (_p1[0] + 400.0 -_p2[0])*(100.0/300.0)) # fin elevacion suave, comienzo montaña 1
        _p4 = ( _p3[0] + 800.0, (1500.0 + 200.0*self._rrr)) # pico montaña 1
        _p5 = ( _p4[0] + 300.0, (1300.0 + 200.0*self._rrr)) # valle entre montañas
        _p6 = ( _p4[0] + 800.0, (1850.0 + 100.0*self._rrr)) # pico montaña 2

        p1 = (int(_p1[0]*self.scale/self._dh), int(_p1[1]*self.scale/self._dh))
        p2 = (int(_p2[0]*self.scale/self._dh), int(_p2[1]*self.scale/self._dh))
        p3 = (int(_p3[0]*self.scale/self._dh), int(_p3[1]*self.scale/self._dh))
        p4 = (int(_p4[0]*self.scale/self._dh), int(_p4[1]*self.scale/self._dh))
        p5 = (int(_p5[0]*self.scale/self._dh), int(_p5[1]*self.scale/self._dh))
        p6 = (int(_p6[0]*self.scale/self._dh), int(_p6[1]*self.scale/self._dh))
        p7 = (self._w - 1 , int(self._h/2))

        snow = int(1800.0*self.scale/self._dh) # altura de nieve > 1800
        fab_h = int(math.ceil(20.0*self.scale/self._dh)) #altura de la fabrica es 20m

        self.puntos = {"p1" : p1, "p2" : p2, "p3" : p3, "p4" : p4, "p5" : p5, "p6" : p6, "p7" : p7} 
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

        print("### Estableciendo condiciones iniciales ### ")
        print("### Hora actual: " + str(hora) + " ### ")
        self.hora = hora

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

        print("Temperatura Mar actual: "+ str(M))

        self.cb_general(M)
        self.cb_atmosfera(M)

        print("Temperatura Atmosfera 1000 [m]: "+ str(M - (1000) *(6.0/1000.0)))
        print("Temperatura Atmosfera 2000 [m]: "+ str(M - (2000) *(6.0/1000.0)))
        return 
 
    

    def cb_general(self, M):

        #Tierra:
        T = 20.0
        #Nievesss
        N = 0.0
        #Fabrica
        F = 450*(math.cos((math.pi/12)*self.hora)+2)

        self.emision = F

        for y in range(0,self._h):
            for x in range(0,self._w):
                if self._geografia[y,x] == 1: #Mar
                    self._matrix[y,x] = M
                
                elif self._geografia[y,x] == 2: #Fabrica
                    self._matrix[y,x] = F
                
                elif self._geografia[y,x] == 3: #Tierra
                    self._matrix[y,x] = T
                
                elif self._geografia[y,x] == 4: #Nieve
                    self._matrix[y,x] = N

        print("Temperatura en Fabrica: " +str(F))
        print("Temperatura en Tierra: " +str(T))
        print("Temperatura en Nieve: " +str(N))
        return 


    def cb_atmosfera(self, M ):

        for y in range(0,self._h):
            temp = M - (6.0/1000.0)*(y*self._dh/self.scale)
            for x in range(0,self._w):
                if self._geografia[y,x] == 0: #atmosfera
                    self._matrix[y,x] = temp
        return

    def geografia_to_nan(self):
        """
        Convierte a Nan los elementos de la geografía (cerros, fabrica, mar, nieve) ,de esta manera se puede observar de mejor la temperatura de la atmosfera
        return: none
        """
        for y in range(0,self._h):
            for x in range(1,self._w):
                if self._geografia[y,x] != 0: #No atmosfera
                    self._matrix[y,x] = None
        return 
    

    def start(self, max_iteraciones=3000, func = rho1, e0=0.001, omega = 1):
        """
        Grafica la temperatura actual con colores en escala logaritmica 
        return: none
        """
        self.last_omega = omega
        if max_iteraciones ==0 and e0 ==0:
            print "Error: Debe haber una cantidad máxima de iteraciones o un e0>0 !!"
        print('##### Inicio de Iteraciones ##### \n##### e0 : {0} -- omega:{1} -- iteraciones maximas : {2}  ######'.format(e0, omega, max_iteraciones))
        print('')
        
        cont = 0

        init = time.time()

        while True: #1000 iteraciones
            e = 0
            for x in range(1, self._w-1): # al iterar no se consideran las condiciones de dirichlet (bordes)
                for y in range(self._h-2, 0 ,-1):
                    
                    if self._geografia[y,x] != 0 :
                        break
                    
                    elif self._geografia[y,x] == 0:
                        
                        # a1,e1 = self.faux(x,y,func)
                        a2,e2 = self.faux2(x,y,func, omega)
                        
                        self._matrix[y,x], _e  = a2,e2
                        e = max(e,_e)
            cont+=1        
            
            if cont%10==0:    
                sys.stdout.write("\033[F") #back to previous line
                sys.stdout.write("\033[K") #clear line
                print("Iteracion N°: {0} - Error Max: {1}".format(cont,e))
            
            if e < e0:
                fin = time.time()-init
                print('### Fin Iteraciones -- Numero de iteraciones: {0} -- Tiempo de ejecución: {1}'.format(cont,fin))
                
                return cont, fin

            if cont > max_iteraciones and max_iteraciones!=0:
                fin = time.time()-init
                print('### Fin Iteraciones -- SIN CONVERGER en  {0} iteraciones -- Tiempo de ejecución: {1}'.format(max_iteraciones,fin))
                print e
                return cont, fin


    # def faux(self, i,j, rho = rho1):

    #     uij = self._matrix[j,i]
    #     rij = -4*self._matrix[j,i]
        
    #     #revision si se encuentra sobre un condicion de borde ( no es posible abajo)
    #     if (self._geografia[j-1,i] != 0) :
    #         rij+= 2*self._matrix[j+1,i]
    #         if self._geografia[j-1,i]==2:
    #             rij+= 2*self.emision*(self._dh)**2
    #     else:
    #         rij+=(self._matrix[j-1,i]+self._matrix[j+1,i])

    #     #revision de si se encuentra a izquierda o derecha de una condicion de borde (no es posible en ambos)
    #     if self._geografia[j,i-1] !=0 :
    #         rij+= 2*self._matrix[j,i+1]

    #     elif self._geografia[j,i+1] !=0 :
    #         rij+= 2*self._matrix[j,i-1]
        
    #     else:
    #         rij+=(self._matrix[j,i-1] + self._matrix[j,i+1])

    #     # print -rho(i*self._dh,j*self._dh)
    #     rij+= -rho(i*self._dh/self.scale,j*self._dh/self.scale)*(self._dh**2)

    #     uij+= self.omega*rij/4.0
    #     e = abs(self._matrix[j,i] - uij)
    #     return uij, e
    

    def faux2(self, i,j, rho = rho1, omega=1):


        if (self._geografia[j-1,i] != 0):

            if self._geografia[j-1,i] == 2:

                rij = 2.0 * self._matrix[j+1,i] + self._matrix[j,i-1] + self._matrix[j,i+1]  - 4.0*self._matrix[j,i] + (2.0*self.emision)*(self._dh)**2

            elif (self._geografia[j,i-1] != 0):

                rij = 2.0 * self._matrix[j+1,i] + 2.0*self._matrix[j,i+1] - 4.0*self._matrix[j,i]   


            elif (self._geografia[j,i+1] != 0):
                rij = 2.0 * self._matrix[j+1,i] + 2.0*self._matrix[j,i-1] - 4.0*self._matrix[j,i]   

            else:
                rij = 2.0 * self._matrix[j+1,i] + self._matrix[j,i-1] + self._matrix[j,i+1]  - 4.0*self._matrix[j,i]  

        elif (self._geografia[j,i-1] != 0):
            rij = self._matrix[j+1,i] + 2.0*self._matrix[j,i+1] + self._matrix[j-1,i]  - 4.0*self._matrix[j,i]  
        
        elif (self._geografia[j,i+1] != 0):
            rij = self._matrix[j+1,i] + 2.0*self._matrix[j,i-1] + self._matrix[j-1,i]  - 4.0*self._matrix[j,i]  

        else:
            rij = self._matrix[j+1,i] + self._matrix[j-1,i] + self._matrix[j,i+1] + self._matrix[j,i-1] - 4.0*self._matrix[j,i]  

        
        rij = rij - rho(i*self._dh/self.scale, j*self._dh/self.scale)*(self._dh)**2.0
        uij=  self._matrix[j,i] + omega*rij*0.25
        e = abs(self._matrix[j,i] - uij)
        return uij, e

    def plot(self, save = False):
        """
        Grafica la temperatura actual
        """

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # Se agrega grafico al plot
        cax = ax.imshow(self._matrix, interpolation='none', origin="lower")
        fig.colorbar(cax)

        hora = hora_string(self.hora)
        plt.title('Temperatura a las {0} horas'.format(hora))
        self._fix_axes_sticks(ax)

        if save:
            fig.savefig('images/lintemp_'+str(self.hora)+'_'+str(self.last_omega)+'.png', bbox_inches='tight')
            plt.close(fig)
        else:
            plt.show()
        return

    def plot_log_scale(self, save=False):
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
 
        hora = hora_string(self.hora)
        plt.title('Temperatura a las {0} horas (escala logaritmica)'.format(hora))

        self._fix_axes_sticks(ax)

        if save:
            fig.savefig('images/logtemp_'+str(self.hora)+'_'+str(self.last_omega)+'.png', bbox_inches='tight')        
            plt.close(fig)

        else:
            plt.show()
        return

    def show_map(self, points=True): 
        """
        Grafica un mapa del litoral
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

        plt.title('Mapa del Litoral')
        
        if points:
            for key,value in self.puntos.iteritems():
                plt.text(value[0], value[1], key.upper(), fontsize=12, color='blue', horizontalalignment='center' )

        self._fix_axes_sticks(ax)
        plt.show()    
        return 


    def estadisticas(self):

        _min1 = np.min(self._matrix)
        _max1 = np.max(self._matrix)
        _mean1 = np.mean(self._matrix)
        return [_min1, _max1, _mean1]
    
    def imprime(self):
        print(self._matrix)

    def _fix_axes_sticks(self, ax):

        xnum = len(ax.get_xticks()) - 2
        ynum = len(ax.get_yticks()) - 2
        xlabel = []
        ylabel = []
        
        for i in range(xnum): xlabel.append(str((float(i*self._ancho/(xnum*1000.0)))))
        for j in range(ynum,-1,-1): ylabel.append(str((float(j*self._alto/(xnum*1000.0)))))
        
        ylabel.reverse()        
        ax.set_xticklabels([''] + xlabel)
        plt.xlabel("Ancho [km]")
        ax.set_yticklabels([''] + ylabel)
        plt.ylabel("Altura [km]")
        return


def hora_string(hr):
    hora = int(hr)
    if hora<10:
        hora = "0"+str(hora)
    else:
        hora = str(hora)

    minutos = int((hr%1)*60)
    if minutos<10:
        minutos = "0"+str(minutos)
    else:
        minutos=str(minutos)

    return hora + ":" + minutos

def get_omega_optimo(m, n):
    a = 2.0 + math.sqrt( 4.0 - (math.cos(math.pi/(n-1.0)) + math.cos(math.pi/(m-1.0)))**2)      
    omega = 4.0/a
    print("Omega óptimo: "+str(omega))
    return omega
