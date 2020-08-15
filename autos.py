for i in range(5):
    print("----------------------------------------------------------------")
    nombre_comprador = input("Ingresar nombre: ")
    apellido_comprador = input("Ingresa apellido: ")
    
    marca = input("Ingresar marca: ")
    marca = marca.title()
    if marca == 'Ford':
        precio_marca = 100000
    elif marca == 'Chevrolet':
        precio_marca = 120000
    elif marca == 'Fiat':
        precio_marca = 80000
    else:
        print("No poseemos stock de la marca solicitada")
        continue

    puertas = input("Ingresar cantidad de puertas: ")
    if puertas == '2':
        precio_puertas = 50000
    elif puertas == '4':
        precio_puertas = 65000
    elif puertas == '5':
        precio_puertas = 78000
    else:
        print("No poseemos stock con la cantidad de puertas solicitada")
        continue

    color = input("Ingresar color: ")
    color = color.lower()
    if color == 'blanco':
        precio_color = 10000
    elif color == 'azul':
        precio_color = 20000
    elif color == 'negro':
        precio_color = 30000
    else:
        print("No poseemos stock del color solicitada")
        continue
    
    precio_final = precio_marca + precio_puertas + precio_color
    print("Cliente: "+nombre_comprador+" "+apellido_comprador)
    print("Descripciòn: Realizo la compra de un auto marca "+ marca+" de color "+color +" con "+ puertas+" puertas.")
    print("Precio total: "+str(precio_final))