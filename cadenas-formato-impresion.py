#Ing. Marbellys Campos

nombre = 'Marbellys'

#1.- concatenar
print('Hola ' + nombre) #R: Hola Marbellys

#2.- interpolacion : imprimir variables en cadenas
#2.1 metodo .format()

nombre_completo = 'Marbellys Campos'

print('Quien suscribe {}'.format(nombre_completo)) #R: Quien suscribe Marbellys Campos


nombre1,nombre2,nombre3 = 'Luis', 'Maria','Jose'
print('Son tres: {0}, {1}, {2}'.format(nombre1,nombre2,nombre3)) #R: Son tres: Luis, Maria, Jose

print('Son tres: {a}, {b}, {c}'.format(a='Luis',b='Jose',c='Maria')) #R: Son tres: Luis, Jose, Maria


#2.2 metodo .F-strings()
nombre1,nombre2,nombre3 = 'Lolita', 'Maria','Jose'    
print(f"Son tres: {nombre1},{nombre2},{nombre3}") #R:  Son tres: Lolita,Maria,Jose

