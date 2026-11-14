class Prestamo: 
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro
 
    @property
    def usuario(self):
        return self.__usuario
 
    @property
    def libro(self):
        return self.__libro
 
    def mostrar_informacion(self):
        print(f"Préstamo -> Usuario: {self.__usuario.obtener_nombre()} "
              f"(carnet {self.__usuario.obtener_carnet()}) | "
              f"Libro: {self.__libro.titulo} (código {self.__libro.obtener_codigo()})")
 
    def obtener_usuario(self):
        return self.__usuario
 
    def obtener_libro(self):
        return self.__libro