# Solicitud de datos al comprador
def comprador(nombre_apellido_comprador):
    print("Nombre y apellido de comprador: " + nombre_apellido_comprador)
# Sacar precio total
def precio_total(marca,puertas,color):
    precio_total = int(marca + puertas + color)
    print("El precio total de la compra es: " + str(precio_total) + separador)

def precio_marca(marca):
    if marca == "ford":
        print(100000)
    elif marca == "chevrolet":
        print("120000")
    elif marca == "fiat":s
        print("80000")
    else:
       print("No poseemos stock de la marca ingresada")        

def precio_puertas(puertas):
    if puertas == 2:
        print(50000)
    elif puertas == 4:
        print("65000")
    elif puertas == 5:
        print("78000")
    else:
        print("No poseemos stock con la cantidad de puertas ingresadas")

def precio_color(color):
    if color == "blanco":
        print(10000)
    elif color == "azul":
        print("20000")
    elif color== "negro":
        print("30000")
    else:
        print("No poseemos stock de ese color")

for in range(5):
    print = comprador

comprador(nombre_apellido_comprador)
precio_total(precio_marca,precio_puertas,precio_color)

    if cliente (numero):
        numero = 0
        numero = numero + 1
    cliente = print("Cliente nº: "+ str(numero))
