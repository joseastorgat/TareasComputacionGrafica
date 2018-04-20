# coding=utf-8

"""Tarea 1
@author José
"""
from litoral import Litoral, rho1,rho2


def test():
    lit = Litoral(ancho=4000, alto=2000, dh = 20, RRR=103, omega = 1)
    lit.get_omega_optimo()
    lit.set_geografia()
    lit.cb()
    #plot condiciones iniciales
    lit.plot()

    lit.start(200)

    #plot
    lit._fix_plot()
    lit.plot()
    lit.plot_log_scale()
    return lit

def test2():
    lit = Litoral(ancho=4000, alto=2000, dh = 20, RRR=103, omega = 1)
    lit.get_omega_optimo()
    lit.set_geografia()
    lit.cb()
    #plot condiciones iniciales
    lit.plot()

    lit.start(200,func=rho2)

    #plot
    lit._fix_plot()
    lit.plot()
    lit.plot_log_scale()
    return lit


def main():
    # Instancia rio
    return 



if __name__ == '__main__':
    test() 