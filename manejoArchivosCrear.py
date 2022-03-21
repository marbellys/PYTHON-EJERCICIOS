#Ing. Marbellys Campos

from io import open

archivoTexto=open("pruebaArchivo.txt","w")
frase='Hoy es lunes y tengo mucha flojera'

archivoTexto.write(frase)
archivoTexto.close()