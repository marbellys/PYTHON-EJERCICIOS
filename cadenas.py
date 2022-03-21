#Ing. Marbellys Campos

edad=input('Introduzca su edad:     ')

while (edad.isdigit()==False):
    print('Introduzca un VALOR NUMERICO')
    edad=input('Introduzca su edad')
    
if int(edad)<18:
    print('NO puede pasar')
else:
    print('puede pasar')