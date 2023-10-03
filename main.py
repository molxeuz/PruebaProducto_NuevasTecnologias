import os, sys, keyboard
import process as process

# <-----------------> Limpiar consola    
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# <-----------------> Menu de opciones
def mostrarMenu():
    print("\n <-- Menu de opciones --> ")
    print(" 1. registro de usuario ")
    print(" 2. Rentar una bicicleta ")
    print(" 3. Consultar un usuario ")
    print(" 4. Consultar una bicicleta ")
    print(" 5. Salir \n")
    
# <-----------------> Finalizar programa
def finalizarPrograma():
    print("<-- Gracias por utilizar el software.")
    print("\n" + "Presiona (Ctrl) para mostrar el menú o (Shift) para salir del programa. \n")
    while True:
        if keyboard.is_pressed("ctrl"):
            limpiarConsola()
            break
            mostrarMenu()
        elif keyboard.is_pressed("shift"):
            limpiarConsola()
            print("\n" + "Saliendo del programa...\n")
            sys.exit()

# <-----------------> Ejecutar programa 
opcion = "0"
while opcion != "5":
    mostrarMenu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        limpiarConsola()
        print("Has seleccionado la Opción 1. \n")
        print("Preciona enter para ejecutar... ")
        input()
        process.registrarUsuario()
        finalizarPrograma()
    elif opcion == "2":
        limpiarConsola()
        print("Has seleccionado la Opción 2. \n")
        print("Preciona enter para ejecutar... ")
        input()
        process.registrarRenta()
        finalizarPrograma()
    elif opcion == "3":
        limpiarConsola()
        print("Has seleccionado la Opción 3. \n")
        print("Preciona enter para ejecutar... ")
        input()
        process.consultarUsuario()
        finalizarPrograma()
    elif opcion == "4":
        limpiarConsola()
        print("Has seleccionado la Opción 4. \n")
        print("Preciona enter para ejecutar... ")
        input()
        process.consultarRenta()
        finalizarPrograma()
    elif opcion == "5":
        limpiarConsola()
        print("Has seleccionado la Opción 5. \n")
        print("Preciona enter para ejecutar... ")
        input()
        finalizarPrograma()
        sys.exit()
    else:
        limpiarConsola()
        print("\n" + "Opción no válida. Por favor, selecciona una opción del menú. \n")