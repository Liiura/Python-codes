import numpy as np
from matplotlib import pyplot as plt
# Se define una lista llamada coefi en la cual cada elemento se le define una posición de la siguiente forma [0,1,2,3,...,n] y el elemento en la posición 0,1,2,3,n es un diccionario
# Nota: Un diccionario es una estructura de datos parecida a una lista con la diferencia en que los elementos no se acceden por una posición si no por una clave, es decir que un elemento está definida por una clave y el elemento
# para acceder a los elementos del diccionario se tiene que especificar la clave de la siguiente forma: diccionario[clave]
# si se quiere agregar un elemento al diccionario entonces se tiene que hacer de la siguiente forma: diccionario{elementos_anteriores,clave:dato_a_agregar}
# dentro de cada elemento de la lista coefi existe un diccionario con la función externa y los coeficientes de la ecuación diferencial; Los coeficientes A(x),B(X),C(X) Y la función externa f(x) tienen las claves 1,2,3 y 4 respectivamente, hay que tener eso encuenta a la hora de querer acceder a los coeficientes de la EDO elegida.
# Finalmente para acceder a los coeficientes de un edo en particular tenemos que hacerlo de la siguiente manera coefi[posición_de_mi_ecuacion_en_la_lista][clave_de_mi_coeficiente_dentro_del_diccionario](parámetro_a_evaluar_en_el_coeficiente_de_la_edo)
# dentro de la funciones lambda se puede modificar las funciones al gusto de quien edite el codigo
# Nota 2: Si se va a ingresar una nueva ecuación diferencial entonces debe de ingresarse un nuevo elemento a la lista coefi
# El elemento que se vaya a agregar debe de ser un diccionario que obligatoriamente debe contener 4 datos
# Esos cuatro datos corresponde a los coeficiente A(X),B(X),C(X) y la función externa f(x)
# Cada dato del diccionario debe de contener una clave de 1 a 4, en donde la clave 1 corresponde al coeficiente A(x), la 2 al coeficiente B(x)
# Así sucesivamente hasta llegar a la clave 4 que corresponde a la función externa f(x)
coefi=[{1:lambda x: 1,2:lambda x: 0,3:lambda x: -0.01,4:lambda x: -0.2},{1:lambda x: 7,2:lambda x: -2,3:lambda x: -1,4:lambda x:-x},{1:lambda x: x**2,2:lambda x: -x,3:lambda x: -1,4:lambda x:2*x}]
# cfr es una lista que contiene en cada posición un diccionario en donde hay dos elementos con una clave, el primer elemento siempre corresponderá a la frontera izquierda y el segundo elemento corresponderá a la frontera derecha
# Nota si se quiere ingresar unas nuevas condiciones de frontera para una ecuación diferencial en específico, se debe ingresar una nueva posición en la lista
# el dato de esa posición debe de tener la misma estructura que la de la primera posición de la lista
# recordar que en una lista los datos se separan por comas
cfr=[{1:(0,40),2:(10,200)},{1:(0,5),2:(20,8)},{1:(1.962,0),2:(9.265,0)}]
funcanali=[lambda x:73.4523*np.exp(0.1*x)-53.4523*np.exp(-0.1*x)+20,lambda x:(-1.783e-4)*np.exp(((1+2*np.sqrt(2))/7)*x)+7.0001783*np.exp(((1-2*np.sqrt(2))/7)*x)+x-2,lambda x:0.03862212*np.float_power(x,(1+np.sqrt(2)))+2.33412631*np.float_power(x,(1-np.sqrt(2)))-x]
# cantidad de puntos, modificar si se necesita
n=40
def Graphs(id,ls,h):
    x=np.arange(cfr[id][1][0],cfr[id][2][0]+h,h) # se llena un vector con todos los valores de x
    print(len(x),len(ls))
    y=funcanali[id](x) # se calculan los valores de la función en los x calculados
    plt.plot(x,y,label="Solución analítica")
    plt.plot(x,ls,'r--',label="Solución numérica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.title("Solución numérica vs analítica")
    plt.show()
def finitediferencies(id):
    ai, di, bi, ci, yi = [], [], [], [], [] # se definen las listas que van a contener los coeficientes de las ecuaciones lineales
    xi = cfr[id][1][0] #se trae la coordenada x de la frontera izquierda
    h=(cfr[id][2][0]-cfr[id][1][0])/n # se calculan el número de puntos a econctrar la solución
    for i in range(0,n-1): # empieza el bucle iterador para la variable i
        xi=xi+h # se incrementa el valor de xi para evaluar en el punto xi
        for j in range(0,n-1): # empieza el bucle iterador para la variable j
            if i==j: # si en la diagonal principal
                c2 = (-2 / h ** 2) * coefi[id][1](xi) + coefi[id][3](xi) # entonces calcule el coeficiente 2
                di.append(c2) # y haga una lista con los elementos de la diganonal principal
            if i==j-1: # si se está en la diagonal que está por encima de la principal
                c3 = (1 / h ** 2) * coefi[id][1](xi) + (1 / (2 * h)) * coefi[id][2](xi) #calcula el coeficiente 3
                ci.append(c3) #y haga una lista de valores  de la diagonal que está por encima de la diagonal principal
            if i==j+1: #si se está en la diagonal que está por debajo de la principal
                c1 = (1 / h ** 2) * coefi[id][1](xi) - (1 / (2 * h)) * coefi[id][2](xi) #calcule el cofiente 1
                ai.append(c1) # y haga una lista de valores con los elementos de la diagonal que está por debajo de la diagonal pricipal
        ti=coefi[id][4](xi) #calculo de los bi
        if i==0: # se verifica si se está en la ecuación 1
            ti=ti-((1 / h ** 2) * coefi[id][1](xi) - (1 / (2 * h)) * coefi[id][2](xi))*cfr[id][1][1] #si está en la ecuación 1 entonces se despeja el termino para suma cn bi
        elif i==n-2: # se verifica si se está la última ecuación
            ti=ti-((1 / h ** 2) * coefi[id][1](xi) + (1 / (2 * h)) * coefi[id][2](xi))*cfr[id][2][1] # si están en la última ecuación despeja el termino para sumar con bi
        bi.append(ti) #Se ingresa bi a la lista
    matriz = np.diag(di) + np.diag(ci, 1) + np.diag(ai, -1) # se construye la matriz tridiagonal
    sol=np.linalg.solve(matriz,bi) # se soluciona la matriz tridiagonal
    print("Resultados con la aproximación centrada, para un error de h^2 y un tamaño de paso de h="+str(h))
    xi=cfr[id][1][0]
    print("x="+str(xi)+"  y="+str(cfr[id][2][1])) # se muestra el resultado inicial
    ynum=[cfr[id][1][1]]
    for r in sol: # se recorre el vector solución
        xi=xi+h # se calcula el x para el cual se obtiene una solución de y
        print("x="+str(xi)+"  y="+str(r))
        ynum.append(r) # se guardan los valores del vector solución en otra lista para poder gráficar
    print("x=" + str(cfr[id][2][0]) + "  y=" + str(cfr[id][2][1])) #se muestra el resultado final
    ynum.append(cfr[id][2][1])
    Graphs(id,ynum,h) # se llama a una función que grafica las dos soluciones, si no se tiene función analítica para la función escogida, comentar esta línea con #

#try:
print("Actualmente hay "+str(len(coefi))+" ecuaciones diferenciales ingresadas")
print("Las funciones están en una lista que van desde las posición 0 hasta "+str(len(coefi)-1)+", el id será esa posición en la lista")
id=int(input("Ingrese el id de la ecuación diferencial para la cual se solucionará sobre un intervalo"))
finitediferencies(id)
#except:
print("""Ha ocurrido un error al ejecutar el código, revisa si la información que ingresaste es válida""")
