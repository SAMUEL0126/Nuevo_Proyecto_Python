agenda = {}

def agregar_requerimiento(identificador, nombre, correo, telefono, identificacion):
    requerimiento = {
        'nombre': nombre,
        'correo': correo,
        'telefono': telefono,
        'identificacion': identificacion
    }
    agenda[identificador] = requerimiento

def editar_requerimiento(identificador, nombre, correo, telefono, identificacion):
    if identificador in agenda:
        requerimiento = agenda[identificador]
        requerimiento['nombre'] = nombre
        requerimiento['correo'] = correo
        requerimiento['telefono'] = telefono
        requerimiento['identificacion'] = identificacion
    else:
        print("El requerimiento no existe en la agenda.")

def eliminar_requerimiento(identificador):
    if identificador in agenda:
        del agenda[identificador]
    else:
        print("El requerimiento no existe en la agenda.")

while True:
    print("1. Agregar requerimiento")
    print("2. Editar requerimiento")
    print("3. Eliminar requerimiento")
    print("4. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        identificador = input("Ingrese el identificador del requerimiento: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")
        telefono = input("Ingrese el teléfono: ")
        identificacion = input("Ingrese la identificación: ")
        
        agregar_requerimiento(identificador, nombre, correo, telefono, identificacion)
        print("Requerimiento agregado correctamente.")
        
    elif opcion == "2":
        identificador = input("Ingrese el identificador del requerimiento a editar: ")
        
        if identificador in agenda:
            nombre = input("Ingrese el nuevo nombre: ")
            correo = input("Ingrese el nuevo correo: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            identificacion = input("Ingrese la nueva identificación: ")
            
            editar_requerimiento(identificador, nombre, correo, telefono, identificacion)
            print("Requerimiento editado correctamente.")
        else:
            print("El requerimiento no existe en la agenda.")
        
    elif opcion == "3":
        identificador = input("Ingrese el identificador del requerimiento a eliminar: ")
        
        eliminar_requerimiento(identificador)
        print("Requerimiento eliminado correctamente.")
        
    elif opcion == "4":
        break
    
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
