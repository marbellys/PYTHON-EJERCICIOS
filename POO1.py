#Ing. Marbellys Campos

class empleado():
    nombre = 'Marbellys'
    apellido = 'Campos'
    edad = 15
    sexo ='F'
    activo = True
    
    def desactivar(self): # comportamiento o metodo
        self.activo = False
        #pass
    
    def estado(self):     # comportamiento o metodo
        if (self.activo):
            return "El trabajador está ACTIVO"
        else:
            return "El trabajador está INACTIVO"
        
miEmpleado = empleado() # se instancia la clase
    
print('el nombre del empleado es:',miEmpleado.nombre + ' ' + miEmpleado.apellido)
print(miEmpleado.estado())

miEmpleado.desactivar()

print(miEmpleado.estado())

print ("..........a continuacion creamos un segundo objeto.......")

    
    