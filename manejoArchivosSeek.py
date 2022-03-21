from io import open

archivo= open('pruebaArchivo.txt','r')

archivo.seek(10)

print(archivo.read())
print('.......leo otra vez hast ala posicion 11........')
print(archivo.read(11))