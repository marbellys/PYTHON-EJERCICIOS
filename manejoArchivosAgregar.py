from io import open

archivo=open('pruebaArchivo.txt','a')
texto='\n ya perdi el sueño'
archivo.write(texto)
archivo.close()

