#Ing. Marbellys Campos

from io import open

archivoTexto=open("pruebaArchivo.txt","r")

lineasTexto = archivoTexto.readlines()

archivoTexto.close()
print('........muestra todo el archivo...........')
print(lineasTexto)  #muestra todas las lineas


print('\n.........muestra solo la tercera linea...........')
print(lineasTexto[2])  #muestra solo la primera linea