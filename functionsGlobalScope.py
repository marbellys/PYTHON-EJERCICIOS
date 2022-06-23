# funciones parametros global scope
def  persona(nombre):
    nombre = nombre + ' Campos'
    print('estpy dentro',nombre) 
   # return nombre


  
        
nombre = 'koli'
persona('Margarita')
print('estoy fuera',nombre)