from datetime import date
from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


def titulo(texto):
    print(f"\n--- {texto} ---")


def ejecutar_pruebas():
    b = Biblioteca()

    titulo("Prueba 1: Registrar tres libros")
    b.agregar_libro(Libro("L001", "Cien años de soledad", "Gabriel García Márquez", 1967))
    b.agregar_libro(Libro("L002", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605))
    b.agregar_libro(Libro("L003", "El principito", "Antoine de Saint-Exupéry", 1943))

    titulo("Prueba 2: Registrar dos usuarios")
    b.agregar_usuario(Usuario("U001", "Ana López", "ana@correo.com"))
    b.agregar_usuario(Usuario("U002", "Carlos Pérez", "carlos@correo.com"))

    titulo("Prueba 3: Registrar un libro con código repetido")
    b.agregar_libro(Libro("L001", "Otro libro", "Otro autor", 2000))

    titulo("Prueba 4: Realizar un préstamo correctamente")
    b.realizar_prestamo("U001", "L001", date(2026, 11, 10))

    titulo("Prueba 5: Prestar un libro que ya está prestado")
    b.realizar_prestamo("U002", "L001", date(2026, 11, 11))

    titulo("Prueba 6: Préstamo con un usuario que no existe")
    b.realizar_prestamo("U999", "L002", date(2026, 11, 11))

    titulo("Préstamos activos")
    b.mostrar_prestamos()

    titulo("Prueba extra: Devolución con fecha anterior a la salida")
    b.devolver_libro("L001", date(2026, 11, 5))

    titulo("Prueba 7: Devolver un libro")
    b.devolver_libro("L001", date(2026, 11, 13))

    titulo("Prueba 8: Buscar un libro existente")
    libro = b.buscar_libro("L002")
    if libro is not None:
        libro.mostrar_informacion()

    titulo("Prueba 9: Buscar un libro que no existe")
    resultado = b.buscar_libro("L999")
    print(f"Resultado de la búsqueda: {resultado}")

    titulo("Prueba 10: Mostrar libros y comprobar estados")
    b.realizar_prestamo("U002", "L003", date(2026, 11, 13))
    b.mostrar_libros()

    titulo("Historial de entradas y salidas")
    b.mostrar_historial()

    titulo("Préstamos activos al final")
    b.mostrar_prestamos()


if __name__ == "__main__":
    ejecutar_pruebas()