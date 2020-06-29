import math as m
import numpy as np
d = [1,1,1,1,1]
d_u = [2,2,2,2]
d_d = [3,3,3,3]
m=[]
matriz = np.diag(d) + np.diag(d_u, 1) + np.diag(d_d, -1)
print(matriz)
for i in matriz:
    print(i[0])
