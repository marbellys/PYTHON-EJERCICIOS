class vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        
       self.enmarcha=True
        
        
    def acelerar(self):
        
        acelera=True
        
        
    def frenar(self):
        
        self.frena=True
        
    def estado(self):
        
        print('Marca:',self.marca,'\nModelo:',self.modelo,'\nEn marcha:',self.enmarcha,'\nAcelerando:',self.acelera,'\nFrenado:',self.frena)

class moto(vehiculos):
    pass

miMoto =moto('toyota','corola')  #se le coloca argumentos porq hereda el constructor de la clase vehiculos que recibe paramtros

miMoto.estado()