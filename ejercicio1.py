#Sacar promedio
def promedio  (nota_matematica,nota_literatura, nota_fisica):
    return (nota_matematica + nota_literatura + nota_fisica)/3

#Imprimir datos
def datos_del_alumno(nombre,apellido,promedio_alumno):
    print("El alumno: " + nombre + " " + apellido + " tiene promedio:" + str(promedio_alumno))

#Ver aprobacion de alumno
    if promedio_alumno >= 6:
        print("Aprobado")
        if promedio_alumno >= 9:
            print("Alumno destacado")
    elif promedio_alumno >=4:
        print("A recuperatorio")    
    else:
        print("Insuficiente")

#Ingresar datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nota_matematica = int(input("Ingrese su nota de Matematicas: "))
nota_literatura = int(input("Ingrese su nota de Literatura: "))
nota_fisica = int(input("Ingrese su nota de Fisica: "))


promedio_alumno = promedio(nota_matematica,nota_literatura, nota_fisica) 
datos_del_alumno(nombre,apellido,promedio_alumno)
estado_aprobacion(promedio_alumno)