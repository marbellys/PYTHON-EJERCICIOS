#Ing. Marbellys Campos

def divide():
    try:
        a = float(input('Introduce el primer valor:'))
        b = float(input('Introduce el segundo valor:'))
        print('el calculo es:' + str(a/b))
    except ZeroDivisionError:
        print('Error... division por 0')
     except ValueError:
        print('Valor no valido')
    except:
        print('Ocurrió un Error')
    print('Programa finalizado')

divide()