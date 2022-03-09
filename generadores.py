#Ing. Marbellys Campos

#generador de nros pares, hasta un numero maximo

#utilizando la forma tradicional de funciones
def generapares(limite):
    cant=0
    pares=[]
    while cant <= limite:
        if cant % 2 == 0:
           pares.append(cant) 
        cant += 1
    return pares

print('Utilizando la forma tradicional de funciones:',generapares(20))

#Utilizando GENERADORES y devolviendo toda la lista genera
def generapares(limite):
    cant=0
    
    while cant <= limite:
        if cant % 2 == 0:
          yield cant 
        cant += 1
pares = generapares(20)   
print('DEVUELVE TODA LA LISTA')
for i in pares:
    print('generado:',i)
    
    
#Utilizando GENERADORES y devolviendo un elemento a la vez
def generapares(limite):
    cant=0
    
    while cant <= limite:
        if cant % 2 == 0:
          yield cant 
        cant += 1
pares = generapares(20)   
print('DEVUELVE UN ELEMENTO A LA VEZ')

print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
print('mas codigo de programacion........................')
print(next(pares))
