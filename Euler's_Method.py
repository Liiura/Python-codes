import numpy as np
def FirstFunction():
    fx = lambda y: np.exp(-y)
    h = 0.1
    y = 0
    x0 = 0
    for x in range(0, 2):
        if x == 0:
            y = y + 0.05 * fx(y)
            print("xn=", x0, " yn=", y)
            continue
        y = y + 0.05 * fx(y)
        x0 = x0 + 0.05
        "{0:3f}".format(x0)
        print("xn=", x0, " yn=", y)
def SecondFunction():
    fxy = lambda t,y: y*t**3-1.1*y
    h = 0.5
    y=1
    x0 = 0
    for x in range(0,2):
        y=y+ h*fxy(x0,y)
        x0=x0+h
        print("xn=", x0, " yn=", y)
def ThirdFunction():
    fxy = lambda x, y: (x-y)**2
    h = 0.05
    y = 0.5
    x0 = 0
    for x in range(0,10):
        if x==0:
            y=y+h*fxy(x0,y)
            print("xn=", x0, " yn=", y)
            x0 = x0 + h
            continue
        y = y + h * fxy(x0, y)
        print("xn=", x0, " yn=", y)
        x0 = x0 + h
def FourthFunction():
    fxy = lambda x, y: x*y + np.sqrt(y)
    h = 0.05
    y = 1
    x0 = 0
    for x in range(0,10):
        if x == 0:
            y = y + h * fxy(x0, y)
            print("xn=", x0, " yn=", y)
            x0 = x0 + h
            continue
        y = y + h * fxy(x0, y)
        print("xn=", x0, " yn=", y)
        x0 = x0 + h
def FiveFunction():
    fxy = lambda x, y: x*y**2 - y/x
    h = 0.05
    y = 1
    x0 = 1
    for x in range(0,10):
        if x == 0:
            y = y + h * fxy(x0, y)
            print("xn=", x0, " yn=", y)
            x0 = x0 + h
            continue
        y = y + h * fxy(x0, y)
        print("xn=", x0, " yn=", y)
        x0 = x0 + h
def SixFunction():
    fxy = lambda x,y: y-y**2
    h = 0.1
    y = 0.5
    x0 = 0
    for x in range(0,10):
        if x == 0:
            y = y + h * fxy(x0, y)
            print("xn=", x0, " yn=", y)
            x0 = x0 + h
            continue
        y = y + h * fxy(x0, y)
        print("xn=", x0, " yn=", y)
        x0 = x0 + h

SecondFunction()




