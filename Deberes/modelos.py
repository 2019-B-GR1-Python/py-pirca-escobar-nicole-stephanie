def menu_principal ():
    print ("Selecciona una opción")
    print ("\t1 - Ingresar Modelos")
    print ("\t2 - Eliminar Modelo Registrado")
    print ("\t3 - Consultar Modelos Registrados")
    print ("\t4 - Modificar Modelos Registrados")
    print ("\t5 - Buscar Modelos Registrados")
    print ("\t6 - salir")

while True:
    menu_principal()
      
    opcionMenu = input("Elija una opción ")
            
    if opcionMenu=="1":
        print("1. \n  Registros de Modelos")
        ingresar_modelos()
     
    elif opcionMenu=="2": 
        print("2. \n Eliminar Modelo Registrado")
        eliminar_modelo()
        
    elif opcionMenu=="3":
        print("3. \n Consultar Modelos Registrados")
        leer_Modelos()  
        
    elif opcionMenu=="4":
        print("4. \n Modificar Modelos Registrados")
        modificar_modelo()
        
    elif opcionMenu=="5":
        print("4. \n Buscar Modelos Registrados")
        buscar_modelo()
   
    elif opcionMenu=="6":
        break
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def leer_Modelos():
    try:
        path='./modelo.txt'
        archivo_abierto = open(path)
        lineas= archivo_abierto.readlines()
        print("\nMODELOS\n")
        for linea in lineas:
            print(f "  {linea}")
        archivo_abierto.close
    except Exception as error:
        print(f "Error en lectura: {error}")

def ingresar_modelos():
    print("\n  Ingrese la información del modelo a ingresar\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre: ")
    descripcion = input("  Descripcion: ")
    color = input("  Color: ")
    precio = input("  Precio: ")
    try:
        path = "./modelo.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo}, {nombre},{descripcion}, {color}, {precio}\n"])
        archivo_escritura_abierto.close()
        print("\n Ingreso del Modelo exitoso \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")
def modificar_modelo():
    codigo = input("\n  Ingrese el codigo a modificar: ")
    try:
        path="./modelo.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                nombre = input("  Ingrese el nuevo nombre del modelo: ")
                precio = input("  Ingrese el nuevo precio: ")
                modelo_modificado = f"{codigo}  , {nombre}  , {precio}\n"
                archivo_abierto.write(modelo_modificado)
                archivo_abierto.truncate()
                print(f "\n  Modelo {codigo} modificado \n")
            else:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
    except Exception as error:
        print(f "Error en actualizacion: {error}")
def eliminar_modelo():
    codigo = input("\n  Ingrese el codigo a eliminar: ")
    try:
        path="./modelo.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if not codigo in linea:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
        print(f"\n Eliminado: {codigo} \n")
    except Exception as error:
        print(f"Error en actualizacion: {error}")
eliminar_modelo()


def buscar_modelo():
    codigo = input("\n  Ingrese el codigo del modelo: ")
    try:
        path="./modelo.txt"
        archivo_abierto = open(path)
        lineas = archivo_abierto.readlines()
        for linea in lineas:
            if not codigo in linea:*
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
        print(f "\n  Encontrado: {codigo} \n")
    except Exception as error:
        print(f "Modelo no encontrado: {error}")
buscar_modelo()