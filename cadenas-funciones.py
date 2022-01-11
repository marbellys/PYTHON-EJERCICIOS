#Ing. Marbellys Campos

direccion = 'Venezuela, Edo. Bolivar'

#convertir a mayuscula
print(direccion.upper())  #resultado: VENEZUELA, EDO. BOLIVAR


#convertir a mayuscula
print(direccion.lower()) #resultado: venezuela, edo. bolivar

#split
direccion = 'Venezuela, Edo. Bolivar'

print(direccion.split()) #resultado: ['Venezuela,', 'Edo.', 'Bolivar']

direccion = 'Venezuela|Edo. Bolivar'

print(direccion.split('|')) #resultado: ['Venezuela', 'Edo. Bolivar']

