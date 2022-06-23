#Run this prior to starting the exercise
from random import randint as rnd

empleados = 'empleados.txt'
excluidos = 'inactivos.txt'
fee =('yes','no')

# Genera informacion en archivos
def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Empleados  Fecha Ingreso  Activo  \n')
        data = "{:^9}  {:<12}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Empleados  Fecha Ingreso  Activo  \n')
        data = "{:^9}  {:<12}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


#genFiles(empleados,excluidos)


'''
Los dos argumentos de esta función son los archivos:
    - empleados:Archivo con la lista de los miembros actuales
    - excluidos: Archivo que contiene la lista de antiguos miembros
    
    Esta función debe eliminar todas las filas de empleados.txt que contengan 'no' 
    en la columna "Activo" y las añade a excluidos.txt.
    '''
def cleanFiles(empAct,empExcl):
    # TODO: Open the empleados file as in r+ mode
    with open(empAct,'r+') as emp: 
        #TODO: Open the excluidos file in a+ mode
        with open(empExcl,'a+') as exc:
            emp.seek(0)
            empleados = emp.readlines()  #crea una lista con lo q esta en el archivo empleados
                                         #donde el 1er registro es la cabecera
            cabecera = empleados[0]
            empleados.pop(0)   # borra la cabecera
            for empleado in empleados:
                if 'no' in empleado:  #si el registro tiene 'no'
                    exc.write(empleado)
                    
            #esto hace lo mismo:
            #exc = [empleado for empleado in empleados if ('no' in empleado)]
                       
            #go to the beginning of the write file
            emp.seek(0) 
            emp.write(cabecera)
            for empleado in empleados:
               if (empleado in exc):
                 exc.write(empleado)
               else:
                 emp.write(empleado)      
            emp.truncate()
                

cleanFiles(empleados,excluidos)


cabeceras = "Empleados  Fecha Ingreso  Activo  \n"
with open(empleados,'r') as readFile:
    print("empleados Activos: \n\n")
    print(readFile.read())
    
with open(excluidos,'r') as readFile:
    print("Empleados Excluidos: \n\n")
    print(readFile.read()) 
    
    
def testMsg(passed):
    if passed:
       return 'Paso la prueba'
    else :
       return 'Falló la prueba'

testWrite = "pruebaEscitura.txt"
testAppend = "pruebaAgregar.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("El número de filas no cuadra. Asegúrese de que sus archivos finales tienen el mismo encabezado y formato.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Miembros inactivos en el archivo")
        break
    else:
        if line not in ogWrite:
            print("Los datos del archivo no coinciden con el archivo original")
            passed = False
print ("{}".format(testMsg(passed)))
    