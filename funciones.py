#def nombre de funcion,funcion es un grupo de lineas de codigo que hacen algo y cada vez que llame a esa funcion va a ejecutar esas lineas de codigo

def ingresar_numero():
    numero = int (input("ingrese numero: "))
    numero = numero*30
    return numero
    
def hacer_algo_con_numeros(a,b):
    
    return a + b  
#mi_numero = ingresar_numero()
#print(mi_numero)
a = 10
b = 50
mi_variable = hacer_algo_con_numeros(a,b)
print(mi_variable)
mi_variable = hacer_algo_con_numeros(30,1000)
print(mi_variable)


