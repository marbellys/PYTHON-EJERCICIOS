#Ing. Marbellys Campos

class Coche():
    
    def desplazamiento(self):
        
        print('me desplazo utilizando 4 ruedas')
        
class Moto():
    
    def desplazamiento(self):
        print('Me despalzo utilizando 2 ruedas')
        
class Camion():
    
    def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')


# SIN polimorfismo:
print('...........SIN polimorfismo.........')
       
miMoto = Moto()
miMoto.desplazamiento()

miCoche = Coche()
miCoche.desplazamiento()

miCamion = Camion()
miCamion.desplazamiento()



# Para hacer lo mismo con polimorfismo:
print('...........Para hacer lo mismo con polimorfismo.........')
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)
    
    