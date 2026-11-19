#simulador de un estacionamiento
#universiadad tecnica de cotopaxi
#Nombre: Marcos hidalgo
#curso: 1"A" software


cupos = 50
maximo = 50

while True:
    print("\n===== ESTACIONAMIENTO =====")
    print("1. Entrada de vehículo")
    print("2. Salida de vehículo")
    print("3. Consultar cupos")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:

        case 1:
            if cupos > 0:
                cupos -= 1
                print("Vehículo ingresado correctamente")
                print("Cupos disponibles:", cupos)
            else:
                print("Estacionamiento lleno")

        case 2:
            if cupos < maximo:
                cupos += 1
                print("Vehículo salió correctamente")
                print("Cupos disponibles:", cupos)
            else:
                print("No hay vehículos en el estacionamiento")

        case 3:
            print("Cupos disponibles:", cupos)
            print("Cupos ocupados:", maximo - cupos)

        case 4:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida")
