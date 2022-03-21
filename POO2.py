#Ing. Marbellys Campos

class empleado():
    nombre = 'Marbellys'
    apellido = 'Campos'
    edad = 15
    sexo ='F'
    activo = True
    
    def trabajar(self, activado): # comportamiento o metodo
        self.activo = activado
        if (self.activo):
                return "El trabajador está ACTIVO"
        else:
            return "El trabajador está INACTIVO"
    
    def estado(self):     # comportamiento o metodo
        print('El nombre del empleado es:',self.nombre,self.apellido,' y tiene ', self.edad,' de edad')
        
miEmpleado = empleado() # se instancia la clase
  
miEmpleado.estado()

print(miEmpleado.trabajar(True))

print ("..........a continuacion creamos un segundo objeto.......")

empleado2 = empleado()

print(miEmpleado.trabajar(False))  
empleado2.estado()