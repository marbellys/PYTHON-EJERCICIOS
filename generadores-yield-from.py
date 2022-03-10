#Ing. Marbellys Campos

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento
        
devueltas = devuelve_ciudades("Barcelona","Caracas","Pto Ordaz","Maturin")
print(next(devueltas))
print(next(devueltas))
print(next(devueltas))