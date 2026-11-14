from Biblioteca import Biblioteca
import Funciones


def main():
    biblioteca = Biblioteca()
    opcion = 0

    while opcion != 10:
        Funciones.mostrar_menu()
        opcion = Funciones.leer_opcion()
        print()

        if opcion == 1:
            Funciones.registrar_libro(biblioteca)
        elif opcion == 2:
            Funciones.registrar_usuario(biblioteca)
        elif opcion == 3:
            biblioteca.mostrar_libros()
        elif opcion == 4:
            biblioteca.mostrar_usuarios()
        elif opcion == 5:
            Funciones.pedir_prestamo(biblioteca)
        elif opcion == 6:
            Funciones.pedir_devolucion(biblioteca)
        elif opcion == 7:
            biblioteca.mostrar_prestamos()
        elif opcion == 8:
            Funciones.pedir_busqueda_libro(biblioteca)
        elif opcion == 9:
            Funciones.pedir_busqueda_usuario(biblioteca)
        elif opcion == 10:
            print("Gracias por usar el sistema. ¡Hasta pronto!")


if __name__ == "__main__":
    main()