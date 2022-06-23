# Write line to file
exmp2 = 'archivo2.txt'
with open(exmp2, 'r+') as writefile:
    writefile.write("This is line A \n")
    writefile.write("This is line B \n")
#    print(writefile.readlines())
    
with open(exmp2, 'r+') as testwritefile:
    print(testwritefile.readline())
    
    
    
lFrutas = ["Peras\n","Manzanas\n","Uvas\n","Melon\n","Patilla\n","Lulo\n"]

with open('frutas.txt','w+') as frutas:
    for fruta in lFrutas:
        print(fruta)
        frutas.write(fruta)