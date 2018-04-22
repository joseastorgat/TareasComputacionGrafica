# coding=utf-8

"""Tarea 1
@author José
"""
from litoral import Litoral, rho1,rho2, get_omega_optimo
import numpy as np
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color  # grafico

def test_omega():

    return

def test_it_and_times():
    return


def explorar_horas():
    horas = [0.0,8.0,12.0,16.0,20.0]

def explorar_horas():

    #parametros:

    dh=25
    scale=0.01
    rrr=103
    rho = rho1
    horas = [0,8,12,16,20]
    
    iteraciones=5000
    epsilon=0.001    
 
    lit = Litoral(dh,rrr,scale)

    ome_opt = get_omega_optimo(lit._h, lit._w)

    its =[]
    times =[]
    est = []

    for hora in horas:

        lit.reset()
        lit.cb(hora)
        it, time = lit.start(max_iteraciones=iteraciones,func=rho,e0=epsilon, omega = ome_opt)        
        its.append(it)
        times.append(time)
        lit.plot_log_scale(save=True)
        lit.plot(save=True)
        est.append(lit.estadisticas())
        lit.plot_log_scale(save=True)
        lit.plot(save=True)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    graph = plt.plot(omegas, times, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Tiempo [s]')
    plt.title(r'Tiempo de Ejecucion $\epsilon = 0.001$')

    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    graph = plt.plot(omegas, its, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Iteraciones')
    plt.title(r'Numero de iteraciones $\epsilon = 0.001$')
 
    plt.show()
        

    return its, times, est, lit

def explorar_omegas(hora=0):

    #parametros:
    dh=40
    scale=0.01
    rrr=103
    rho = rho1
    iteraciones=2000
    epsilon=0
    lit = Litoral(dh=dh, RRR=rrr,scale=scale)

    ome_opt = get_omega_optimo(lit._h, lit._w)
    omegas = np.linspace(1,2,4,endpoint=False)

    omegas = np.append(omegas, [ome_opt])
    its =[]
    times =[]
    est = []

    for omega in omegas:
        lit.cb(hora)
        it, time = lit.start(max_iteraciones=iteraciones,func=rho,e0=epsilon, omega = omega)        
        its.append(it)
        times.append(time)
        est.append(lit.estadisticas())
        lit.plot_log_scale(save=True)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    graph = plt.plot(omegas, times, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Tiempo [s]')
    plt.title('Tiempo de Ejecucion para {0} iteraciones sobre Litoral'.format(iteraciones))
    plt.show()

    return its, times, est, lit

def explorar_omegas2(hora=0):

    #parametros:
    dh=40
    scale=0.01
    rrr=103
    rho = rho1
    iteraciones=0
    epsilon=0.01
    lit = Litoral(dh=dh, RRR=rrr,scale=scale)

    ome_opt = get_omega_optimo(lit._h, lit._w)
    omegas = np.linspace(1,2,4,endpoint=False)

    omegas = np.append(omegas, [ome_opt])
    its =[]
    times =[]
    est = []

    print omegas
    for omega in omegas:
        lit.cb(hora)
        it, time = lit.start(max_iteraciones=iteraciones,func=rho,e0=epsilon, omega = omega)        
        its.append(it)
        times.append(time)
        est.append(lit.estadisticas())
        lit.plot_log_scale(save=True)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    graph = plt.plot(omegas, times, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Tiempo [s]')
    plt.title(r'Tiempo de Ejecucion $\epsilon = 0.001$')

    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    graph = plt.plot(omegas, its, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Iteraciones')
    plt.title(r'Numero de iteraciones $\epsilon = 0.001$')
 
    plt.show()

    return its, times, est, lit


def main():
    # Instancia rio


    print(" ### Estudio Temperaturas en Litoral ### ")
    
    grilla  = input("Tamaño de diferencial (metros) : ")
    rrr = input("Geografía (rrr): ")
    
    lit = Litoral(dh=grilla, RRR=rrr, omega=omega)
    
    if omega ==0:
        lit.get_omega_optimo()

    omega = input("omega ( 0: omega optimo) : " )
    if omega<1 and omega>2 and omega!=0:
        print("Omega debe ser un valor entre 1 y 2 (o 0 si se desea usar óptimo)")
        omega = input("omega \n ( 0: omega optimo)" )
    
    lit.set_geografia()
    lit.show_map()
    hora = input("¿Que hora es? : " )
    lit.cb()
    
    _rho = input("rho function: (1: rho=0 -- 2:rho= 1/sqrt(y**2 + x**2 + 120 ) ) : " )

    if _rho == 1:
        rho = rho1
    else:
        rho = rho2
    
    max_it = input("Maximo numero de Iteraciones (0 no max): ")
    e0 = input("e0 : " )

    lit.start(max_it,func = rho , e0=e0)

    # lit._fix_plot()
    lit.plot()
    lit.plot_log_scale()
 

    return lit



if __name__ == '__main__':
    main() 