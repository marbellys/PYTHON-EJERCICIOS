#Ing. Marbellys Campos

# cadenas de textos
ejemplo1 = 'Con comilla simple'
ejemplo2 = "Con comilla doble"

#imprime las variables
print(ejemplo1) #salida   Con comilla simple
print(ejemplo2) #salida   Con comilla doble

print('Con \ncomilla \nsimple')

print(ejemplo1 , ejemplo2)

# agarrar subsecciones de cadenas
# 1.- indices de cadenas
print(ejemplo1[1]) #salida o

#indices de inverso
print(ejemplo2[-17]) #salida C

#toma el ultimo de la cadena
print(ejemplo2[-1]) #salida e

#2.- slicing
print(ejemplo1[1:5]) #salida   on c

print(ejemplo1[4:]) #salida  comilla simple

#las cadenas NO SE PUEDEN CAMBIAR
#pero SI CONCATENAR

nombre_apellido = 'Marbellys Campos'

apellido_esposo = 'Espinoza'

nombre_apellido = nombre_apellido +' '+ apellido_esposo

print(nombre_apellido) #salida:  Marbellys Campos Espinoza
