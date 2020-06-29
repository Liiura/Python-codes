from matplotlib import pyplot as plt
from sympy import *
import numpy as np
import math
gx=lambda x: np.cos(x)
fx=lambda x: np.sin(x)
x=np.linspace(0,10,100)
aa=fx(x)
bb=gx(x)
plt.plot(x,aa,'r--',label="seno")
plt.plot(x,bb,label="coseno")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Función seno")
plt.grid()
plt.legend()
plt.savefig('gráfica_python.png')
plt.show()
