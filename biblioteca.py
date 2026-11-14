from libro import Libro
from usuario import Usuario
from prestamo import Prestamo


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []
        self.__historial = []

    def agregar_libro(self, libro):
        if self.buscar_libro(libro.obtener_codigo()) is not None:
            print(f"Error: ya existe un libro con el código {libro.obtener_codigo()}.")
            return False
        self.__libros.append(libro)
        print(f"Libro '{libro.titulo}' registrado correctamente.")
        return True

    def buscar_libro(self, codigo):
        for libro in self.__libros:
            if libro.obtener_codigo() == codigo:
                return libro
        return None

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro is None:
            print("Error: el libro no existe.")
            return False
        if not libro.esta_disponible():
            print("Error: no se puede eliminar un libro que está prestado.")
            return False
        self.__libros.remove(libro)
        print(f"Libro '{libro.titulo}' eliminado.")
        return True

    def mostrar_libros(self):
        if len(self.__libros) == 0:
            print("No hay libros registrados.")
            return
        for libro in self.__libros:
            libro.mostrar_informacion()

    def agregar_usuario(self, usuario):
        if self.buscar_usuario(usuario.obtener_carnet()) is not None:
            print(f"Error: ya existe un usuario con el carnet {usuario.obtener_carnet()}.")
            return False
        self.__usuarios.append(usuario)
        print(f"Usuario '{usuario.obtener_nombre()}' registrado correctamente.")
        return True

    def buscar_usuario(self, carnet):
        for usuario in self.__usuarios:
            if usuario.obtener_carnet() == carnet:
                return usuario
        return None

    def mostrar_usuarios(self):
        if len(self.__usuarios) == 0:
            print("No hay usuarios registrados.")
            return
        for usuario in self.__usuarios:
            usuario.mostrar_informacion()

    def realizar_prestamo(self, carnet, codigo, fecha=None):
        usuario = self.buscar_usuario(carnet)
        if usuario is None:
            print("Error: el usuario no existe. Préstamo cancelado.")
            return False

        libro = self.buscar_libro(codigo)
        if libro is None:
            print("Error: el libro no existe. Préstamo cancelado.")
            return False

        if not libro.esta_disponible():
            print("Error: el libro ya está prestado. Préstamo cancelado.")
            return False

        prestamo = Prestamo(usuario, libro, fecha)
        self.__prestamos.append(prestamo)
        usuario.agregar_prestamo(prestamo)
        libro.prestar()
        print(f"Préstamo realizado: '{libro.titulo}' -> {usuario.obtener_nombre()} "
              f"(salida: {prestamo.fecha_salida.strftime('%d/%m/%Y')}).")
        return True

    def devolver_libro(self, codigo, fecha=None):
        libro = self.buscar_libro(codigo)
        if libro is None:
            print("Error: el libro no existe.")
            return False

        if libro.esta_disponible():
            print("Error: el libro no está prestado.")
            return False

        prestamo_encontrado = None
        for prestamo in self.__prestamos:
            if prestamo.obtener_libro() is libro:
                prestamo_encontrado = prestamo
                break

        if prestamo_encontrado is None:
            print("Error: no se encontró el préstamo del libro.")
            return False

        if not prestamo_encontrado.registrar_entrada(fecha):
            print("Error: la fecha de entrada no puede ser anterior a la fecha de salida.")
            return False

        prestamo_encontrado.obtener_usuario().quitar_prestamo(prestamo_encontrado)
        self.__prestamos.remove(prestamo_encontrado)
        self.__historial.append(prestamo_encontrado)
        libro.devolver()
        print(f"Libro '{libro.titulo}' devuelto correctamente "
              f"(entrada: {prestamo_encontrado.fecha_entrada.strftime('%d/%m/%Y')}).")
        return True

    def mostrar_prestamos(self):
        if len(self.__prestamos) == 0:
            print("No hay préstamos activos.")
            return
        for prestamo in self.__prestamos:
            prestamo.mostrar_informacion()

    def mostrar_historial(self):
        if len(self.__historial) == 0:
            print("No hay movimientos en el historial.")
            return
        for prestamo in self.__historial:
            prestamo.mostrar_informacion()