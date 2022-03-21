class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
        self.acelera=False
        self.frena=False
        
  
        
    def descripcion(self):
        
        print('Nombre:',self.nombre, '\nEdad:',self.edad, '\nDireccion:', self.lugar_residencia)

    
class Empleado(Persona):
   def __init__(self,salario,antiguedad):
       self.salario,
       self.antiguedad
       
antonio=Persona('maria lopez',15,'pto ordaz')   
antonio.descripcion()
#antonio = Persona()