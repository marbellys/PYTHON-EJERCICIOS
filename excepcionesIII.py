#Ing. Marbellys Campos
# Lanzar excepciones

#evaluador de edad, dependiendo de la edad, decir si eres joven o no

def evaluaredad(edad):
    
    if edad <= 0:
        raise ZeroDivisionError("ingrese valor mayor a cero "+str(edad))
        #raise TypeError("ingrese valor mayor a cero "+str(edad))
    elif edad <16:
        return 'menor de edad'
    elif edad <28:
        return 'joven'
    elif edad <36:
        return 'meejor edad'
    elif edad <50:
        return 'aun productivo'
    elif edad <80:
        return 'Cuidese mucho'
    
        
        
print(evaluaredad(-6))
print('proc culminado')
        