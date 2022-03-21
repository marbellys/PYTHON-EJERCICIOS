#Ing. Marbellys Campos

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('no se puede dividir entre cero')
        return('operacion erronea')

num1 = int(input('introduce el primer valor:'))
num2 = int(input('introduce el segundo valor:'))
opt = input('introduce la opcion deseada (sumar , restar, multiplicar, dividir):  ')

if opt == 'sumar':
    print('la suma es:', sumar(num1,num2))
elif opt == 'restar':
     print('la resta es:', restar(num1,num2))
elif opt == 'multiplicar':
     print('la multiplicacion es:', multiplicar(num1,num2))
elif opt == 'dividir':
     print('la division es:', dividir(num1,num2))
else:
    print('operacion invalida')
    
print('todo ejecutado, continuar programas')
     
     
     
     
     
     
     