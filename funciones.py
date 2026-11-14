from datetime import datetime
from libro import Libro
from usuario import Usuario


def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Mostrar libros")
    print("4. Mostrar usuarios")
    print("5. Realizar préstamo")
    print("6. Devolver libro")
    print("7. Mostrar préstamos")
    print("8. Buscar libro")
    print("9. Buscar usuario")
    print("10. Mostrar historial de entradas y salidas")
    print("11. Salir")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("El campo no puede estar vacío.")


def leer_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Entrada inválida. Ingrese un número entero.")


def leer_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError:
            print("Fecha inválida. Use el formato DD/MM/AAAA.")


def leer_opcion():
    while True:
        opcion = leer_entero("Seleccione una opción: ")
        if 1 <= opcion <= 11:
            return opcion
        print("Opción fuera de rango. Elija entre 1 y 11.")


def registrar_libro(biblioteca):
    codigo = leer_texto("Código: ")
    titulo = leer_texto("Título: ")
    autor = leer_texto("Autor: ")
    anio = leer_entero("Año de publicación: ")
    biblioteca.agregar_libro(Libro(codigo, titulo, autor, anio))


def registrar_usuario(biblioteca):
    carnet = leer_texto("Carnet: ")
    nombre = leer_texto("Nombre: ")
    correo = leer_texto("Correo: ")
    biblioteca.agregar_usuario(Usuario(carnet, nombre, correo))


def pedir_prestamo(biblioteca):
    carnet = leer_texto("Carnet del usuario: ")
    codigo = leer_texto("Código del libro: ")
    fecha = leer_fecha("Fecha de salida DD/MM/AAAA (Enter para hoy): ")
    biblioteca.realizar_prestamo(carnet, codigo, fecha)


def pedir_devolucion(biblioteca):
    codigo = leer_texto("Código del libro a devolver: ")
    fecha = leer_fecha("Fecha de entrada DD/MM/AAAA (Enter para hoy): ")
    biblioteca.devolver_libro(codigo, fecha)


def pedir_busqueda_libro(biblioteca):
    codigo = leer_texto("Código del libro a buscar: ")
    libro = biblioteca.buscar_libro(codigo)
    if libro is None:
        print("Libro no encontrado.")
    else:
        libro.mostrar_informacion()


def pedir_busqueda_usuario(biblioteca):
    carnet = leer_texto("Carnet del usuario a buscar: ")
    usuario = biblioteca.buscar_usuario(carnet)
    if usuario is None:
        print("Usuario no encontrado.")
    else:
        usuario.mostrar_informacion()