#Necesito que dada una edad, decida el programa si soy mayor o menor de edad
#Mayor de edad es 18 o +
#Si es mayor de 70 avisale que es jubilado
edad = 105
if edad >= 18:
    print("Usted es mayor de edad")
    if edad > 100:#if anidados
               print("Bienvenida Mirta Legrand")
               edad = 2
    if edad > 70:#if anidados
                print("Usted es jubilado!!!!")
else:
    print("Usted es menor de edad")