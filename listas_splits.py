from platform import python_branch


l='a,b c,d'
y=l.split()
print('y..',y)
x=l.split(',')
print('x..',x)

print('range3:....',range(3))

print('range 0,3:....',range(0,3))


languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))
print(enumerate_prime)


colores=['rojo','verde','azul','negro']
for i,valor in enumerate(colores):
    print(i,valor)
    
    
    
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while i<len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i+=1
    
print('lista...', new_squares)


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) ):
    if squares[i] == 'orange':
      new_squares.append(squares[i])
    i = i + 1
print ('lista 2...',new_squares)

L=[1,3,2]
O=sorted(L)

print('o...',O)

L.sort()
print('sort..',L)


def suma(a):
  
    """ Añade 1 a la variable a"""    
    b=a+1
   # return b
c=suma(10)
#print('b....',b)
print('c...',c)
