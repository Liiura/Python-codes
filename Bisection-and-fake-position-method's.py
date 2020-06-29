import math as m
import numpy as np
from matplotlib import pyplot as plt
#nota si se quiere agregar una función debe ingresarse de la misma manera en la que están ingresadas las demás funciones, al lado de los vectores o diccionarios se explica a qué corresponde esa estructura de datos
#2nota Los diccionarios de diferencial por abri y cerrar así {}, para ellos hay que tener en cuenta la clave, es por ello que la clave de una función en específico de un diccionario debe de ser la misma que en la de los otros diccionarios
#3nota en el vector list2 es recomendable ingresar la función de la manera en que están las otras para que se pueda ver por pantalla la función a elegir
y1=lambda x:-2*x**6-1.5*x**4+10*x+2
list={'1':lambda x:x**3-3*x+1,'2': lambda x:x**3-2*np.sin(x),'3':lambda x:x**2 - 7,'4':lambda x:x**4 -20,'5':lambda x:x**10 -1,'6':lambda x: m.exp(x)-3*x,'7':lambda x:x**2-x-2,'8':lambda x:m.exp(x)+x**3,'9':lambda x:-12*x**5-6*x**3+10} #Listado de funciones disponibles en el código
list2=["1. x^3-3x+1 Recomendada para punto fijo","2. x^3-2sen(x)","3. 7^(1/2)","4. 20^(1/4)","5. x^10 - 1",'6. e^x - 3x  recomendada para punto fijo','7.x^2-x-2 recomendada para punto fijo','8. e^-x -x recomendada para punto fijo','9.-2*x^6-1.5*x^4+10*x+2 recomendada para punto fijo '] #Listado de funciones que se muestran por pantalla
deria={'1':lambda x:3*x**2-3,'2':lambda x:3*x**2-2*np.cos(x),'3':lambda x:2*x,'4':lambda x:4*x**3,'5':lambda x:10*x**9,'6':lambda x:m.exp(x)-3,'7':lambda x:2*x-1,'8':lambda x:-m.exp(x)+3*x**2,'9':lambda x:-60*x**4-18*x**2} #derivadas analíticas para el método de newton
derin={'1':(0.3,0),'2':(-1.5,1),'3':(2.23,1.9),'4':(2,1.7),'5':(0.5,0),'6':(1,1.1),'7':(1.5,0.9),'8':(-1,1),'9':(1,0)}#aproximaciones xn y xn-1 para el método de la sectante
ini={'1':0,'2':-1.5,'3':2.23,'4':2,'5':0.5,'6':1,'7':1.5,'8':0.5,'9':1} #aproximaciones iniciales para el método de newton
fp={'1':lambda x: (3/x)-(1/x**2),'6':lambda x:m.exp(x)/3,'7':lambda x:1+2/x,'8':lambda x:-m.exp(x)/(x**2),'9':lambda x: (10/(12*x**4))-(6/(12*x))} #función g(x) para hacer las iteraciones de punto fijo
fpini={'1':1.9,'6':0.5,'7':1,'8':-0.71,'9':1} #aproximaciones iniciales de las funciones para el método de punto fijo
inter={'1':(0,1),'2':(-1.5,-1),'3':(2,3),'4':(1,3),'5':(0,1.3),'6':(1,2),'7':(1.5,2.5),'8':(-1,0.5),'9':(0,1)} #intervalos para los métodos cerrados
def BisectionMethod(num):
    i=inter[num]
    a=i[0]
    b=i[1]
    rs=[]
    rs1=[]
    t = True
    veri = True
    iter = 0
    tole = 0.001  # tolerancia
    r0an = 0
    r0 = 0
    if list[num](a)*list[num](b)<0:
        n = m.ceil((m.log10(b - a) - m.log10(2 *tole)) / m.log10(2))
        while t:
            r0an = r0
            r0=(a+b)/2
            if list[num](a)*list[num](r0)<0:
                b=r0
            else:
                a=r0
            err = abs((r0 - r0an) / r0)*100
            if err <= tole:
                t = False
            elif iter >= n+20:
                print("Se ha alcanzado el número máximo de iteraciones y el método no pudo converger")
                t = False
                veri = False
            iter = iter + 1
            if num == '8':
                errt = abs((0.56714329 - r0) / 0.56714329)*100
                rs.append(iter)
                rs1.append(err)
        if veri and num == '9':
            print("""Método Utilizado:Bisección
            Intervalo de solución x0=""",i, """
            Tolerancia:""", tole, """
            Número de iteraciones realizadas:""", iter, """
            Valor aproximado de la coordenada x del punto máximo:""", r0, """
            punto máximo:""",r0, """,""", y1(r0), """
            Error aproximado porcentual:""", err * 100)  # se imprimen los resultados
        elif veri:
            print("""Método Utilizado:Bisección
            Intervalo de solución:""",i,"""
            Tolerancia:""",tole,"""
            Número de iteraciones realizadas:""",iter,"""
            iteraciones calculadas según la tolerancia ingresada:""",n+1,"""
            Valor aproximado de la raiz:""",r0,"""
            Error aproximado porcentual:""",err*100)#se imprimen los resultados
            if num=='8':
                return rs,rs1
    else:
        print("The function has not sign change")
        return  "null"
def FakePosition(num):
    i = inter[num]
    a = i[0]
    b = i[1]
    rs = []
    rs0=[]
    t=True
    veri=True
    iter=0
    tole=0.001 #tolerancia
    r0an=0
    r0=0
    if list[num](a) * list[num](b) < 0:
        n = m.ceil((m.log10(b - a) - m.log10(2 *tole)) / m.log10(2))
        while t:
            r0an=r0
            r0 = (a*list[num](b)-b*list[num](a))/(list[num](b)-list[num](a))
            if list[num](a) * list[num](r0) < 0:
                b = r0
            else:
                a = r0
            err = abs((r0 - r0an) / r0)*100
            if err <= tole:
                t = False
            elif iter >= n+5:
                print("Se ha alcanzado el número máximo de iteraciones y el método no pudo converger")
                t = False
                veri = False

            iter = iter + 1
            if num == '8':
                errt = abs((0 - r0) / 0.56714329)*100
                rs.append(iter)
                rs0.append(err)
        if veri and num == '9':
            print("""Método Utilizado:Falsa posicion
            Intervalo de solución x0=""", i, """
            Tolerancia:""", tole, """
            Número de iteraciones realizadas:""", iter, """
            Valor aproximado de la coordenada x del punto máximo:""",r0, """
            punto máximo:""", r0, """,""", y1(r0), """
            Error aproximado porcentual:""", err * 100)  # se imprimen los resultados
        elif veri:
            print("""Método Utilizado:Falsa posición
            Intervalo de solución:""",i,"""
            Tolerancia:""",tole,"""
            Número de iteraciones realizadas:""",iter,"""
            iteraciones calculadas según la tolerancia ingresada:""",n+1,"""
            Valor aproximado de la raiz:""",r0,"""
            Error aproximado porcentual:""",err*100)#se imprimen los resultados
            if num=='8':
                return rs,rs0
    else:
        print("The function has not sign change")
def FakePosition2(num): #llega como parámetro la función a trabajar
    i = inter[num]  #se obtiene el intervalo en donde se va a trabajar
    a = i[0]  #se obtiene el extremo izquierdo del intérvalo
    b = i[1]  #se obtiene el extremo derecho del intérval
    rs = []
    t=True
    veri=True
    iter=0
    tole=0.001 #tolerancia
    F=list[num](a) #se evalua la función en el extremo izquierdo
    G=list[num](b)#se evalua la función en el extremo derecho
    r0an=0
    r0=0
    if list[num](a) * list[num](b) < 0: #verifica si hay cambio de signo
        n = m.ceil((m.log10(b - a) - m.log10(2 * tole)) / m.log10(2)) #calcula el número de iteraciones
        while t: #inicia el bucle
            r0an=r0
            r0 = (a*G-b*F)/(G-F) #calcula la aproximación
            if list[num](a) * list[num](r0) < 0: #evalua si hay cambio de signo
                b = r0 #asigna la aproximación al valor derecho del intervalo
                if F*list[num](r0)>0: #evalua si es positivo el producto para verificar si se divide entre dos la función evaluada en el extremo izquierdo del intervalo
                    F=F/2 #si entra, divide la función entres dos
                rs.append(list[num](r0)) #mete la raiz evaluada en la función a un vector
            else: # si no hay entonces verifica si el producto de la función evaluada en el extremo izquierdo por la función evaluada en la raiz es mayor que cero
                if F*list[num](r0)>0: #verifica si el producto es mator que  cero para ver si se divide el extremo derecho
                    G=G/2 #se divide el extremo derecho evaluado en la función por dos
                a = r0 #se asigna r0 al extremo izquierdo
                F=list[num](r0) #Se calcula F
                rs.append(list[num](r0)) #se mete la raiz evaluada en la función a un vector
            err=abs((r0-r0an)/r0)
            if err<=tole:
                t=False
            elif iter>=n+1:
                print("Se ha alcanzado el número máximo de iteraciones y el método no pudo converger")
                t=False
                veri=False
            iter=iter+1
        if veri and num == '9':
            print("""Método Utilizado:Falsa posicion modificado
            Intervalo de solución x0=""", i, """
            Tolerancia:""", tole, """
            Número de iteraciones realizadas:""", iter, """
            Valor aproximado de la coordenada x del punto máximo:""", r0, """
            punto máximo:""", r0, """,""", y1(r0), """
            Error aproximado porcentual:""", err * 100)  # se imprimen los resultados
        elif veri:
            print("""Método Utilizado:Falsa posición modificado
            Intervalo de solución:""",i,"""
            Tolerancia:""",tole,"""
            Número de iteraciones realizadas:""",iter,"""
            iteraciones calculadas según la tolerancia ingresada:""",n+1,"""
            Valor aproximado de la raiz:""",r0,"""
            Error aproximado porcentual:""",err*100)#se imprimen los resultados
    else: #si no ocurre el cambio de signo el método no trabaja
        print("The function has not sign change")
def NewtonMethod(num): #el parámetro num corresponde a la función a la cual el método encontrará la raiz
    tole=1e-3 #se define la tolerancia
    iter=0 #variable que cuenta en número de iteraciones
    v=True #variable booleana que detendrá el cicla a partir de una condición
    xn=ini[num] #aproximación inicial de la raíz
    xnan=0 #variable auxiliar que almacena el valor anterior de la raiz
    rs=[]
    rs1=[]
    s=True
    while(v): #comienzo del bucle
        xnan=xn #se le asigna el valor de la raiz actual a la auxiliar antes de hacer el cálculo de la nueva aproximación
        xn=xn-list[num](xn)/deria[num](xn) #método de newton(list y deria son diccionarios que contienen las funciones y la derivadas analíticas respectivamente )
        err=abs((xn-xnan)/xn) #se calcula el error aproximado
        if err<=tole: #se verifica si el error aproximado es menor o igual que la tolerancia
            v=False #si entra al condicional entonces cambia el valor de la variable booleana para parar el ciclo
        elif iter>100:
            v=False
            s=False
            print("Se ha alcanzado el máximo de iteraciones y el método no pudo converger")
        iter=iter+1 #se calcula el número de iteraciones
        if num == '8':
            errt = abs((0.56714329 - xn) / 0.56714329)*100
            rs.append(iter)
            rs1.append(err)
    if s and num=='9':
        print("""Método Utilizado:Newton
        Aproximación inicial x0=""",ini[num],"""
        Tolerancia:""",tole,"""
        Número de iteraciones realizadas:""",iter,"""
        Valor aproximado de la coordenada x del punto máximo:""",xn,"""
        punto máximo:""",xn,""",""",y1(xn),"""
        Error aproximado porcentual:""",err*100)#se imprimen los resultados
    elif s:
        print("""Método Utilizado:Newton-Raphson
        Aproximación inicial:""",ini[num],"""
        Tolerancia:""",tole,"""
        Número de iteraciones realizadas:""",iter,"""
        Valor aproximado de la raiz:""",xn,"""
        Error aproximado porcentual:""",err*100)#se imprimen los resultados
        if num=='8':
            return rs,rs1
def SecantMethod(num):
    i=derin[num]
    tole = 1e-3  # se define la tolerancia
    iter = 0  # variable que cuenta en número de iteraciones
    v = True  # variable booleana que detendrá el ciclo a partir de una condición
    xn = i[0] # aproximación inicial de la raíz
    xnan =i[1] # variable auxiliar que almacena el valor anterior de la raiz
    xa=0
    s=True
    rs=[]
    rs1=[]
    while v:
        xa=xn #se le asigna el valor de la raiz xn a la auxiliar antes de hacer el cálculo de la nueva aproximación
        xn=xn-((xn-xnan)/(list[num](xn)-list[num](xnan)))*list[num](xn) #opera el método de la secante
        xnan=xa #se le asigna el valor xn al valor xn-1
        err=abs((xn-xa)/xn) #se cálcula el error
        if err<=tole:#se evalua el error
            v=False #si entra cambia el estado del bucle
        elif iter>100:
            v=False
            s=False
            print("Se ha alcanzado el máximo de iteraciones posibles y el método no pudo converger")
        iter=iter+1 #aumenta el numero de iteraciones
        if num == '8': #si al función ingresada es la de la tarea se calcula el error verdadero porcentual y se mete en vectores la iteración y error corresponde a esa iteración
            errt = abs((0.56714329 - xn) / 0.56714329)*100
            rs.append(iter)
            rs1.append(err)
    if s and num=='9':
        print("""Método Utilizado:Secante
        Aproximación inicial x0=""",i[0],""" y x-1=""",i[1],"""
        Tolerancia:""",tole,"""
        Número de iteraciones realizadas:""",iter,"""
        Valor aproximado de la coordenada x del punto máximo:""",xn,"""
        punto máximo:""",xn,""",""",y1(xn),"""
        Error aproximado porcentual:""",err*100)#se imprimen los resultados
    elif s:
        print("""Método Utilizado:Secante
        Aproximación inicial x0=""",i[0],""" y x-1=""",i[1],"""
        Tolerancia:""",tole,"""
        Número de iteraciones realizadas:""",iter,"""
        Valor aproximado de la raiz:""",xn,"""
        Error aproximado porcentual:""",err*100)#se imprimen los resultados
        if num=='8':
            return rs,rs1
def FixedPoint(num):
    try: #esta sentencia intenta ejecuta un código, si ocure un error en la ejecución del código se hace un manejo del error sin que se salga de la ejecución del programa
        xn=fpini[num] #se llama a la aproximación inicial
        xan=0 #se crea una variable auxiliar que va a manejar el valor anterior calculuado de la raiz
        tole=0.001 #se define la tolerancia
        iter=0 #se define la variable contadora de iteraciones
        t=True #variable que romperá el ciclo while
        v=True #variable que es utilizada para mostrar un condicional
        while t:
            xan=xn #se asigna el valor de la raiz a la variable auxiliar anter de calcular la nueva aproximación
            xn=fp[num](xn) #opera el método dpunto fijo llamando a una función que está contenida en el diccionario fp
            err=abs((xn-xan)/xn) #se calcula el error aproximado
            if err<=tole: #se verifica si el error está por debajo de la tolerancia
                t=False #si si está se sale del ciclo
            elif iter>=100: # si no, verifica si se han excedido el número de iteraciones
                t=False #si sí ocurre se sale del ciclo y muestra un mensaje
                v=False
                print("Se ha alcanzado el máximo de iteraciones posibles y no se ha encontrado el punto fijo")
            iter=iter+1 #se incrementa las iteraciones
        if num=='9':
                print("""Método Utilizado: Punto fijo
            Aproximación inicial:""", fpini[num], """
            Tolerancia:""", tole, """
            Número de iteraciones realizadas:""", iter, """
            Valor aproximado del punto fijo:""", xn, """
            punto máximo:""",xn,""",""",y1(xn),"""
            Error aproximado porcentual:""", err * 100)  # se imprimen los resultados
        if v: #si el método funcionó correctamente muestra un mensaje con toda la información
                print("""Método Utilizado: Punto fijo
            Aproximación inicial:""", fpini[num], """
            Tolerancia:""", tole, """
            Número de iteraciones realizadas:""", iter, """
            Valor aproximado del punto fijo:""", xn, """
            Error aproximado porcentual:""", err * 100)  # se imprimen los resultados
    except:
        print("El método de punto fijo no puede trabajar con la función ingresada")
def SegundoPuntoTarea(ln,ls): #este método gráfica los errores de la función del segundo punto de la tarea
    #xb=lb[0]
    #xfp=lfp[0]
    xne=ln[0]
    xs=ls[0]
    #yb=lb[1]
    #yfp=lfp[1]
    yne=ln[1]
    ys=ls[1]
    #plt.plot(xb,yb,label='Bisection method')
    #plt.plot(xfp, yfp, label='Fake position')
    plt.plot(xs, ys, label='Secant method')
    plt.plot(xne, yne, label='Newton Rhapson')
    plt.yscale('log')
    plt.grid()
    plt.xlabel('Iteraciones')
    plt.ylabel('error porcentual verdadero')
    plt.legend()
    plt.title('Comparación de errores')
    plt.show()
    plt.savefig('gráfica_python2.png')
print("Choose your function")
for x in list2:
    print(x)
f=input("function:")
if f=='8':
    #lb=BisectionMethod(f)
    #lfp=FakePosition(f)
    #ln=NewtonMethod(f)
    #ls=SecantMethod(f)
    #FakePosition2(f)
    FixedPoint(f)
    #SegundoPuntoTarea(ln,ls)
elif f=='9':
    BisectionMethod(f)
    FakePosition(f)
    FakePosition2(f)
    NewtonMethod(f)
    SecantMethod(f)
    FixedPoint(f)
else:
    print("Resultado del método elegido") #si se quiere utilizar algún método quitar el # para que funcione, el caso de quererlos todos quitar todos los #
    #BisectionMethod(f) #tengase en cuenta de que no todas las funciones le funcionan el método de punto fijo, en pantalla se muestra un listado de funciones en las que se aclara cuales son recomendadas para punto fijo
    #FakePosition(f)
    #FakePosition2(f)
    #NewtonMethod(f)
    #SecantMethod(f)
    #FixedPoint(f)



