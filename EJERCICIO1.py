class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que cero.")

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El nuevo precio debe ser mayor que cero.")

    def obtener_precio(self):
        return self.__precio

    def obtener_nombre(self):
        return self.__nombre

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.__precio -= self.__precio * (porcentaje / 100)
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

# Ejemplo de uso
producto = Producto("Laptop", 1200)
print(f"Producto: {producto.obtener_nombre()}, Precio: ${producto.obtener_precio()}")

producto.cambiar_precio(1100)
print(f"Nuevo Precio: ${producto.obtener_precio()}")

producto.aplicar_descuento(10)
print(f"Precio con descuento: ${producto.obtener_precio()}")
