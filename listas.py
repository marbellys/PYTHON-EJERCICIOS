#Ing. Marbellys Campos

gustos = ['Comer', 'Bailar','Correr','Nadar']

sabores = ['dulce','amargo','acido']

#indice de listas
print(gustos[2]) #R:  Correr

#slicing de listas
print(gustos[2:]) #R: ['Correr', 'Nadar']

#concatenar listas
nueva_lista = gustos + sabores
print(nueva_lista) #R:  ['Comer', 'Bailar', 'Correr', 'Nadar', 'dulce', 'amargo', 'acido']

print(gustos + sabores)

#Modificacion de listas

gustos[0] = 'Saltar'

print(gustos)  #R: ['Saltar', 'Bailar', 'Correr', 'Nadar']


#Funciones de las listas

#append: agregar elemento a la lista

sabores = ['dulce','amargo','acido']
sabores.append('citrico')
print(sabores)  #R: ['dulce', 'amargo', 'acido', 'citrico']

#pop:remover element de la lista

sabores.pop()
print(sabores)  #R: ['dulce', 'amargo', 'acido']


#pop:remover un element en particular de la lista
sabores = ['dulce', 'amargo', 'acido', 'citrico']
elem_eliminado = sabores.pop(1)
print(sabores)  #R: ['dulce', 'acido', 'citrico']
print(f'Eliminado: {elem_eliminado}')  #R: ['dulce', 'acido', 'citrico']

#sort: ordenar listas
sabores = ['dulce', 'amargo', 'acido', 'citrico']
sabores.sort()
print(sabores)  #R: ['acido', 'amargo', 'citrico', 'dulce']

#sort: muestra la lista en reverso
sabores = ['dulce', 'amargo', 'acido', 'citrico']
sabores.reverse()
print(sabores)  #R: ['citrico', 'acido', 'amargo', 'dulce']

# OJO: no se le asigna a una lista, una lista ordenada, ya que este no retorna nada
sabores = ['dulce', 'amargo', 'acido', 'citrico']
orden = sabores.sort() #NO ES CORRECTO
print(orden) #R: None