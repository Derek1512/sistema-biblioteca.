class Usuario:
    def __init__(self, carnet, nombre, correo):
        self.__carnet = carnet
        self.__nombre = nombre
        self.__correo = correo
        self.__prestamos = []

    @property
    def carnet(self):
        return self.__carnet

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):
        print(f"Carnet: {self.__carnet} | Nombre: {self.__nombre} | "
              f"Correo: {self.__correo} | "
              f"Préstamos activos: {len(self.__prestamos)}")

    def obtener_carnet(self):
        return self.__carnet

    def obtener_nombre(self):
        return self.__nombre

    def agregar_prestamo(self, prestamo):
        self.__prestamos.append(prestamo)

    def quitar_prestamo(self, prestamo):
        if prestamo in self.__prestamos:
            self.__prestamos.remove(prestamo)
            return True
        return False

    def obtener_prestamos(self):
        return list(self.__prestamos)