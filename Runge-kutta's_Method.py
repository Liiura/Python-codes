import numpy as np
from matplotlib import pyplot as plt
def FirstFunction():
    y=1
    x=0
    h=0.5
    xs=np.arange(0,3.1,0.05)
    ys=[y]
    sy=[1]
    fxy= lambda x,y:y*x**3-1.1*y
    gxy=lambda x: (np.exp(np.sin(x)))**2
    aa=gxy(xs)
    for s in range(0,2):
        k=fxy(x,y)
        k2=fxy((x+0.5*h),(y+0.5*h*k))
        k3=fxy((x+0.5*h),(y+0.5*h*k2))
        k4=fxy((x+h),(y+h*k3))
        y=y+(1/6)*h*(k+2*k2+2*k3+k4)
        x = x + h
        print(y)
        ys.append(y)
def SecondFunction():
    y = 1
    x = 0
    h = 0.05
    xs = np.arange(0, 3.1, 0.05)
    ys = [y]
    sy = [1]
    print(xs)
    fxy = lambda x,y: y*(10-2*y)
    gxy = lambda x:  10/(8*np.exp(-10*x)+2)
    aa = gxy(xs)
    for s in range(0,61):
        k = fxy(x, y)
        k2 = fxy((x + 0.5 * h), (y + 0.5 * h * k))
        k3 = fxy((x + 0.5 * h), (y + 0.5 * h * k2))
        k4 = fxy((x + h), (y + h * k3))
        y = y + (1 / 6) * h * (k + 2 * k2 + 2 * k3 + k4)
        x = x + h
        ys.append(y)
    print(ys)
    print(aa)
    y = 1
    x = 0
    for s in range(0, 61):
        y = y + h * fxy(x, y)
        x = x + h
        sy.append(y)

    plt.plot(xs, ys, label="Runge-kutta's method")
    plt.plot(xs, sy, "r--", label="Euler's method")
    plt.plot(xs, aa, "g--", label="Real solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()
def ThirdFunction():
    y = 1
    x = 0
    h = 0.05
    xs = np.arange(0,14.1, 0.1)
    ys = [y]
    sy = [1]
    #fxy = lambda x,y: (2*x)*y**2 #diferential equation
    #gxy = lambda x: -1/(x**2-1) #analitycal solution
    r=9.129988e-7
    fxy= lambda x,y:r*x*(232854-x)
    gxy=lambda x:232854/(1+232853*np.exp(-232854*r*x))
    aa = gxy(xs)
    print("x=", x, ", y=", y)
    for s in range(0,140):
        k = fxy(x,y)
        k2 = fxy((x + 0.5 * h), (y + 0.5 * h * k))
        k3 = fxy((x + 0.5 * h), (y + 0.5 * h * k2))
        k4 = fxy((x + h), (y + h * k3))
        y = y + (1 / 6) * h * (k + 2 * k2 + 2 * k3 + k4)
        x = x + h
        ys.append(y)
        print("x=", x, ", y=", y)
    y = 1
    x = 0
    print("x=", x, ", y=", y)
    for s in range(0,140):
        y = y + h * fxy(x, y)
        x = x + h
        sy.append(y)
        print("x=",x,", y=",y)
    plt.plot(xs, ys, label="Runge-kutta's method")
    plt.plot(xs, sy, "r--", label="Euler's method")
    plt.plot(xs, aa, "g--", label="Real solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.title("Modelo matemático del coronavirus en Envigado")
    plt.show()
def FourthFunction():
    y = 0
    x = 0
    h = 0.1
    xs = np.arange(0, 1.1, 0.1)
    ys = [y]
    fxy = lambda x, y: (2 * x) * y ** 2
    gxy = lambda x: -1 / (x ** 2 - 1)
    aa = gxy(xs)
    print("x=", x, ", y=", y)
    for s in range(0, 10):
        k = fxy(x, y)
        k2 = fxy((x + 0.5 * h), (y + 0.5 * h * k))
        k3 = fxy((x + 0.5 * h), (y + 0.5 * h * k2))
        k4 = fxy((x + h), (y + h * k3))
        y = y + (1 / 6) * h * (k + 2 * k2 + 2 * k3 + k4)
        x = x + h
        ys.append(y)
        print("x=", x, ", y=", y)
    plt.plot(xs, ys, label="Runge-kutta's method")
    plt.plot(xs, aa, "g--", label="Real solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()

FirstFunction()