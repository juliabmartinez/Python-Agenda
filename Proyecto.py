import os
CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre , telefono , categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():

        crear_directorio()

        # Muestra el menu de opciones
        mostra_menu()

        # Preguntar al Usuario la acciòn a realizar

        preguntar = True
        while preguntar:
             opcion = input('Seleccione una opcion: \r\n')
             opcion = int(opcion)


            # Ejecutar las opciones


             if opcion == 1:
                agregar_contacto()
                preguntar = False
             elif opcion == 2:
                editar_contacto()
                preguntar = False
             elif opcion == 3:
                mostrar_contactos()
                preguntar = False
             elif opcion == 4:
                buscar_contacto()
                preguntar = False
             elif opcion == 5:
                eliminar_contacto()
                preguntar = False
             else:
                print('Opciòn no Válida, Intente de nuevo')


def eliminar_contacto():
    nombre = input('Selecciones el contacto que quiere eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado Correctamente')
    except expression as identifier:
        print('No existe contacto')
    app()

def buscar_contacto():
    nombre = input ('Selecione el Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')

    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

def mostra_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agreagr Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto ')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists('contactos/'):
        os.makedirs('contactos')

def editar_contacto():
    print('Escribe el contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = os.path.isfile(CARPETA + nombre_anterior + EXTENSION)



    if existe:

            with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

              # Resto de los Campos
              nombre_contacto = input('Agrega el Nuevo Nombre:\r\n')
              telefono_contacto = input('Agregar el Nuevo Telefono:\r\n')
              categoria_contacto = input('Agrega la Nueva Categoria:\r\n')

              # Instanciar
              contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
              # Escribir en el archivo

              archivo.write('Nombre:' + contacto.nombre + '\r\n')
              archivo.write('Telefono:' + contacto.telefono + '\r\n')
              archivo.write('Categoria:' + contacto.categoria + '\r\n')

             # Renombrar el archivo
              os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

    else:
        print('Ese contacto no existe')

        # Mostra Mensaje de exito
        print('\r\n Contacto editado Correctamente \r\n')

        app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

# Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)




    if not existe:

       with open(CARPETA +nombre_contacto + EXTENSION, 'w') as archivo:
        # Resto de los campos
        telefono_contacto = input('Agregar el Telefono:\r\n')
        categoria_contacto = input('Categoria Contacto:\r\n')

        # Instanciar la clase
        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

       # Escribir en el archivo

        archivo.write('Nombre:' + contacto.nombre + '\r\n')
        archivo.write('Telefono:' + contacto.telefono +'\r\n')
        archivo.write('Categoria:' + contacto.categoria +'\r\n')

         #Mostrar un mensaje de exito
        print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese contacto ya existe')

        # Reinciar La app
        app()

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
