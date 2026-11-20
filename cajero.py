#simulador de un cajero automático
#universiadad tecnica de cotopaxi
#Nombre: Marcos hidalgo
#curso: 1"A" software
#cajero donde 1 es consultar saldo, 2 es depositar, 3 es retirar, 4 es salir
saldo = 0.00
while True :
    print("""Cajero automático UTC     #muestra todas las opcciones del cajero
          Opciones:
          1. Consultar saldo
          2. Depositar
          3. Retirar
          4. Salir
          """)

    opcion = int(input("Ingrese una opción: "))      #nos pide elegir la opcion que vamos a utilizar en el cajero
    match opcion:
        case 1:
            print(f"Su saldo es: ${saldo:.2f}")      #aqui consultamos el saldo
        case 2:
            monto = float(input("Ingrese el monto a depositar: "))          #aqui realizamos el deposito
            if monto > 0:
                saldo += monto
                print(f"Su saldo es: ${saldo:.2f}")
            else:
                print("El monto a depositar debe ser mayor que cero.")
        case 3:
            monto = float(input("Ingrese el monto a retirar: "))               #qui realizamos los retiros
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Su saldo es: ${saldo:.2f}")
            else:
                print("Saldo insuficiente no se puede realizar el retiro.")
        case 4:
            print("Gracias por usar el cajero automatico")                       #aqui es la opcion de salir
            break
        case _:
            print("Opción no valida")