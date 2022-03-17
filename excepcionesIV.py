#Ing. Marbellys Campos
# Lanzar excepciones

#calculo de raiz cuadrada

import math

def calculaRaiz(nro):
    if nro < 0:
        raise ValueError('El nro No debe ser negativo')
    else:
        raiz = math.sqrt(nro)   
        
nro = int(input('Ingrese un numero: ')) 
try:
    calculaRaiz(nro)
except ValueError as NoPermiteNegativos:
    print(NoPermiteNegativos)