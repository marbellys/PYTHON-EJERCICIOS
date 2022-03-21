#Ing. Marbellys Campos

email = str(input('Favor introducir su Email: '))

arroba = email.count('@')

if (arroba !=1) or (email.find('@')==0) or ((len(email)-1)==email.rfind('@')):
    print('Mail incorecto')
else:
      print('Mail corecto')

