
# <-----------------> Registro de usuarios a rentar una bicicleta
usuarios_registrados = []
def registrarUsuario():
    cedula_usuario = input(" <-- Ingresa tu cedula: ")
    nombre_usuario = input("\n <-- Ingresa tu nombre completo: ")
    correo_usuario = input("\n <-- Ingresa tu correo: ")
    usuarios_guardados = {
        "cedula_usuario": cedula_usuario,
        "nombre_usuario": nombre_usuario,
        "correo_usuario": correo_usuario,
    }
    usuarios_registrados.append(usuarios_guardados)
    print("\n--> Registro exitoso. Ahora puedes rentar una bicicleta. ")

# <-----------------> Consultar usuario
def consultarUsuario():
    print("--> Listado de usuario solicitado \n")
    if len(usuarios_registrados) == 0:
        print("<-- No hay usuarios registrados")
    else:
        for usuarios_guardados in usuarios_registrados:
            print(" < -- > ")
            print(" Cedula del usuario: " + usuarios_guardados["cedula_usuario"])
            print(" Nombre del usuario: " + usuarios_guardados["nombre_usuario"])
            print(" Correo del usuario: " + usuarios_guardados["correo_usuario"])
            print(" < -- > \n")
            
# <-----------------> Registrar bicicletas a los usuarios registrados
rentas_registradas = []
def registrarRenta():
    cedula_renta = input("<-- Ingresa la cedula del usuario: ")
    renta_cedula_encontrada = False
    for usuarios_guardados in usuarios_registrados:
        if usuarios_guardados["cedula_usuario"] == cedula_renta:
            renta_cedula_encontrada = True
    if not renta_cedula_encontrada:
        print("\n--> Cedula no existe o no se ha registrado")
        registrarRenta()
        return
    origen = input("\n <-- Ingresa el origen de su viaje: ")
    destino = input("\n <-- Ingresa el destino de su viaje: ")
    renta_guardada = {
        "cedula_renta": cedula_renta,
        "origen": origen,
        "destino": destino,
    }
    rentas_registradas.append(renta_guardada)
    print("\n--> Renta exitosa. ")

def consultarRenta():
    print("--> Listado de rentas registradas \n")
    if len(rentas_registradas) == 0:
        print("<-- No hay rentas registradas")
    else:
        for renta_guardada in rentas_registradas:
            print(" < -- > ")
            cedula_renta = renta_guardada["cedula_renta"]
            nombre = ""
            for usuario_guardado in usuarios_registrados:
                if usuario_guardado["cedula_usuario"] == cedula_renta:
                    nombre = usuario_guardado["nombre_usuario"]
                    break
            print(" Nombre usuario" + nombre)
            print(" Cedula usuario" + cedula_renta)
            print(" Origen: " + renta_guardada["origen"])
            print(" Destino: " + renta_guardada["destino"])
            print(" < -- >")