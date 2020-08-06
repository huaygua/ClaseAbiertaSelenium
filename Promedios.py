nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Alumno: " + nombre + " " + apellido)

nota_matematica = int(input("Ingrese su nota de Matematicas: "))
nota_literatura = int(input("Ingrese su nota de Literatura: "))
nota_fisica = int(input("Ingrese su nota de Fisica: "))

def promedio  (nota_matematica,nota_literatura, nota_fisica):
    return (nota_matematica + nota_literatura + nota_fisica)/3
    
    
promedio_alumno = promedio(nota_matematica,nota_literatura, nota_fisica) 
print("Su promedio es " + str(promedio_alumno))


promedio = float (promedio_alumno)

if promedio_alumno >= 9:
    print("Alumno destacado")
elif promedio_alumno >= 6:
    print("Aprobado")
    
elif promedio_alumno >=4:
    print("A recuperatorio")
else:
    print("Insuficiente")
