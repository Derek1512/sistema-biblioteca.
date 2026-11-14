class Libro:
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"

    def __init__(self, codigo, titulo, autor, anio):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__estado = Libro.DISPONIBLE

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def anio(self):
        return self.__anio

    @property
    def estado(self):
        return self.__estado

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo} | Título: {self.__titulo} | "
              f"Autor: {self.__autor} | Año: {self.__anio} | "
              f"Estado: {self.__estado}")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in (Libro.DISPONIBLE, Libro.PRESTADO):
            self.__estado = nuevo_estado
            return True
        return False

    def obtener_codigo(self):
        return self.__codigo

    def obtener_estado(self):
        return self.__estado

    def esta_disponible(self):
        return self.__estado == Libro.DISPONIBLE

    def prestar(self):
        return self.cambiar_estado(Libro.PRESTADO)

    def devolver(self):
        return self.cambiar_estado(Libro.DISPONIBLE)