# funciones con coleccion de argumentos
def  persona(*nombres):
   #for i in nombres:
    # print('el nombre es:',i) 
   for i,x in enumerate(nombres):
     print(i,x)
        
persona('Margarita','Marbellys','Mauruy')