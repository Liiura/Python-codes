from matplotlib import pyplot as plt
import numpy as np
import math as m
import cmath as cm
def Paratrooper(): # se define la función para el ejercicio del paracaidista
    v=0 #valor inicial de velocidad en función del tiempo
    vt= lambda t: (np.tanh(9.8*np.sqrt(0.225/(68.1*9.8))*t))/(np.sqrt(0.225/(68.1*9.8))) #solución analítica de la ecuación diferencial
    ts=np.arange(0,2,0.01) #se crea un vector que contendrá puntos de 0 a 3 con incrementos de 0.01
    aa=vt(ts) #se evalua la solución analítica y se guardan los puntos en un vector
    ms=[v] #se agrega la codición inicial para v al vector que tendrá los puntos de la solución numérica
    h=0.01 #se define el tamaño de paso
    print(ts) #Se imprimen los valor de ts
    print(aa) #se imprimen los valores de aa
    for x in range(0,199): #ciclo que controlará la aproximación numérica
        v=v+(9.8-(0.225/68.1)*v**2)*h #se crear la itenerancia de la solución numérica
        ms.append(v) #se agrega el valor calculado al vector
    plt.plot(ts,aa,label="Analytical solution") #se crean los parámetros de la gráfica de la solución analítica
    plt.plot(ts,ms,"r--",label="Numerical solution") #se crean los parámetros de la solución numérica
    plt.grid() #se agrega una malla a la gráfica
    plt.xlabel("T(s)") #se agrega una etiqueta al eje x
    plt.ylabel("v(m/s)") #se agrega una etiqueta al eje y
    plt.legend() #se agrega la leyenda que se definieron en los parámetros
    plt.title("Numerical solution vs analytical solution")
    plt.show() #se muestra la gráfica
Paratrooper()
#se llama la función
def CuadraticFunction(a,b,c):
    if(b**2-4*a*c<0):
        x1 = (-b + cm.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-cm.sqrt(b**2-4*a*c))/2*a
    else:
        x1= (-b+m.sqrt(b**2-4*a*c))/2*a
        x2=(-b-m.sqrt(b**2-4*a*c))/2*a
    return x1,x2
#a=float(input("a coeficient: "))
#b=float(input("b coeficient: "))
#c=float(input("c coeficient: "))
#s=CuadraticFunction(a,b,c)
#print(s)
def CubicFunction(a,b,c,d):
    j=b/a
    k=c/a
    l=d/a
    p=-(j**2/3)+k
    q=((2*j**3)/27)-((k*j)/3)+l
    if q**2/4 + p**3/27<0:
        a0=m.radians(-q/2)
        b0=m.radians(m.sqrt(-q**2/4 - p**3/27))
        theta=m.atan(b0/a0)
        ds=m.cos(theta/3)
        z1=2*m.sqrt(-p/3)*m.cos((theta+2*m.pi*0)/3)
        z2=2*m.sqrt(-p/3)*m.cos((theta+2*m.pi*1)/3)
        z3=2*m.sqrt(-p/3)*m.cos((theta+2*m.pi*2)/3)
        x1 = z1 - j/3
        x2 = z2 - j/3
        x3 = z3 - j/3
    elif q**2/4 + p**3/27==0:
        z1=np.cbrt((-q/2)+m.sqrt(((q**2)/4) + ((p**3)/27)))+ np.cbrt((-q/2)-m.sqrt(((q**2)/4) + ((p**3)/27)))
        z2=(-z1/2)+m.sqrt((z1/2)**2+(q/z1))
        z3 =-z1/2+m.sqrt((z1/2)**2+q/z1)
        x1=z1-j/3
        x2=z2-j/3
        x3=z3-j/3
    else:
        print(-2**(1/3))
        z1=np.cbrt(-q/2+m.sqrt((q/2)**2+(p/3)**3)) + np.cbrt(-q/2-m.sqrt((q/2)**2+(p/3)**3))
        z2=-z1/2+cm.sqrt((z1/2)**2+q/z1)
        z3 =-z1/2-cm.sqrt((z1/2)**2+q/z1)
        x1=z1-float(j)/float(3)
        x2=z2-float(j)/float(3)
        x3=z3-float(j)/float(3)
    return x1,x2,x3
#a=float(input("a coeficient"))
#b=float(input("b coeficient"))
#c=float(input("c coeficient"))
#d=float(input("d coeficient"))
#s=CubicFunction(a,b,c,d)
#print(s)
def TaylorSerie(n,x0): ##se crea la función
    cosx=1.0 ##se inicializa el coseno en 1
    x0 = m.radians(x0) #se pasa a radianes el el número enviado
    for x in range(1,n+1): ##se crea un ciclo que controlará la serie de taylor
        cosx=cosx+((-1)**x*x0**(2*x))/m.factorial(2*x) #se hace la función acumuladora
    realcosx=m.cos(x0) #se calcula "el valor del coseno a través de funciones de python"
    error=((abs(realcosx-cosx))*100)/realcosx #se calculo el error relativo porcentual
    print("valor real aproximado:",realcosx) #se imprime el valor real
    print("Valor aproximado en la serie de Taylor:",cosx) #se imprime el valor calculado con la serie
    print("Erorr relativo porcentual:",error,"%") #se muestra el error
x=float(input("Ingresa el valor de x a evaluar"))
n=int(input("ingresa valor de iteraciones"))
TaylorSerie(x,n)
