#Nuestro programa se va a ejecutar hasta que una variable sea True
#​while = mientras una condición se cumpla, el loop continua

condicion = False
i = 0
while condicion == False:
    if i == 3:
        condicion = True
    print(i)
    i = i + 1