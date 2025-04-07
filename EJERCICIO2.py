class Rectangulo:
    def __init__(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")

    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Las nuevas dimensiones deben ser mayores que cero.")

    def calcular_area(self):
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)

    def obtener_dimensiones(self):
        return self.__largo, self.__ancho

# Ejemplo de uso
rectangulo = Rectangulo(10, 5)
print(f"Dimensiones: {rectangulo.obtener_dimensiones()}")
print(f"Área: {rectangulo.calcular_area()}")
print(f"Perímetro: {rectangulo.calcular_perimetro()}")

rectangulo.cambiar_dimensiones(15, 7)
print(f"Nuevas dimensiones: {rectangulo.obtener_dimensiones()}")
print(f"Nueva Área: {rectangulo.calcular_area()}")
print(f"Nuevo Perímetro: {rectangulo.calcular_perimetro()}")
