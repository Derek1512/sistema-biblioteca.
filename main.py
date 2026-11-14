from biblioteca import biblioteca
import funciones


def main():
    biblioteca = biblioteca()
    opcion = 0

    while opcion != 10:
        funciones.mostrar_menu()
        opcion = funciones.leer_opcion()
        print()

        if opcion == 1:
            funciones.registrar_libro(biblioteca)
        elif opcion == 2:
            funciones.registrar_usuario(biblioteca)
        elif opcion == 3:
            biblioteca.mostrar_libros()
        elif opcion == 4:
            biblioteca.mostrar_usuarios()
        elif opcion == 5:
            funciones.pedir_prestamo(biblioteca)
        elif opcion == 6:
            funciones.pedir_devolucion(biblioteca)
        elif opcion == 7:
            biblioteca.mostrar_prestamos()
        elif opcion == 8:
            funciones.pedir_busqueda_libro(biblioteca)
        elif opcion == 9:
            funciones.pedir_busqueda_usuario(biblioteca)
        elif opcion == 10:
            print("Gracias por usar el sistema. ¡Hasta pronto!")


if __name__ == "__main__":
    main()