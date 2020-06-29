def sumar(a,b):
    return a+b;
def restar(a,b):
    return a-b;
def dividir(a,b):
    return a/b;
def multiplicar(a,b):
    return a*b;
print("bienvenido al calculator 3000"+'\n'+"¿que deseas hacer?");
print("Opciones\n1.- Sumar\n2.- Restar\n3.- Multiplicar");
cal= input('Escoge una: ');
num1=input("ingresa el número a ");
num2=input("ingresa el número b ");
operaciones = { '1': sumar, '2': restar, '3': multiplicar};

try:
    resultado=operaciones[cal](int(num1),int(num2));
    print("el resultado es: ",resultado);
except:
    print("por favor verifique su opción")