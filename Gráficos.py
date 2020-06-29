from matplotlib import pyplot as plt
import numpy as np
def Newton():
    xs=np.arange(0,40,1)
    o2=lambda x:8.418-0.1391*(x-24)+(271/160000)*(x-24)*(x-32)
    o3=lambda x:9.870-0.1815*(x-16)+(53/20000)*(x-16)*(27-24)-(51/1280000)*(x-16)*(x-24)*(x-32)
    o4=lambda x:11.843-0.247*(x-8)+(131/32000)*(x-8)*(x-16)-(77/1280000)*(x-8)*(x-16)*(x-24)*(x-32)
    o5=lambda x:14.621-0.347*(x-0)+(1/100)*(x-0)*(x-8)-(23/256000)*(x-0)*(x-8)*(x-16)*(x-24)+(2.62e-3)*(x-0)*(x-16)*(x-24)+(-6.71e-7)*(x-0)*(x-8)*(x-16)*(x-24)*(x-32)
    y2=o2(xs)
    y3=o3(xs)
    y4=o4(xs)
    y5=o5(xs)
    plt.plot(xs,y2,'r--',label='polinomio newton grado 2')
    plt.plot(xs,y3,label='polinomio newton grado 3')
    plt.plot(xs,y4,label='polinomio newton grado 4')
    plt.plot(xs,y5,label='polinomio newton grado 5')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráficos de polinomios de newton")
    plt.grid()
    plt.legend()
    plt.savefig('gráfica_newton.png')
    plt.show()
def Lineal():
    xs = np.arange(0, 30, 1)
    o1=lambda x: 11.766-0.1395*x
    y=o1(xs)
    plt.plot(xs,y,'r--',label='interpolación')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de interpolación lineal")
    plt.grid()
    plt.legend()
    plt.savefig('gráfica_lineal.png')
    plt.show()
def Lagrange():
    xs = np.arange(0, 30, 1)
    x0=0
    x1=8
    x2=16
    x3=24
    x4=32
    x5=40
    y0=14.621
    y1=11.843
    y2=9.870
    y3=8.418
    y4=7.302
    y5=6.413
    F0=lambda x:((((x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x5)))/((x0-x1)*(x0-x2)*(x0-x3)*(x0-x4)*(x0-x5)))*y0
    F1=lambda x:((((x-x0)*(x-x2)*(x-x3)*(x-x4)*(x-x5)))/((x1-x0)*(x1-x2)*(x1-x3)*(x1-x4)*(x1-x5)))*y1
    F2=lambda x:((((x-x0)*(x-x1)*(x-x3)*(x-x4)*(x-x5)))/((x2-x0)*(x2-x1)*(x2-x3)*(x2-x4)*(x2-x5)))*y2
    F3=lambda x:((((x-x0)*(x-x1)*(x-x2)*(x-x4)*(x-x5)))/((x3-x0)*(x3-x1)*(x3-x2)*(x3-x4)*(x3-x5)))*y3
    F4=lambda x:((((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x5)))/((x4-x0)*(x4-x1)*(x4-x2)*(x4-x3)*(x4-x5)))*y4
    F5=lambda x:((((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x4)))/((x5-x0)*(x5-x1)*(x5-x2)*(x5-x3)*(x5-x4)))*y5
    F=F0(xs)+F1(xs)+F2(xs)+F3(xs)+F4(xs)+F5(xs)
    plt.plot(xs,F,'r--',label='Polinomio de grado 5')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de polinomio de Lagrange")
    plt.grid()
    plt.legend()
    plt.savefig('gráfica_lagrange.png')
    plt.show()
Newton()
Lineal()
Lagrange()
