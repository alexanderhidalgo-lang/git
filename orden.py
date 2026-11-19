#ordenamiento de 10 numeros (orden ascendente y descendente) numero mayor y menor
#universiadad tecnica de cotopaxi
#Nombre: Marcos hidalgo
#curso: 1"A" software


numero = int(input("Ingrese los números: "))      #ingreso de los 10 numeros
numeros = []                                       #creacion de la lista vacia
for i in range (numero):                                      #ciclo for para ingresar los 10 numeros
    num = int(input(f"numero {i+1}: "))   #ingreso de los numeros
    numeros.append(num)                             #agregar los numeros a la lista

numeros.sort()                                      #ordenamiento de los numeros
print(numeros)  #mostrar los numeros
numeros.sort(reverse=True)                       #ordenamiento de los numeros en orden descendente
print(numeros)  #mostrar los numeros



print(f"maximo: {max(numeros)}")  #mostrar el numero mayor
print(f"minimo: {min(numeros)}")  #mostrar el numero menor