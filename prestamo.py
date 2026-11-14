from datetime import date


class Prestamo:
    def __init__(self, usuario, libro, fecha_salida=None):
        self.__usuario = usuario
        self.__libro = libro
        if fecha_salida is None:
            fecha_salida = date.today()
        self.__fecha_salida = fecha_salida
        self.__fecha_entrada = None

    @property
    def usuario(self):
        return self.__usuario

    @property
    def libro(self):
        return self.__libro

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    def registrar_entrada(self, fecha=None):
        if fecha is None:
            fecha = date.today()
        if fecha < self.__fecha_salida:
            return False
        self.__fecha_entrada = fecha
        return True

    def esta_activo(self):
        return self.__fecha_entrada is None

    def mostrar_informacion(self):
        salida = self.__fecha_salida.strftime("%d/%m/%Y")
        if self.__fecha_entrada is None:
            entrada = "Pendiente"
        else:
            entrada = self.__fecha_entrada.strftime("%d/%m/%Y")
        print(f"Préstamo -> Usuario: {self.__usuario.obtener_nombre()} "
              f"(carnet {self.__usuario.obtener_carnet()}) | "
              f"Libro: {self.__libro.titulo} (código {self.__libro.obtener_codigo()}) | "
              f"Salida: {salida} | Entrada: {entrada}")

    def obtener_usuario(self):
        return self.__usuario

    def obtener_libro(self):
        return self.__libro