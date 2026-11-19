def operaciones (valor):
    
    if valor == 4:
        print("Suma") 
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la suma es:", num1 + num2)
    elif valor == 3:
        print("Resta")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la resta es:", num1 - num2)      
    elif valor == 2:
        print("Multiplicación")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la multiplicación es:", num1 * num2)
    elif valor == 1:
        print("División")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if num2 != 0:
            print("El resultado de la división es:", num1 / num2)
        else:
            print("Error: No se puede dividir entre cero.")  
        
    """
    Función que recibe un parametro para sumar,restar,multiplicar y dividir.
    """

print("ingrese un valor a operar: 4 para sumar, 3 para restar, 2 para multiplicar, 1 para dividir")
valor = int(input("Ingrese el valor: "))
operaciones(valor)  # Llamada a la función y muestra del resultado