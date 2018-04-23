# coding=utf-8

"""Tarea 1
@author José
"""
from litoral import Litoral, rho1,rho2, get_omega_optimo, temp_chimenea, temp_mar
import numpy as np
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color  # grafico

def test_horas():

    #parametros:
    dh=25
    scale=0.01
    rrr=103
    rho = rho1
    # horas = [0,8,12,16,20]
    horas = np.linspace(0,24,25,endpoint=True)
    iteraciones=5000
    epsilon=0.001    
 
    lit = Litoral(dh,rrr,scale)
    ome_opt = get_omega_optimo(lit._h, lit._w)

    its =[]
    times =[]
    est = []
    lit.show_map()
    for hora in horas:
        lit.cb(hora)

        it, time = lit.start(max_iteraciones=iteraciones, func=rho, e0=epsilon, omega = ome_opt)        
        its.append(it)
        times.append(time)
        est.append(lit.estadisticas())
        lit.geografia_to_nan()
        lit.plot_log_scale(save=True)
        lit.plot(save=True)
        
    fig = plt.figure()
    graph = plt.plot(horas, times, color='red', marker='o', linestyle='-', linewidth=2, markersize=12,)
    plt.xlabel(' Hora del Dia [hr] ')
    plt.ylabel('Tiempo [s]')
    plt.title(r'Tiempo de Ejecucion $\epsilon = 0.001 $ ')

    fig2 = plt.figure()
    graph = plt.plot(horas, its, color='red', marker='o', linestyle='-', linewidth=2, markersize=12,)
    plt.xlabel('Hora del Dia [hr]')
    plt.ylabel('Iteraciones')
    plt.title(r'Numero de iteraciones $\epsilon = 0.001$')

    fig3 = plt.figure()
    ax = fig3.add_subplot(111)
    temps_min =[]
    temps_max =[]
    temps_mean =[]
    for i in est:
        temps_min.append(i[0])
        temps_max.append(i[1])
        temps_mean.append(i[2])

    plt.plot(horas, temps_min, color='blue', linestyle='-', linewidth=4, label="T Minima")
    plt.plot(horas, temps_mean, color='green', linestyle='-', linewidth=4, label="T Maxima")
    plt.plot(horas, temps_max, color='red', linestyle='-', linewidth=4, label="T Promedio")

    ax.set_yscale('symlog')
    plt.xlabel(' Hora del Dia [hr] ')
    plt.ylabel( r'Temperatura [ $^{\circ}$ C ]')
    plt.title("Temperatura Max - Min - Promedio para diferentes horas")
    plt.legend()
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)    
    plt.show()
    return its, times, est, lit

def test_omegas(hora=0):

    #parametros:
    dh=25
    scale=0.01
    rrr=103
    rho = rho1
    iteraciones=1000
    epsilon=0
    lit = Litoral(dh=dh, RRR=rrr,scale=scale)

    ome_opt = get_omega_optimo(lit._h, lit._w)
    print ome_opt
    omegas = np.linspace(1,2,8,endpoint=False)

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
    graph = plt.plot(omegas, times, color='red', marker='o', linestyle='-', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Tiempo [s]')
    plt.title('Tiempo de Ejecucion para {0} iteraciones sobre Litoral'.format(iteraciones))
    plt.show()

    return its, times, est, lit

def test_omegas2(hora=0):

    #parametros:
    dh=25
    scale=0.01
    rrr=103
    rho = rho1
    iteraciones=0
    epsilon=0.001
    lit = Litoral(dh=dh, RRR=rrr,scale=scale)

    ome_opt = get_omega_optimo(lit._h, lit._w)

    omegas = np.linspace(1,2,8,endpoint=False)

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
    graph = plt.plot(omegas, times, color='red', marker='o', linestyle='-', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Tiempo [s]')
    plt.title(r'Tiempo de Ejecucion $\epsilon = 0.001$')

    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    graph = plt.plot(omegas, its, color='red', marker='o', linestyle='-', linewidth=2, markersize=12,)
    plt.xlabel(r'$ \omega $')
    plt.ylabel('Iteraciones')
    plt.title(r'Numero de iteraciones $\epsilon = 0.001$')
    plt.show()

    return its, times, est, lit


def plot_temps():
    horas = np.linspace(0,24,49,endpoint=True)
    temps1 =[]
    temps2 = []
    title1= ' Temperatura de las chimeneas a diferentes horas'
    title2 =' Temperatura del mar diferentes horas'

    for hora in horas:
        temps1.append( temp_chimenea(hora))
        temps2.append( temp_mar(hora))
    
    xlabel = 'Hora del Dia '
    ylabel = r'Temperatura [ $^{\circ}$ C ]'

    fig1 = plt.figure()
    __plot_temps(fig1, horas, temps1, xlabel, ylabel, title1)
    fig2 = plt.figure()
    __plot_temps(fig2, horas, temps2, xlabel, ylabel, title2)

def __plot_temps(fig, horas, temps, xlabel="", ylabel="", title="", label=""):
    graph = plt.plot(horas, temps, color='red', linestyle='-', linewidth=4, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


def main():
    # Instancia rio
    print(" ### Estudio Temperaturas en Litoral ### ")
    grilla  = input("Tamaño de diferencial (metros) : ")
    rrr = input("Geografía (rrr): ")
    scale = input("Escala:  ")

    lit = Litoral(dh=grilla, RRR=rrr, scale=scale)
    omega = input("omega ( 0: omega optimo) : " )

    if omega ==0:
        omega = get_omega_optimo(lit._w, lit._h)

    if omega<1 and omega>2 and omega!=0:
        print("Omega = {0} no válido, usaremos omega óptimo")
        omega = get_omega_optimo()
    
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

    lit.start(max_it,func = rho , e0=e0, omega=omega)

    # lit._fix_plot()
    lit.plot()
    lit.plot_log_scale()
    return lit

if __name__ == '__main__':
    main() 