#Ing. Marbellys Campos

from io import open

archivoTexto=open("pruebaArchivo.txt","r")

texto = archivoTexto.read()

archivoTexto.close()

print(texto)